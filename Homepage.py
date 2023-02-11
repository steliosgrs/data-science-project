import streamlit as st
import pandas as pd
import numpy as np
from tools.clean import cleaning
from tools.dictonaries import categories

# Datasets
millions = pd.read_csv('datasets/MIL_coun31_12-20_cat80.csv')
percents = pd.read_csv('datasets/GDP_coun31_12-20_cat80.csv')
TotalGDP = pd.read_csv('datasets/mil_GDP_TOTAL_31_12-20.csv')

# Clean datasets
df_percs = cleaning(percents)
df_money = cleaning(millions)

e = NameError('Please upload a file from sidebar')

# Basic configuration for the web application
st.set_page_config(
    page_title="Home Page",
    page_icon="🚩",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.write("TODO: Add Documentation")

	

	