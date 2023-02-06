import streamlit as st
import pandas as pd
import os
import requests as r
import numpy as np
import importlib
from clean import cleaning
from functions import find_max
from dictonaries import categories
millions = pd.read_csv('MIL_coun31_12-20_cat80.csv')
percents = pd.read_csv('GDP_coun31_12-20_cat80.csv')
TotalGDP = pd.read_csv('mil_GDP_TOTAL_31_12-20.csv')

BASE_URL = 'https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/'
# req = r.get('https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/GOV_10A_EXP?format=SDMX-CSV')
# req = r.get('https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/NAMA_10_GDP?format=SDMX-CSV?startPeriod=2012&endPeriod=2015')
# req = r.get('https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/GOV_10A_EXP/A.PC_GDP?format=SDMX-CSV&startPeriod=2012&endPeriod=2020')
dataset_code = 'GOV_10A_EXP'
# req = r.get(BASE_URL+dataset_code+'/A.PC_GDP.S13.TOTAL.TE.BG?format=SDMX-CSV&startPeriod=2012&endPeriod=2020')
# req.text

df_percs = cleaning(percents)
df_money = cleaning(millions)
e = NameError('Please upload a file from sidebar')
# print(req.text)
st.set_page_config(
    page_title="Data Analysis",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
activiteis= ['Home','Find max', 'Find min']
choice = st.sidebar.selectbox("Menu", activiteis)

# hide_st_style = """
#   <style>
#   #MainMenu {visibility: hidden;}
#   footer {visibility: hidden;}
#   </style>
# """
# st.markdown(hide_st_style, unsafe_allow_html=True)

if choice == 'Home':
	st.header('Data Analysis Project')

elif choice == 'Find max':
	st.title('Task 1')

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
	