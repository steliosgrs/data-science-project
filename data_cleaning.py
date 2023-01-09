import pandas as pd
from dictionaries import countries
import copy


def clean_data(data: pd.DataFrame, ignore_negatives_and_zeros=False, ignore_eu=True) -> pd.DataFrame:
    """
    :param data: raw .csv file, source https://ec.europa.eu/eurostat/databrowser/view/
    GOV_10A_EXP__custom_4037043/default/table?lang=en
    :param ignore_negatives_and_zeros: ignores negative numbers in 'OBS_VALUE' column.
    :param ignore_eu: ignores EU_27 country entries (EU27 totals)
    :return: pandas dataframe structured as:

    Category  Country  Year     Value
    0  General public services  Austria  2012  7.261159
    1  General public services  Austria  2013  7.210486
    2  General public services  Austria  2014  6.825444
    3  General public services  Austria  2015  6.793782
    4  General public services  Austria  2016  6.462216
    ....
    """

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
    """
    where csv is countries_and_GDPs.csv cleaned
    ########################################
    """
    gdp_actual = copy.deepcopy(csv)

    # finding the requested GDP
    value = gdp_actual.loc[(gdp_actual["Country"] == country) & (gdp_actual["Year"] == year), ["Value"]]
    return value['Value'].item()


def percentage(numerator, denominator) -> float:
    # turning 2 values into a fraction
    return (numerator / denominator) * 100


def convert_percentages_to_true_decimals(df_to_be_converted: pd.DataFrame, conversion_based_df: pd.DataFrame)\
        -> pd.DataFrame:
    """
    converting 1 decimal percentages from original CSV to more accurate percentages using GDP's CSV

    :param df_to_be_converted: a csv with millions for each category
    :param conversion_based_df: each country's GDP
    :return: new dataframe with more accurate percentages dividing first gdp value with GDP.
    df to be converted and conversion based df should be cleaned first using clean_data function.
    """

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
