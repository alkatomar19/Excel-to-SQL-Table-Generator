import pandas as pd
import os
import logging
from sqlalchemy import text
from db_connection import get_engine
from utils import clean_name


def convert_yes_no(val):
    if isinstance(val, str):
        val = val.strip().upper()
        if val == "YES":
            return 1
        elif val == "NO":
            return 0
    return val

def run_ingestion(data_folder="data"):
    engine = get_engine()

    files = [f for f in os.listdir(data_folder) if f.endswith(".xlsx")]

    for file in files:
        path = os.path.join(data_folder, file)
        base = clean_name(file.replace(".xlsx", ""))

        excel = pd.ExcelFile(path)

        for sheet in excel.sheet_names:
            df = excel.parse(sheet)

            if df.empty:
                continue

            #table = f"staging.{clean_name(base)}_{clean_name(sheet)}"
            table = f"staging.{clean_name(base)}"
            df.columns = [clean_name(c) for c in df.columns]
            #  Convert YES/NO → 1/0 (for BIT compatibility)
            df = df.map(convert_yes_no)

            # handle NaN (avoid SQL issues)
            df = df.where(pd.notnull(df), None)
            df.to_sql(
                table.split(".")[1],
                engine,
                schema="staging",
                if_exists="append",
                index=False,
                chunksize=1000
            )

            logging.info(f"Loaded -> {table}")