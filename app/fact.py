import os
from utils import classify_column


def create_facts_sql(df, base_name):
    fact_cols = []

    for col in df.columns:
        if classify_column(df, col) == "fact":
            fact_cols.append(col)

    sql = f"""
CREATE TABLE fact.{base_name} (
"""

    for col in fact_cols:
        sql += f"    {col} FLOAT,\n"

    sql = sql.rstrip(",\n") + "\n);"

    os.makedirs("output/fact", exist_ok=True)

    with open(f"output/fact/fact_{base_name}.sql", "w") as f:
        f.write(sql)

    return f"fact_{base_name}"