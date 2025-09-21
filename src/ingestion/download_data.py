#!/usr/bin/env python3
"""
Example: downloads a CSV from a URL and saves it in data/raw/<basename>.
"""
import argparse
import logging
from pathlib import Path
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)

def download_csv(url: str) -> Path:
    logger.info("Downloading %s", url)
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    name = url.split("/")[-1] or "data.csv"
    out = DATA_DIR / name
    out.write_bytes(resp.content)
    logger.info("Saved to %s", out)
    return out

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, help="CSV URL to download")
    args = parser.parse_args()
    download_csv(args.url)

if __name__ == "__main__":
    main()
