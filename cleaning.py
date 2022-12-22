import pandas as pd

from dictionaries import financialSectors
from dictionaries import countries
from functions import cleaning

# Reading CSVs using pandas csv read

dfGDP = pd.read_csv("expensesGDP.csv")
dfActual = pd.read_csv('expensesActual.csv')

# Removing unnecesary data from both datasets using the cleaning function

dfGDP = cleaning(dfGDP)
dfActual = cleaning(dfActual)

# Replacing the coded data with their actual values in both datasets

# Dataset GDP
dfGDP['Category'] = dfGDP['Category'].replace(financialSectors)
dfGDP['Country'] = dfGDP['Country'].replace(countries)

# Dataset Actual
dfActual['Category'] = dfActual['Category'].replace(financialSectors)
dfActual['Country'] = dfActual['Country'].replace(countries)
