import streamlit as st
import pandas as pd
from streamlit_extras.dataframe_explorer import dataframe_explorer
from tools.dictonaries import categories
from tools.clean import cleaning

percents = pd.read_csv('datasets\GDP_coun31_12-20_cat80.csv')
millions = pd.read_csv('datasets\MIL_coun31_12-20_cat80.csv')
TotalGDP = pd.read_csv('datasets\mil_GDP_TOTAL_31_12-20.csv')


df_percs = cleaning(percents)
df_money = cleaning(millions)

st.title("Dataset Exploration")


# with st.sidebar:
cateFullDecs = list(categories.values())
dataset = st.selectbox("Select Dataset",['Percentage', 'Millions', 'My Dataset'])
# dataset = st.sidebar.selectbox("Select Dataset",['Percentage', 'Millions', 'My Dataset'])
if dataset == 'My Dataset':
    file = st.sidebar.file_uploader("Choose a CSV file",type=['csv'] )
    if file is not None:
        dataframe = pd.read_csv(file)
        dataframe = cleaning(dataframe)				

elif dataset == 'Percentage':
    dataframe = df_percs

elif dataset == 'Millions':
    dataframe = df_money


fl_df = dataframe_explorer(dataframe)
st.dataframe(fl_df, use_container_width=True)
    # categoryChoice = st.sidebar.selectbox("Categories",cateFullDecs)
