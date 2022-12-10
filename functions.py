import pandas as pd
import numpy as np

countries = {
'BE': 'Belgium',
'BG': 'Bulgaria',
'CZ': 'Czechia',
'DK': 'Denmark',
'DE': 'Germany', 
'EE': 'Estonia',
'IE': 'Ireland',
'EL': 'Greece',
'ES': 'Spain',
'FR': 'France',
'HR': 'Croatia',
'IT': 'Italy',
'CY': 'Cyprus',
'LV': 'Latvia',
'LT': 'Lithuania',
'LU': 'Luxembourg',
'HU': 'Hungary',
'MT': 'Malta',
'NL': 'Netherlands',
'AT': 'Austria',
'PL': 'Poland',
'PT': 'Portugal',
'RO': 'Romania',
'SI': 'Slovenia',
'SK': 'Slovakia',
'FI': 'Finland',
'SE': 'Sweden',
'IS': 'Iceland',
'NO': 'Norway',
'CH': 'Switzerland' }

# Blueprint for max
def find_max(df:pd.DataFrame):
    total_values = df.loc[df['Category'] == 'TOTAL']
    # print(total_values)
    per = total_values['Percent']

    max_idnex = per.astype(float).idxmax(axis=0)
    total_max = np.max(total_values.Percent.values)
    # print(total_max)
    countryCode = total_values.loc[max_idnex].Country
    # print(countryCode)

    country = countries[countryCode]
    # print(df.iloc[max_idnex])

    return f" Total max {total_max} Country: {country}"

# print(find_max(df))

