import pandas as pd
from dictionaries import countries
import copy


def clean_data(data: pd.DataFrame, ignore_negatives=False, ignore_zeros=False, ignore_eu=True) -> pd.DataFrame:
    """
    :param data: raw .csv file, source https://ec.europa.eu/eurostat/databrowser/view/
    GOV_10A_EXP__custom_4037043/default/table?lang=en
    :param ignore_negatives: ignores negative numbers in 'OBS_VALUE' column.
    :param ignore_zeros: ignores 0 values in 'OBS_VALUE' column
    :param ignore_eu: ignores EU_27 country entries (EU27 totals)
    :return: pandas dataframe structured as:

       Category                 Country  Year  Value
    0  General public services  Austria  2012  7.2
    1  General public services  Austria  2013  7.2
    2  General public services  Austria  2014  6.8
    3  General public services  Austria  2015  6.7
    4  General public services  Austria  2016  6.4
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
    if ignore_negatives:
        data = drop_negatives(data)
    if ignore_zeros:
        data = drop_zeros(data)
    if ignore_eu:
        data.drop(data[data['Country'] == 'EU27_2020'].index, inplace=True)
    data.drop(data[data['Country'] == 'EA19'].index, inplace=True)
    data = data.dropna(subset=['Value'])
    data = data.reset_index(drop=True)

    return data


def drop_negatives(df: pd.DataFrame):
    return df[df['Value'] >= 0]


def drop_zeros(df: pd.DataFrame):
    return df[df['Value'] > 0]


def drop_total_categories(df: pd.DataFrame):
    """

    :param df:
    :return: dataframe without rows that have category equal to categories in list. These categories are the sum
    of other sub-categories.
    """
    total_categories_to_be_dropped = ['General public services', 'Defence', 'Public order and safety',
                                      'Economic affairs', 'Environmental protection', 'Housing and community amenities',
                                      'Health', 'Recreation, culture and religion', 'Education', 'Social protection']
    for category in total_categories_to_be_dropped:
        df.drop(df[df['Category'] == category].index, inplace=True)
    return df


def gdp_finder(country, year: int, csv) -> float:
    """
    where csv is countries_and_GDPs.csv cleaned
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

    :param df_to_be_converted: a csv with millions for each category (cleaned)
    :param conversion_based_df: csv with each country's GDP (cleaned)
    :return: new dataframe with more accurate percentages dividing first gdp value with GDP.
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
