import pandas as pd
import numpy as np
from clean import cleaning
from dictonaries import countries, categories

# Return a dataframe depending on the given argument 
def which_category(df,Category):
    if Category == 'TOTAL':
        # total_values = df.loc[df['Category'] == Category]
        total_values = df.loc[df['Category'] == 'TOTAL']
    elif Category == 'all':
        total_values = df.loc[df['Category'] != 'TOTAL']
    else:
        total_values = df.loc[df['Category'] == Category]
    return total_values

# Finding the max entries for every year
def find_max(df:pd.DataFrame, Category='TOTAL'):
    total_max_year = pd.DataFrame()
    total_values = which_category(df,Category)

    # Take the year range of the dataset 
    # eg. if 2012-2020 years = [2012, 2013, ... 2019, 2020]
    years = df.Year.unique()

    for year in range(years.__len__()):
        df_year = total_values.loc[total_values['Year'] == years[year]]

        # Find max and the index of max
        max_idnex = df_year['Value'].astype(float).idxmax(axis=0)
        total_max = np.max(df_year.Value.values)

        # Find and match country
        countryCode = total_values.loc[max_idnex].Country
        country = countries[countryCode]

        # Find and match category
        categoryCode = total_values.loc[max_idnex].Category
        category  = categories[categoryCode]

        # Create new row
        row = {
            "Country":country,
            "Year":years[year],
            "Category":category,
            "Value":total_max,
            }
        row = pd.DataFrame(row,index=[0])

        # Append row in dataframe
        total_max_year = pd.concat([total_max_year, row],ignore_index=True)

    return total_max_year

def find_min(df:pd.DataFrame):
    df = df.loc[df['Country'] == 'EU27_2020']
    index_min = df['Value'].astype(float).idxmin(axis=0)
    min = df.min()
    return df.loc[index_min]

# Finds max by category every year for every country
def max_by_category(df:pd.DataFrame):
    wout_total = df.loc[df['Category'] != 'TOTAL']
    categories_max = pd.DataFrame()
    country_keys = countries.keys()
    years = df.Year.unique()

    for year in range(years.__len__()):
        df_year = wout_total.loc[wout_total['Year'] == years[year]]

        for key in country_keys:
            df_country = df_year.loc[df_year['Country'] == key]
            max_idnex = df_country.Value.astype(int).idxmax(axis=0)
            category_max = np.max(df_country.Value.values)
            categoryCode = df_country.loc[max_idnex].Category
            category  = categories[categoryCode]
            row = {
                "Country":countries[key],
                "Category":category,
                "Year":years[year],
                "Value":category_max
            }
            row = pd.DataFrame(row,index=[0])
            categories_max = pd.concat([categories_max, row],ignore_index=True)
    return categories_max

