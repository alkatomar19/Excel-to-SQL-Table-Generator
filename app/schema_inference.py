import pandas as pd
import re
import numpy as np

def profile_column(series):
    return {
        "null_pct": series.isnull().mean(),
        "unique_count": series.nunique(),
        "total_count": len(series),
        "is_unique": series.nunique() == len(series),
        "sample_values": series.dropna().head(5).tolist()
    }

def clean_column_name(col):
    col = col.strip()
    col = re.sub(r'[^\w]+', '_', col)
    return col.lower()

def infer_sql_type(series):
    series_non_null = series.dropna()

    # Boolean detection
    if series_non_null.isin([0, 1, True, False]).all():
        return "BIT"

    # Integer
    if pd.api.types.is_integer_dtype(series):
        return "INT"

    # Float → detect precision
    if pd.api.types.is_float_dtype(series):
        max_val = series_non_null.max()
        precision = len(str(int(max_val))) + 2
        return f"DECIMAL({precision},2)"

    # Date detection (even if object)
    try:
        parsed = pd.to_datetime(series_non_null, errors='raise')
        return "DATETIME"
    except:
        pass

    # String length optimization
    max_len = series.astype(str).str.len().max()

    if max_len < 50:
        return f"VARCHAR({max_len})"
    elif max_len < 255:
        return "VARCHAR(255)"
    else:
        return "VARCHAR(MAX)"
        
def detect_primary_key(df):
    for col in df.columns:
        profile = profile_column(df[col])
        if profile["is_unique"] and profile["null_pct"] == 0:
            return col
    return None

def add_surrogate_key(columns):
    return ["    id INT IDENTITY(1,1) PRIMARY KEY"] + columns

def null_constraint(series):
    if series.isnull().mean() > 0:
        return "NULL"
    return "NOT NULL"

def generate_create_table_advanced(df, table_name, schema="stg"):
    columns_sql = []
    
    pk = detect_primary_key(df)

    for col in df.columns:
        clean_col = clean_column_name(col)
        sql_type = infer_sql_type(df[col])
        nulls = null_constraint(df[col])

        col_def = f"    {clean_col} {sql_type} {nulls}"

        # Mark primary key
        if col == pk:
            col_def += " PRIMARY KEY"

        columns_sql.append(col_def)

    # If no PK → add surrogate key
    if pk is None:
        columns_sql = add_surrogate_key(columns_sql)

    # Add metadata columns (DW style)
    columns_sql.append("    created_at DATETIME DEFAULT GETDATE()")

    return f"""
CREATE TABLE {schema}.{table_name} (
{',\n'.join(columns_sql)}
);
"""

def generate_data_report(df):
    report = []

    for col in df.columns:
        profile = profile_column(df[col])

        report.append({
            "column": col,
            "null_pct": round(profile["null_pct"] * 100, 2),
            "unique_values": profile["unique_count"],
            "is_unique": profile["is_unique"]
        })

    return pd.DataFrame(report)

def classify_table(df):
    num_cols = 0
    text_cols = 0

    for col in df.columns:
        dtype = df[col].dtype

        if "int" in str(dtype) or "float" in str(dtype):
            num_cols += 1
        else:
            text_cols += 1

    total = len(df.columns)

    num_ratio = num_cols / total
    text_ratio = text_cols / total

    # Heuristic rules
    if num_ratio > 0.6:
        return "fact"
    elif text_ratio > 0.6:
        return "dimension"
    else:
        return "dimension"  # default safer
    
def add_scd2_columns(columns_sql):
    scd_cols = [
        "    effective_date DATETIME",
        "    expiry_date DATETIME",
        "    is_current BIT"
    ]
    return columns_sql + scd_cols

def generate_table_with_dw_logic(df, table_name):
    table_type = classify_table(df)

    schema = "dim" if table_type == "dimension" else "fact"

    columns_sql = []

    pk = detect_primary_key(df)

    for col in df.columns:
        clean_col = clean_column_name(col)
        sql_type = infer_sql_type(df[col])
        nulls = null_constraint(df[col])

        col_def = f"    {clean_col} {sql_type} {nulls}"

        if col == pk:
            col_def += " PRIMARY KEY"

        columns_sql.append(col_def)

    # Add surrogate key for dimensions
    if table_type == "dimension":
        columns_sql.insert(0, "    id INT IDENTITY(1,1) PRIMARY KEY")

    # Add SCD Type 2 columns ONLY for dimensions
    if table_type == "dimension":
        columns_sql = add_scd2_columns(columns_sql)

    # Add metadata
    columns_sql.append("    created_at DATETIME DEFAULT GETDATE()")

    return f"""
-- Detected as: {table_type.upper()}
CREATE TABLE {schema}.{table_name} (
{',\n'.join(columns_sql)}
);
"""
def detect_measures(df):
    measures = []

    for col in df.columns:
        col_lower = col.lower()

        if ("id" in col_lower):
            continue  # skip keys

        dtype = df[col].dtype

        if "int" in str(dtype) or "float" in str(dtype):
            measures.append(col)

    return measures

def detect_foreign_keys(df, primary_key):
    fks = []

    for col in df.columns:
        col_lower = col.lower()

        if col == primary_key:
            continue

        if col_lower.endswith("_id"):
            if df[col].nunique() < len(df):  # repeating → likely FK
                fks.append(col)

    return fks

def generate_index_statements(table_name, schema, primary_key, foreign_keys):
    indexes = []

    # PK index (usually auto-created, but we show it)
    if primary_key:
        indexes.append(
            f"CREATE CLUSTERED INDEX idx_{table_name}_{primary_key} ON {schema}.{table_name}({primary_key});"
        )

    # FK indexes
    for fk in foreign_keys:
        indexes.append(
            f"CREATE NONCLUSTERED INDEX idx_{table_name}_{fk} ON {schema}.{table_name}({fk});"
        )

    return indexes

def generate_full_dw_script(df, table_name):
    table_type = classify_table(df)
    schema = "dim" if table_type == "dimension" else "fact"

    pk = detect_primary_key(df)
    fks = detect_foreign_keys(df, pk)
    measures = detect_measures(df)

    columns_sql = []

    for col in df.columns:
        clean_col = clean_column_name(col)
        sql_type = infer_sql_type(df[col])
        nulls = null_constraint(df[col])

        col_def = f"    {clean_col} {sql_type} {nulls}"

        if col == pk:
            col_def += " PRIMARY KEY"

        columns_sql.append(col_def)

    # Dimension logic
    if table_type == "dimension":
        columns_sql.insert(0, "    id INT IDENTITY(1,1) PRIMARY KEY")
        columns_sql = add_scd2_columns(columns_sql)

    columns_sql.append("    created_at DATETIME DEFAULT GETDATE()")

    create_stmt = f"""
-- Detected as: {table_type.upper()}
-- Measures: {measures}
-- Foreign Keys: {fks}

CREATE TABLE {schema}.{table_name} (
{',\n'.join(columns_sql)}
);
"""

    # Indexes
    index_statements = generate_index_statements(table_name, schema, pk, fks)

    return create_stmt + "\n\n" + "\n".join(index_statements)

def get_business_key(primary_key):
    return primary_key  # or smarter logic later

def get_attribute_columns(df, pk):
    return [col for col in df.columns if col != pk]

def generate_scd2_merge(table_name, df, pk, schema="dim"):
    business_key = pk
    attributes = get_attribute_columns(df, pk)

    compare_condition = " OR ".join([
        f"TARGET.{col} <> SOURCE.{col}" for col in attributes
    ])

    update_set = ", ".join([
        f"{col} = SOURCE.{col}" for col in attributes
    ])

    insert_columns = ", ".join([business_key] + attributes + [
        "effective_date", "expiry_date", "is_current"
    ])

    insert_values = ", ".join([
        f"SOURCE.{business_key}"
    ] + [f"SOURCE.{col}" for col in attributes] + [
        "GETDATE()", "'9999-12-31'", "1"
    ])

    merge_sql = f"""
MERGE {schema}.{table_name} AS TARGET
USING stg.{table_name} AS SOURCE
ON TARGET.{business_key} = SOURCE.{business_key}
AND TARGET.is_current = 1

WHEN MATCHED AND ({compare_condition}) THEN
    UPDATE SET
        TARGET.expiry_date = GETDATE(),
        TARGET.is_current = 0

WHEN NOT MATCHED THEN
    INSERT ({insert_columns})
    VALUES ({insert_values});
"""

    return merge_sql

