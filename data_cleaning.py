import pandas as pd
from dictionaries import countries
import copy


def clean_data(data: pd.DataFrame, ignore_negatives_and_zeros=False, ignore_eu=True) -> pd.DataFrame:
    columns_to_drop = ['DATAFLOW', 'LAST UPDATE', 'freq', 'na_item', 'unit', 'sector', 'OBS_FLAG']

    # renaming headers
    data.rename(columns={'cofog99': 'Category', 'geo': 'Country', 'TIME_PERIOD': 'Year',
                         'OBS_VALUE': 'Value'}, inplace=True)

    try:  # countries_and_GDPs.csv has no "sector" header
        data.drop(columns_to_drop, inplace=True, axis=1)
    except KeyError:
        del columns_to_drop[5]
        data.drop(columns_to_drop, inplace=True, axis=1)

    #   ignoring negative values and EU medians (EU27 category) based on parameter.
    if ignore_negatives_and_zeros:
        data = data[data['Value'] > 0]
    if ignore_eu:
        data.drop(data[data['Country'] == 'EU27_2020'].index, inplace=True)
    data.drop(data[data['Country'] == 'EA19'].index, inplace=True)
    data = data.dropna(subset=['Value'])
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

def percentage(numerator, denominator) -> float:   # turning 2 values into a fraction
    return (numerator / denominator) * 100


def convert_percentages_to_true_decimals(df_to_be_converted: pd.DataFrame, conversion_based_df: pd.DataFrame)\
        -> pd.DataFrame:

    # df to be converted and conversion based df should be cleaned first using clean_data function.

    new_df_category = df_to_be_converted['Category']
    new_df_country = df_to_be_converted['Country']
    new_df_year = df_to_be_converted['Year']
    new_df_value = []

    for index, row in df_to_be_converted.iterrows():
        old_value = row[3]
        total_value = gdp_finder(row[1], row[2], conversion_based_df)
        new_df_value.append(percentage(old_value, total_value))

    new_df = pd.DataFrame({'Category': new_df_category,
                           'Country': new_df_country,
                           'Year': new_df_year,
                           'Value': new_df_value})
    # use new_df.to_csv('percentages.csv', index=False) to make the output a new csv file in current directory.
    return new_df
