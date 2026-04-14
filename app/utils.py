import pandas as pd
from sqlalchemy import inspect
def clean_name(name: str) -> str:
    import re

    name = name.strip().lower()

    #  Replace business symbols FIRST
    name = name.replace("#", "_id")
    name = name.replace("%", "_pct")
    name = name.replace("$", "_amt")
    name = re.sub(r"\bno\b", "number", name)  

    # Replace spaces and hyphens
    name = re.sub(r"[ -]+", "_", name)

    # Remove special characters
    # Replace special characters with underscore
    name = re.sub(r'[^a-z0-9_]', '_', name)

    # Replace multiple underscores
    name = re.sub(r'_+', '_', name)

    # Remove leading/trailing _
    name = name.strip('_')

    return name

def classify_column(df, col):
    col_series = df[col]

    # safety check (important for real Excel junk data)
    if col_series.empty:
        return "dim"

    # numeric → FACT candidate
    if pd.api.types.is_numeric_dtype(col_series):
        return "fact"

    # uniqueness ratio
    unique_ratio = col_series.nunique(dropna=True) / len(col_series)

    # low cardinality → DIM
    if unique_ratio < 0.3:
        return "dim"

    return "dim"

def build_star_schema(df):
    dims = {}
    facts = []

    for col in df.columns:
        role = classify_column(df, col)

        if role == "fact":
            facts.append(col)
        else:
            dims[col] = df[col].drop_duplicates()

    return dims, facts

def build_table_name(base: str, type_: str):
    base = clean_name(base)
    return f"staging.dim_{base}" if type_ == "dim" else f"staging.fact_{base}"

from sqlalchemy import inspect

def get_staging_tables(engine):
    inspector = inspect(engine)
    return inspector.get_table_names(schema="staging")