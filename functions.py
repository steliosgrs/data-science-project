import pandas as pd
import numpy as np
from clean import cleaning
from dictonaries import countries, categories

# Testing purposes only
# df = pd.read_csv('countries_perGDP_80_2012_2020.csv')
# df = cleaning(df)

# Blueprint for max
def find_max(df:pd.DataFrame):
    total_max_year = pd.DataFrame()
    total_values = df.loc[df['Category'] == 'TOTAL']
    years = df.Year.unique()

    for year in range(years.__len__()):
        df_year = total_values.loc[total_values['Year'] == years[year]]
        max_idnex = df_year['Value'].astype(float).idxmax(axis=0)
        total_max = np.max(df_year.Value.values)
        countryCode = total_values.loc[max_idnex].Country
        country = countries[countryCode]
        row = {
                "Country":country,
                "Year":years[year],
                "Value":total_max
            }
        row = pd.DataFrame(row,index=[0])
        total_max_year = pd.concat([total_max_year, row],ignore_index=True)
    return total_max_year


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


# Testing purposes only
# print(find_max(df))
# print(find_category_max(df))