def generate_dim_table(schema, dim_name, values):
    table = f"CREATE TABLE {schema}.dim_{dim_name} (id INT IDENTITY(1,1), value VARCHAR(255));"
    return table

def generate_fact_table(schema, fact_name, fact_cols):
    cols_sql = ",\n".join([f"{col} DECIMAL(18,2) NULL" for col in fact_cols])

    return f"""
    CREATE TABLE {schema}.fact_{fact_name} (
        id INT IDENTITY(1,1),
        {cols_sql}
    );
    """