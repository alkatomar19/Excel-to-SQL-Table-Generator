import pandas as pd
import re
import numpy as np
from utils import clean_name





# ---------------- PROFILE ----------------
def profile_column(series):
    return {
        "null_pct": series.isnull().mean(),
        "unique_count": series.nunique(),
        "total_count": len(series),
        "is_unique": series.nunique() == len(series)
    }


# ---------------- PK DETECTION ----------------
def detect_primary_key(df):
    for col in df.columns:
        if df[col].isnull().sum() == 0 and df[col].nunique() == len(df):
            return col
    return None


# ---------------- DATE CHECK ----------------
def is_date_column(series):
    series_non_null = series.dropna()

    if len(series_non_null) == 0:
        return False

    sample = series_non_null.sample(min(50, len(series_non_null)), random_state=42)

    try:
        parsed = pd.to_datetime(sample, errors='coerce', infer_datetime_format=True)
        
        success_ratio = parsed.notnull().mean()

        return success_ratio > 0.8  # threshold
    except:
        return False


# ---------------- TYPE INFERENCE ----------------
def infer_sql_type(series):
    s = series.dropna()

    if len(s) == 0:
        return "VARCHAR(50)"

    normalized = s.astype(str).str.lower().str.strip()

    # BOOLEAN
    if normalized.isin(['0','1','true','false','yes','no']).all():
        return "BIT"

    # FLOAT / INT
    if pd.api.types.is_float_dtype(s):
        if (s % 1 == 0).all():
            return "INT" if s.max() < 2_147_483_647 else "BIGINT"

        max_val = s.abs().max()
        int_part = len(str(int(max_val))) if max_val != 0 else 1

        decimal_part = s.astype(str).str.split('.').str[1].dropna()
        scale = decimal_part.map(len).max() if len(decimal_part) > 0 else 0

        return f"DECIMAL({min(int_part+scale,38)},{min(scale,10)})"

    # DATE
    if is_date_column(series):
        return "DATETIME"

    # STRING
    max_len = s.astype(str).str.len().max()

    if max_len <= 50:
        return f"VARCHAR({max_len})"
    elif max_len <= 255:
        return "VARCHAR(255)"
    elif max_len <= 1000:
        return "VARCHAR(1000)"
    else:
        return "VARCHAR(MAX)"


# ---------------- NULL RULE ----------------
def null_constraint(series):
    return "NULL" if series.isnull().any() else "NOT NULL"


# ---------------- CREATE TABLE ----------------
def generate_create_table(df, table_name, schema="staging"):
    columns = []
    pk = detect_primary_key(df)

    if pk is None:
        columns.append("id INT IDENTITY(1,1) PRIMARY KEY")

    for col in df.columns:        
        clean_col = clean_name(col)
        sql_type = infer_sql_type(df[col])
        nulls = null_constraint(df[col])

        col_def = f"{clean_col} {sql_type} {nulls}"
        columns.append(col_def)

    columns.append("created_at DATETIME DEFAULT GETDATE()")

    joined = ',\n'.join(columns)
    return f"""
    CREATE TABLE {schema}.{table_name} (
    {joined}
    );
    """