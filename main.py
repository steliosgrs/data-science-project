from dictionaries import rename_headers
from data_cleaning import *
from find_max_values_each_year import *

raw_df = pd.read_csv(
    "D:\pycharmBackUp\eurostat_data_analysis_git\data-science-project\gov_10a_exp__custom_4083116_linear.csv"
)


def main(raw_df):
    clean_data(raw_df)

    #   splitting dataset in two, !!!! to fix
    df_in_millions = split_df_into_mills_and_percs(raw_df)[0]
    df_in_percentages = split_df_into_mills_and_percs(raw_df)[1]

    #   task 1, put 'NOT TOTAL' in 2nd arg to get all categories but total
    max_values_in_mills = find_max(df_in_millions, 'NOT TOTAL')
    max_values_in_percentages = find_max(df_in_percentages, 'NOT TOTAL')

    # resetting indexes, renaming headers
    dfs = [x.reset_index(drop=True) for x in [max_values_in_percentages, max_values_in_mills]]
    dfs = [rename_headers(x) for x in dfs]

    print(dfs[0], '''\n\n''', dfs[1])
    return ''


if __name__ == '__main__':
    main(raw_df)
