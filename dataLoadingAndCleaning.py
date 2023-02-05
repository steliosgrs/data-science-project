# imports
import pandas as pd
from dictionaries import financialSectors
from dictionaries import countries
from functions import cleaning, cleaningGDPActualValues

# Reading CSVs https://github.com/steliosgrs/data-science-project/blob/dev_vandl_new/analysis.pyusing pandas csv read

dfGDP = pd.read_csv("expensesGDP.csv") # Expenses expressed as percentage of the GDP
dfActual = pd.read_csv('expensesActual.csv') # Expences expressed in market value
dfGDPActual = pd.read_csv('gdpActualPerYear.csv') # Actual GDP per country per year

# Removing unnecessary data from both datasets using the cleaning function

dfGDP = cleaning(dfGDP)
dfActual = cleaning(dfActual)
dfGDPActual = cleaningGDPActualValues(dfGDPActual)


# Replacing the coded data with their actual values in both datasets

# Dataset GDP
dfGDP['Category'] = dfGDP['Category'].replace(financialSectors)
dfGDP['Country'] = dfGDP['Country'].replace(countries)

# Dataset Actual
dfActual['Category'] = dfActual['Category'].replace(financialSectors)
dfActual['Country'] = dfActual['Country'].replace(countries)

# Dataset GDP Actual
dfGDPActual['Country'] = dfGDPActual['Country'].replace(countries)


# Calculating more accurate gdp using gdpAccurate's function output and replacing
# the gdp's value with the one calculated
newGDP = pd.read_csv('dfGDPAcc.csv')
newGDP = newGDP.drop("Unnamed: 0", axis=1)

dfGDPAcc = dfGDP.drop(columns='Value') # Removing the old  gdp values from the dataset
dfGDPAcc['Value'] = newGDP.values








