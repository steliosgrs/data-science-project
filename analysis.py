import pandas as pd
from dictionaries import countries, categories


def find_max_index(data: pd.DataFrame) -> pd.DataFrame:
    #   returns the max index for each year
    max_index = data.groupby('Year')['Value'].idxmax()
    return max_index


#   finds maximum values in <parameter> category for each year 2012-2020
def find_max(data: pd.DataFrame, category: str) -> pd.DataFrame:
    if category == 'NOT TOTAL':
        data = data[data['Category'] != 'TOTAL']
    else:
        data = data[data['Category'] == category]

    max_index = find_max_index(data)
    return data.loc[max_index]


#   finds n_smallest elements of <country>, <year>.
def min_finder(country: str, year: int, dataset: pd.DataFrame, n_smallest: int) -> pd.DataFrame:
    data = dataset.loc[(dataset['Country'] == country) & (dataset['Year'] == year)]
    data2 = data.drop('Value', axis=1, inplace=False)
    output = pd.concat([data2, data], axis=1)
    output = output.nsmallest(n_smallest, 'Value')
    output = output.reset_index(drop=True)
    return output


def find_average_in_each_category(df: pd.DataFrame):
    new_df_categories = []
    new_df_values = []

    for key in categories:
        new_df_categories.append(categories[key])
        temp_df = df[df['Category'] == categories[key]]
        new_df_values.append(temp_df['Value'].mean())

    output = pd.DataFrame({
        'Category': new_df_categories,
        'Mean': new_df_values
    })

    return output.loc[output['Mean'].idxmin()]



