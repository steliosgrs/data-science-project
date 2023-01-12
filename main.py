from data_cleaning import *
from analysis import *
from dictionaries import rename_countries_and_cats, categories

#   opening ang cleaning data from path
df_in_millions = pd.read_csv(
    "D:\pycharmBackUp\eurostat_data_analysis_git\data-science-project\csv_files\csv_in_millions.csv")  # NOQA
countries_and_gdps = pd.read_csv(
    "D:\pycharmBackUp\eurostat_data_analysis_git\data-science-project\csv_files\countries_and_GDPs.csv")  # NOQA
df_in_percentages = pd.read_csv(  # already cleaned
    "D:\pycharmBackUp\eurostat_data_analysis_git\data-science-project\csv_files\csv_in_stronger_percentages.csv")  # NOQA
total_eu_27_gdps = pd.read_csv(  # already cleaned
    "D:\pycharmBackUp\eurostat_data_analysis_git\data-science-project\csv_files\eu_totals_2012_2020.csv")  # NOQA

#   cleaning data and renaming categories and countries
#   ex.  DE -> Germany ... GF01 -> General public services etc.
datasets = [countries_and_gdps, df_in_millions]
for i in datasets:
    clean_data(i, ignore_negatives=False, ignore_zeros=False, ignore_eu=True)
    rename_countries_and_cats(i)

df_in_percentages = drop_negatives(df_in_percentages)  # removing 0s and negatives from cleaned dataset
# with stronger percentages


def task_1(df: pd.DataFrame):
    # ignores total categories
    df = drop_total_categories(df)

    # write 'NOT TOTAL' in 2nd arg to get all categories but total
    max_values = find_max(df, 'NOT TOTAL')

    # resetting indexes
    df = max_values.reset_index(drop=True)
    df['Value'] = df['Value'].round(2)

    return df


def task_2(df: pd.DataFrame):
    task_2_part_1 = find_min_average_in_all_categories(df)
    task_2_part_1_output = task_2_part_1['Category'] + f" has the lowest average founding at" \
                                                       f" {round(task_2_part_1['Mean'], 4)}%. "

    task_2_part_2_3_cat_input = task_2_part_1['Category']

    df = drop_zeros(df)  # ignore zeros for part 2 ###########
    task_2_part_2_3_output = find_min_max_average_in_category(df, task_2_part_2_3_cat_input)

    for key in task_2_part_2_3_output:  # rounding dictionary values
        task_2_part_2_3_output[key] = round(task_2_part_2_3_output[key], 4)
    return task_2_part_1_output, task_2_part_2_3_output


def task_3(df: pd.DataFrame):
    pass


if __name__ == '__main__':
    #print(task_1(df_in_millions))
    #print(task_1(df_in_percentages))

    print(task_2(df_in_percentages))
