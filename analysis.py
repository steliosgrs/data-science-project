import pandas as pd
from dictionaries import *


def find_max_index(data, category):
    #   returns the max index for each year
    max_index = data.groupby('Year')['Value'].idxmax()
    return max_index


def return_max_values_by_indexes(data, indexes):
    return data.loc[indexes]


def find_max(data, category):
    if category == 'NOT TOTAL':
        data = data[data['Category'] != 'TOTAL']
    else:
        data = data[data['Category'] == category]

    max_index = find_max_index(data, category)
    return return_max_values_by_indexes(data, max_index)

