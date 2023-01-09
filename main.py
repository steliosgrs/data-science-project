import pandas as pd

from data_cleaning import *
from analysis import *
from dictionaries import rename_countries_and_cats, categories

#   opening ang cleaning data
df_in_millions = pd.read_csv(
    "D:\pycharmBackUp\eurostat_data_analysis_git\data-science-project\csv_in_millions.csv")  # NOQA
countries_and_gdps = pd.read_csv(
    "D:\pycharmBackUp\eurostat_data_analysis_git\data-science-project\countries_and_GDPs.csv")  # NOQA
df_in_percentages = pd.read_csv(  # already cleaned
    "D:\pycharmBackUp\eurostat_data_analysis_git\data-science-project\csv_in_stronger_percentages.csv")  # NOQA
total_eu_27_gdps = pd.read_csv(  # already cleaned
    "D:\pycharmBackUp\eurostat_data_analysis_git\data-science-project\eu_totals_2012_2020.csv")  # NOQA

#   cleaning data and renaming categories and countries
#   ex.  DE -> Germany ... GF01 -> General public services etc.
datasets = [countries_and_gdps, df_in_millions]
for i in datasets:
    clean_data(i, ignore_negatives_and_zeros=False, ignore_eu=False)
    rename_countries_and_cats(i)


def task_1(df: pd.DataFrame):
    #   task 1, put 'NOT TOTAL' in 2nd arg to get all categories but total
    max_values = find_max(df, 'NOT TOTAL')

    # resetting indexes
    df = max_values.reset_index(drop=True)
    df['Value'] = df['Value'].round(2)

    return df


def task_2(df: pd.DataFrame):
    return find_average_in_each_category(df)


if __name__ == '__main__':
    # print(task_1(raw_df_in_millions))
    # print(task_1(raw_df_in_percentages))

    print(task_2(df_in_percentages))
