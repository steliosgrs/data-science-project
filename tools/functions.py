import pandas as pd
import numpy as np
from tools.dictonaries import countries, categories

# Return a dataframe depending on the given argument 
def which_category(df,Category):
    if Category == 'TOTAL':
        total_values = df.loc[df['Category'] == 'TOTAL']
    elif Category == 'All':
        total_values = df.loc[df['Category'] != 'TOTAL']
    else:
        total_values = df.loc[df['Category'] == Category]
    return total_values

# Finding the max entries for every year
def find_max(df:pd.DataFrame, Category='TOTAL'):

    total_values = which_category(df,Category)
    maxs = total_values.groupby('Year')['Value'].idxmax()

    df.replace(to_replace=list(categories.keys()), value=list(categories.values()), inplace=True)
    df.replace(to_replace=list(countries.keys()), value=list(countries.values()), inplace=True)
    df.drop('Category', axis=1,inplace=True)

    return df.loc[maxs]

def find_min_inEU(df:pd.DataFrame):
    df = df.loc[df['Country'] == 'EU27_2020']
    index_min = df['Value'].astype(float).idxmin(axis=0)
    return df.loc[index_min]

