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

