from data_cleaning import *
from analysis import *
from dictionaries import rename_countries_and_cats

#   opening ang cleaning data
raw_df_in_millions = pd.read_csv(
    "D:\pycharmBackUp\eurostat_data_analysis_git\data-science-project\csv_in_millions.csv")  # NOQA
raw_countries_and_gdps = pd.read_csv(
    "D:\pycharmBackUp\eurostat_data_analysis_git\data-science-project\countries_and_GDPs.csv")  # NOQA
raw_df_in_percentages = pd.read_csv(  # already cleaned
    "D:\pycharmBackUp\eurostat_data_analysis_git\data-science-project\csv_in_stronger_percentages.csv") # NOQA

#   cleaning data and renaming categories and countries
#   ex.  DE -> Germany ... GF01 -> General public services etc.
datasets = [raw_df_in_millions, raw_countries_and_gdps]
for i in datasets:
    clean_data(i)
    rename_countries_and_cats(i)


def task_1(df):
    #   task 1, put 'NOT TOTAL' in 2nd arg to get all categories but total
    max_values = find_max(df, 'NOT TOTAL')

    # resetting indexes
    df = max_values.reset_index(drop=True)
    return df


def task_2(df):
    pass


if __name__ == '__main__':
    print(task_1(raw_df_in_millions))
    print(task_1(raw_df_in_percentages))

    task_2(raw_df_in_percentages)
