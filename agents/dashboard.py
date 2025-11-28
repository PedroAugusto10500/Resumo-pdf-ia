import streamlit as st
import pandas as pd
import json
import os

st.set_page_config(page_title="📊 Dashboard PDF Assistant", layout="wide")
st.title("📊 Dashboard de Uso do PDF Assistant")

def load_logs():
    path = "outputs/usage_log.json"
    if not os.path.exists(path):
        return pd.DataFrame()
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    data = []
    for line in lines:
        try:
            data.append(json.loads(line))
        except:
            pass
    if data:
        return pd.DataFrame(data)
    else:
        return pd.DataFrame()

df = load_logs()

if df.empty:
    st.info("Nenhum log encontrado ainda.")
else:
    st.dataframe(df)
    st.download_button("📥 Baixar CSV", df.to_csv(index=False), "logs.csv", mime="text/csv")
