from dictionaries import rename_countries_and_cats
from data_cleaning import *
from analysis import *

raw_df_in_millions = pd.read_csv(
    "D:\pycharmBackUp\eurostat_data_analysis_git\data-science-project\csv_in_millions.csv"
)
raw_df_in_percentages = pd.read_csv(
    "D:\pycharmBackUp\eurostat_data_analysis_git\data-science-project\csv_in_percentages.csv"
)


def main(df):
    clean_data(df)
    # resetting indexes after dropping rows
    df = df.reset_index(drop=True)

    #   task 1, put 'NOT TOTAL' in 2nd arg to get all categories but total
    max_values = find_max(df, 'TOTAL')

    # resetting indexes, renaming headers

    df = max_values.reset_index(drop=True)
    df = rename_countries_and_cats(df)
    print(df)
    return ''


if __name__ == '__main__':
    main(raw_df_in_millions)
    main(raw_df_in_percentages)
