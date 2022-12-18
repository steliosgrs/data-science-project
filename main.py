from dictionaries import *
from data_cleaning import *
from find_max_values_each_year import *

raw_df = pd.read_csv(
    "D:\pycharmBackUp\eurostat_data_analysis_git\data-science-project\gov_10a_exp__custom_4083116_linear.csv"
)


def main(raw_df):
    clean_data(raw_df)

    #   splitting dataset in two
    df_in_millions = split_df_into_mills_and_percs(raw_df)[0]
    df_in_percentages = split_df_into_mills_and_percs(raw_df)[1]

    max_index_in_mills = find_max_index_in_mills(df_in_millions)
    max_index_in_percentages = find_max_indexes_in_percs(df_in_percentages)

    # Use the index to select the rows with the maximum value from the original DataFrame

    max_values_in_mills = return_max_values_by_indexes(df_in_millions, max_index_in_mills)
    max_values_in_percentages = return_max_values_by_indexes(df_in_percentages, max_index_in_percentages)

    print(max_values_in_percentages)
    print(max_values_in_mills)


if __name__ == '__main__':
    main(raw_df)
