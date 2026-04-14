import pandas as pd

def clean_name(name: str) -> str:
    import re

    name = name.strip().lower()

    # 🔥 Replace business symbols FIRST
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
    unique_ratio = df[col].nunique() / len(df)

    # numeric → FACT
    if pd.api.types.is_numeric_dtype(df[col]):
        return "fact"

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
            dims[col] = df[col].unique()

    return dims, facts