import os
import streamlit as st
from utils.utils import sql_query_with_user_token, read_file
from utils.constants import SQL_PATH
from components.figures import revenue_hbar

# Ensure environment variable is set correctly
assert os.getenv('DATABRICKS_WAREHOUSE_ID'), "DATABRICKS_WAREHOUSE_ID must be set in app.yaml."

st.header("Supply chain DataCo dashboard")

user_token = st.context.headers.get('X-Forwarded-Access-Token')

data = sql_query_with_user_token("SELECT * FROM supply_chain_demo.gold.mart_puerto_rico LIMIT 1000;", user_token=user_token)

product_revenue = sql_query_with_user_token(read_file(SQL_PATH / "product_revenue.sql"), user_token=user_token)

revenue_hbar(product_revenue)

st.dataframe(data=product_revenue)


st.dataframe(data=data, height=600, use_container_width=True)
