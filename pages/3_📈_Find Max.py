import streamlit as st
import pandas as pd
from tools.dictonaries import categories
from tools.clean import cleaning
from tools.functions import find_max

percents = pd.read_csv('datasets\GDP_coun31_12-20_cat80.csv')
millions = pd.read_csv('datasets\MIL_coun31_12-20_cat80.csv')
TotalGDP = pd.read_csv('datasets\mil_GDP_TOTAL_31_12-20.csv')

df_percs = cleaning(percents)
df_money = cleaning(millions)
e = NameError('Please upload a file from sidebar')
st.title("Find Max")

with st.sidebar:
    cateFullDecs = list(categories.values())
    dataset = st.sidebar.selectbox("Select Dataset",['Percentage', 'Millions', 'My Dataset'])
    if dataset == 'My Dataset':
        file = st.sidebar.file_uploader("Choose a CSV file",type=['csv'] )
        if file is not None:
            dataframe = pd.read_csv(file)
            dataframe = cleaning(dataframe)				

    elif dataset == 'Percentage':
        dataframe = df_percs

    elif dataset == 'Millions':
        dataframe = df_money

    categoryChoice = st.sidebar.selectbox("Categories",cateFullDecs)


col1, col2 = st.columns(2,gap='large')


with col1:
    categoryCode =list(categories.keys())[list(categories.values()).index(categoryChoice)]
    st.header("Find Max")
    
    try:
        maxdf=find_max(dataframe,Category=categoryCode)
        maxdf.set_index('Country',inplace=True)
        st.bar_chart(maxdf,x='Year',y='Value')
    except:
        st.exception(e)
with col2:
    st.subheader(f"{categoryChoice}")
    # st.checkbox("Use container width", value=True, key="use_container_width")
    try:
        st.dataframe(maxdf,use_container_width=True)
    except:
        pass