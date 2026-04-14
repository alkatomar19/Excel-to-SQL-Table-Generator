import os
from utils import classify_column


def create_dimensions_sql(df, base_name):
    dim_cols = []

    for col in df.columns:
        if classify_column(df, col) == "dim":
            dim_cols.append(col)

    sql = f"""
CREATE TABLE dim.{base_name} (
"""

    for col in dim_cols:
        sql += f"    {col} VARCHAR(255),\n"

    sql = sql.rstrip(",\n") + "\n);"

    os.makedirs("output/dim", exist_ok=True)

    with open(f"output/dim/dim_{base_name}.sql", "w") as f:
        f.write(sql)

    return f"dim_{base_name}"