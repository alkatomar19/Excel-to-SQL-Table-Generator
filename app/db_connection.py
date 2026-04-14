import sqlalchemy as sa
import urllib

import configparser
import os

from settings import SQL_CONFIG

server = SQL_CONFIG["server"]

def get_engine():   

    server = SQL_CONFIG["server"]
    database = SQL_CONFIG["database"]
    driver = SQL_CONFIG["driver"]    

    params = urllib.parse.quote_plus(
        f"DRIVER={driver};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"Trusted_Connection=yes;"
    )

    conn_str = f"mssql+pyodbc:///?odbc_connect={params}"

    return sa.create_engine(conn_str)

