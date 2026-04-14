import os
import time
import logging
import argparse

from sqlgen import generate_create_table
from db_setup import run_database_setup
from ingestion import run_ingestion
from utils import clean_name

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("log/pipeline.log"),
            logging.StreamHandler()
        ]
    )


def run_sql_generation(data_folder="data", output_folder="output"):
    import pandas as pd

    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(data_folder):
        if not file.endswith(".xlsx"):
            continue

        path = os.path.join(data_folder, file)
        base = file.replace(".xlsx", "").lower()

        excel = pd.ExcelFile(path)

        for sheet in excel.sheet_names:
            df = excel.parse(sheet)

            if df.empty:
                continue

            #table = f"{base}_{sheet}".lower().replace(" ", "_")
            #table = f"{base}".lower().replace(" ", "_")
            table = clean_name(f"{base}")

            sql = generate_create_table(df, table)

            with open(f"{output_folder}/{table}.sql", "w") as f:
                f.write(sql)


def main():
    start = time.time()
    setup_logger()

    logging.info(" PIPELINE STARTED")

    # STEP 1
    logging.info("STEP 1: SQL GENERATION")
    #run_sql_generation("data",'staging')
    logging.info("STEP 1 DONE")

    # STEP 2
    logging.info("STEP 2: DATABASE SETUP")
    #run_database_setup()
    logging.info("STEP 2 DONE")

    # STEP 3
    logging.info("STEP 3: INGESTION")
    run_ingestion()
    logging.info("STEP 3 DONE")

    logging.info(f" PIPELINE COMPLETE in {round(time.time()-start,2)}s")


if __name__ == "__main__":
    main()