#!/usr/bin/env python3
"""
Example of loading CSV into Postgres (via pandas.to_sql).
Uses environment variables (via .env).
"""
import argparse
import os
from pathlib import Path
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()  # read .env if exists 

def get_engine():
    user = os.getenv("DB_USER", "user")
    pw = os.getenv("DB_PASS", "pass")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5433")
    db = os.getenv("DB_NAME", "warehouse")
    url = f"postgresql://{user}:{pw}@{host}:{port}/{db}"
    return create_engine(url, echo=False)

def load_csv_to_table(csv_path: str, table_name: str, if_exists="append"):
    df = pd.read_csv(csv_path)
    engine = get_engine()
    df.to_sql(table_name, engine, if_exists=if_exists, index=False)
    print(f"Loaded {len(df)} rows into {table_name}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Path to CSV file")
    parser.add_argument("--table", required=True, help="Destination table name")
    args = parser.parse_args()
    load_csv_to_table(args.file, args.table)

if __name__ == "__main__":
    main()
