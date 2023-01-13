import pandas as pd
from dictionaries import countries, categories


def find_max_index(data: pd.DataFrame) -> pd.DataFrame:
    #   returns the max index for each year
    max_index = data.groupby('Year')['Value'].idxmax()
    return max_index


#   finds maximum values in <parameter> category for each year 2012-2020
def find_max(data: pd.DataFrame, category: str) -> pd.DataFrame:
    if category == 'NOT TOTAL':
        data = data[data['Category'] != 'Total']
    else:
        data = data[data['Category'] == category]

    max_index = find_max_index(data)
    return data.loc[max_index]


def find_n_min_in_country_and_year(country: str, year: int, dataset: pd.DataFrame, n_smallest: int) -> pd.DataFrame:

    # finds n_smallest rows by value of <country>, <year>.
    data = dataset.loc[(dataset['Country'] == country) & (dataset['Year'] == year)]
    data2 = data.drop('Value', axis=1, inplace=False)
    output = pd.concat([data2, data], axis=1)
    output = output.nsmallest(n_smallest, 'Value')
    output = output.reset_index(drop=True)
    return output


def find_min_average_in_all_categories(df: pd.DataFrame):
    """
    :param df
    :return: category with the smallest average on all cats, 2012-2020.
    """
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


def find_min_max_average_in_category(df: pd.DataFrame, category: str) -> dict \
        :

    """
    :param df
    :param category
    :return: dictionary in form: {'max_country: 99.0, min_country: 0.0001}
    """
    temp_df = df[df['Category'] == category]

    # max finding
    maximum_value = -69
    maximum_country = ''
    # min finding
    minimum_value = 100
    minimum_country = ''
    for key in countries:
        temp_country_df = temp_df[temp_df['Country'] == countries[key]]
        temp_country_average = temp_country_df['Value'].mean()

        if temp_country_average > maximum_value:  # max finding
            maximum_value = temp_country_average
            maximum_country = countries[key]

        if temp_country_average < minimum_value:  # min finding
            minimum_value = temp_country_average
            minimum_country = countries[key]
    return {minimum_country: minimum_value, maximum_country: maximum_value}


def find_average_value_for_each_year_and_category(df: pd.DataFrame) -> dict:
    """
    :param df: cleaned dataframe
    :return: dictionary with average value in each category and each year:
        {
    'Total 2012': 200424.36,
    'Total 2013': 202287.6033333333,
      ...}
    """
    dic = {}
    for key in categories:
        temp_category_df = df[df['Category'] == categories[key]]
        for year in range(2012, 2021):
            temp_category_and_year_df = temp_category_df[temp_category_df['Year'] == year]
            dic[f'{categories[key]} {year}'] = temp_category_and_year_df['Value'].mean()

    return dic
