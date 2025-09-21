import streamlit as st
import pandas as pd
from pathlib import Path

st.title("Demo ETL — list of files â data/raw")
p = Path("data/raw")
csvs = list(p.glob("*.csv"))
st.write("Find CSV:", [str(x.name) for x in csvs])

if csvs:
    df = pd.read_csv(csvs[0])
    st.write("Preview:", df.head())
