import os
import logging
from sqlalchemy import text
from db_connection import get_engine


def extract_table_name(sql):
    """
    Extract table name from CREATE TABLE statement
    """
    import re
    match = re.search(r'CREATE TABLE\s+([^\s(]+)', sql, re.IGNORECASE)
    return match.group(1) if match else None


def drop_table_if_exists(conn, table_name):
    drop_sql = f"""
    IF OBJECT_ID('{table_name}', 'U') IS NOT NULL
        DROP TABLE {table_name}
    """
    conn.execute(text(drop_sql))


def run_database_setup(sql_folder="staging"):
    engine = get_engine()

    logging.info(" STEP 2: Creating staging tables")

    sql_files = [f for f in os.listdir(sql_folder) if f.endswith(".sql")]

    for file in sql_files:
        path = os.path.join(sql_folder, file)

        try:
            with open(path, "r", encoding="utf-8") as f:
                sql = f.read()

            table_name = extract_table_name(sql)

            with engine.begin() as conn:
                if table_name:
                    logging.info(f" Dropping if exists: {table_name}")
                    drop_table_if_exists(conn, table_name)

                logging.info(f" Creating: {table_name}")
                conn.execute(text(sql))

            logging.info(f" Created: {file}")

        except Exception as e:
            logging.error(f" Failed: {file} → {e}")