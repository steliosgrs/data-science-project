import pandas as pd


def find_max_index_in_mills(data):  # includes TOTAL
    max_index_in_mills = data.query("geo != 'EU27_2020' and geo != 'EA19'").groupby('TIME_PERIOD')[
        'OBS_VALUE'].idxmax()

    return max_index_in_mills


def find_max_indexes_in_percs(data):
    max_index_in_percentages = data.groupby('TIME_PERIOD')['OBS_VALUE'].idxmax()

    return max_index_in_percentages


def return_max_values_by_indexes(data, indexes):
    return data.loc[indexes]