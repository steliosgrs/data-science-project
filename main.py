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

max_index_in_mills = df_in_millions.query("geo != 'EU27_2020' and geo != 'EA19'").groupby('TIME_PERIOD')[
    'OBS_VALUE'].idxmax()
max_index_in_percentages = df_in_percentages.groupby('TIME_PERIOD')['OBS_VALUE'].idxmax()

# Use the index to select the rows with the maximum value from the original DataFrame

max_values_in_mills = df_in_millions.loc[max_index_in_mills]
max_values_in_percentages = df_in_percentages.loc[max_index_in_percentages]

# ??????????????????
# max_values_in_mills.reset_index()
# max_values_in_percentages.reset_index()
#
#
print(max_values_in_percentages)
print(max_values_in_mills)

