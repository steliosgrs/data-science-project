import pandas as pd
from dictionaries import *


def find_max_index_in_mills(data):  # includes TOTAL

    max_index_in_mills = data.query("Country != 'EU27_2020' and Country != 'EA19'").groupby('Year')[
        'Expense Amount'].idxmax()

    return max_index_in_mills


def find_max_indexes_in_percs(data):
    max_index_in_percentages = data.groupby('Year')['Expense Amount'].idxmax()

    return max_index_in_percentages


def return_max_values_by_indexes(data, indexes):
    return data.loc[indexes]
