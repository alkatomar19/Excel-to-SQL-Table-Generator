import streamlit as st
import pandas as pd
from schema_inference import generate_create_table

st.title("Excel to SQL Table Generator")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

table_name = st.text_input("Table Name", "stg_table")

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    
    st.write("Preview Data:")
    st.dataframe(df.head())

    sql = generate_create_table(df, table_name)

    st.code(sql, language="sql")

    st.download_button(
        label="Download SQL",
        data=sql,
        file_name=f"{table_name}.sql",
        mime="text/plain"
    )