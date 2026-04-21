import os
import time
import logging
import argparse
import pandas as pd
from sqlgen import run_sql_generation
from db_setup import run_database_setup, Generate_master_script
from ingestion import run_ingestion
from utils import clean_name
from dim import create_dimensions_sql
from fact import create_facts_sql
from utils import clean_name
from db_connection import get_engine
from sqlalchemy import inspect

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("log/pipeline.log"),
            logging.StreamHandler()
        ]
    )

def run_modeling(table_name):
    engine = get_engine()
    df = pd.read_sql(f"SELECT * FROM staging.{table_name}", engine)
    base_name = clean_name(table_name)
    dim_table = create_dimensions_sql(df, base_name)
    fact_table = create_facts_sql(df, base_name)

    print("STAR SCHEMA CREATED")
    print("DIMS:", dim_table)
    print("FACT:", fact_table)

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
    #Generate_master_script("staging")
    logging.info("STEP 2 DONE")

    # STEP 3
    logging.info("STEP 3: INGESTION")
    #run_ingestion()
    logging.info("STEP 3 DONE")

    # STEP 4
    engine = get_engine()
    inspector = inspect(engine)
    tables = inspector.get_table_names(schema="staging")
    print(tables)
    logging.info("STEP 4: STAR SCHEMA GENERATION")

    #for table_name in tables:
        #run_modeling(table_name)

    logging.info("STEP 4 DONE")

    logging.info(f" PIPELINE COMPLETE in {round(time.time()-start,2)}s")


if __name__ == "__main__":
    main()