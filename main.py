import pandas as pd
from dictionaries import countries, categories

raw_df = pd.read_csv(
    "D:\pycharmBackUp\eurostat_data_analysis_git\data-science-project\gov_10a_exp__custom_4083116_linear.csv"
)

columns_to_drop = [
    'DATAFLOW',
    'LAST UPDATE',
    'freq',
    'na_item',
    'unit',
    'sector',
    'OBS_FLAG'

]

#   cleaning data ###

raw_df.drop(columns_to_drop, inplace=True, axis=1)

#   splitting dataset in two
df_in_millions = raw_df.iloc[:23040, :]
df_in_percentages = raw_df.iloc[23040:, :]

max_values = df_in_percentages.query("cofog99 != 'TOTAL'").groupby('TIME_PERIOD').max()

print(max_values)


for i in range(2012, 2020 + 1):

    max_value = max_values.loc[i, 'OBS_VALUE']
    max_country = max_values.loc[i, 'geo']
    max_category = max_values.loc[i, 'cofog99']

    max_category = categories[max_category]
    max_country = countries[max_country]
    print(f' The highest GDP% expentage in {i} is {max_value}, in {max_category} category, by {max_country} country')
