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


# df_in_percentages = drop_negatives(df_in_percentages)  # removing 0s and negatives from cleaned dataset
# with stronger percentages


def task_1(df: pd.DataFrame):
    # ignore total categories ex. Social Protection
    # df = drop_total_categories(df)

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


def task_3(df: pd.DataFrame) -> dict:
    del categories['TOTAL']  # we don't want Total category in results

    delta_dic = {}  # Δ<category> = Category average of 2020 - Category average of 2012
    dic = find_average_value_for_each_year_and_category(df)

    for key in categories:  # appending 2020-2012 average difference in new dictionary
        delta_dic[categories[key]] = dic[f'{categories[key]} {2020}'] - dic[f'{categories[key]} {2012}']

    # default values to be compared
    minimum: float = delta_dic[next(iter(delta_dic.items()))[0]]  # getting value of first dictionary pair to use
    # as minimum.
    maximum: float = delta_dic[next(iter(delta_dic.items()))[0]]  # similarly for maximum
    least_change: float = abs(delta_dic[next(iter(delta_dic.items()))[0]])  # similarly, for least changed founding
    # default strings to be replaced
    min_category = next(iter(delta_dic.items()))[0]  # getting key of first dictionary pair to use as country with
    # min and max category. we can't use empty string because if min or max category is the first pair, then we get
    # empty string in return.
    max_category = next(iter(delta_dic.items()))[0]
    least_change_category = next(iter(delta_dic.items()))[0]

    for key in delta_dic:  # finding min, max, closest to 0 in delta_dic
        if delta_dic[key] > maximum:  # max finding
            maximum = delta_dic[key]
            max_category = key
        if delta_dic[key] < minimum:  # min finding
            minimum = delta_dic[key]
            min_category = key
        delta_dic[key] = abs(delta_dic[key])  # smallest change finding
        if delta_dic[key] < least_change:
            least_change = delta_dic[key]
            least_change_category = key

    return {min_category: minimum,  max_category: maximum, least_change_category: least_change}


if __name__ == '__main__':
    #print(task_1(df_in_millions))
    #print(task_1(df_in_percentages))
    #print(task_2(df_in_percentages))

    print(task_3(df_in_millions))