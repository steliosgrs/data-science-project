import pandas as pd
from data_cleaning import gdp_finder


def find_max_index(data, category):
    #   returns the max index for each year
    max_index = data.groupby('Year')['Value'].idxmax()
    return max_index


def find_max(data, category):
    if category == 'NOT TOTAL':
        data = data[data['Category'] != 'TOTAL']
    else:
        data = data[data['Category'] == category]

    max_index = find_max_index(data, category)
    return data.loc[max_index]


def min_finder(country, year, dataset, n_smallest):
    # TRIED TO RUN MIN FINDER ON MILLIONS DATSET, CHECK KEYS FOR DEBUGGING
    data = dataset.loc[(dataset['Country'] == country) & (dataset['Year'] == year)]
    dataTemp = round((data['Value'].div(gdp_finder(country, year, dataset))*100), 2)
    data2 = data.drop('Value', axis=1, inplace=False)
    output = pd.concat([data2, dataTemp], axis=1)
    return output.nsmallest(n_smallest, 'Value')
