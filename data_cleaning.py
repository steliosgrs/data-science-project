import pandas as pd
from dictionaries import countries
import copy


def clean_data(data):
    columns_to_drop = ['DATAFLOW', 'LAST UPDATE', 'freq', 'na_item', 'unit', 'sector', 'OBS_FLAG']

    # renaming headers
    data.rename(columns={'cofog99': 'Category', 'geo': 'Country', 'TIME_PERIOD': 'Year',
                         'OBS_VALUE': 'Value'}, inplace=True)

    try:  # countries_and_GDPs.csv has no "sector" header
        data.drop(columns_to_drop, inplace=True, axis=1)
    except KeyError:
        del columns_to_drop[5]
        data.drop(columns_to_drop, inplace=True, axis=1)

    data.drop(data[data['Country'] == 'EU27_2020'].index, inplace=True)
    data.drop(data[data['Country'] == 'EA19'].index, inplace=True)
    data = data.reset_index(drop=True)

    return data


def gdp_finder(country, year: int, csv) -> float:
    gdp_actual = copy.deepcopy(csv)

    # finding the requested GDP
    value = gdp_actual.loc[(gdp_actual["Country"] == country) & (gdp_actual["Year"] == year), ["Value"]]
    return value['Value'].item()


#   converting 1 decimal percentages from original CSV to more accurate percentages using GDP's CSV
#   parameters: a csv with millions for each category, each country's GDP
#   returns new dataframe with more accurate percentages dividing first gdp value with GDP.

def percentage(old_v, new_v):
    return (old_v / new_v) * 100


def convert_percentages_to_true_decimals(df_to_be_converted, conversion_based_df):
    new_df_category = df_to_be_converted['Category']
    new_df_country = df_to_be_converted['Country']
    new_df_year = df_to_be_converted['Year']
    new_df_value = []

    for index, row in df_to_be_converted.iterrows():
        oldv = row[3]
        total_v = gdp_finder(row[1], row[2], conversion_based_df)
        new_df_value.append(percentage(oldv, total_v))

    new_df = pd.DataFrame({'Category': new_df_category,
                           'Country': new_df_country,
                           'Year': new_df_year,
                           'Value': new_df_value})
    # use new_df.to_csv('percentages.csv', index=False) to make the output a new csv file in current directory.
    return new_df
