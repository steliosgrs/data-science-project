from data_cleaning import *
from analysis import *
from dictionaries import rename_countries_and_cats, categories


#   opening ang cleaning data from path
df_in_millions = pd.read_csv(
    r"C:\Users\kalot\GitHub\data-science-project\csv_files\csv_in_millions.csv")  # NOQA
countries_and_gdps = pd.read_csv(
    r"C:\Users\kalot\GitHub\data-science-project\csv_files\countries_and_GDPs.csv")  # NOQA
df_in_percentages = pd.read_csv(  # already cleaned
    r"C:\Users\kalot\GitHub\data-science-project\csv_files\csv_in_stronger_percentages.csv")  # NOQA
total_eu_27_gdps = pd.read_csv(  # already cleaned
    r"C:\Users\kalot\GitHub\data-science-project\csv_files\eu_totals_2012_2020.csv")  # NOQA

#   cleaning data and renaming categories and countries
#   ex.  DE -> Germany ... GF01 -> General public services etc.

countries_and_gdps = clean_data(countries_and_gdps, ignore_negatives=False, ignore_zeros=False, ignore_eu=True)
countries_and_gdps = rename_countries_and_cats(countries_and_gdps)

df_in_millions = clean_data(df_in_millions, ignore_negatives=False, ignore_zeros=False, ignore_eu=True)
df_in_millions = rename_countries_and_cats(df_in_millions)

# uncomment to remove 0s and negatives from cleaned dataset with stronger percentages
# df_in_percentages = drop_negatives(df_in_percentages)


def task_1(df: pd.DataFrame):
    # ignore total categories ex. Social Protection, uncomment to ignore
    # df = drop_total_categories(df)

    # write 'NOT TOTAL' in 2nd arg to get all categories but total
    max_values = find_max_values_in_category_in_each_year(df, 'NOT TOTAL')

    # resetting indexes
    df = max_values.reset_index(drop=True)
    df['Value'] = df['Value'].round(2)

    return df


def task_2(df: pd.DataFrame):
    task_2_part_1 = find_min_sum_in_all_categories_all_years(df)
    task_2_part_1_output = task_2_part_1['Category'] + f" has the lowest average founding sum % at" \
                                                       f" {round(task_2_part_1['Sum of % GDP'], 4)}%. "

    task_2_part_2_3_cat_input = task_2_part_1['Category']

    df = drop_zeros(df)  # ignore zeros for part 2 ###########
    task_2_part_2_3_output = find_min_max_average_in_category_all_years(df, task_2_part_2_3_cat_input)

    for key in task_2_part_2_3_output:  # rounding dictionary values
        task_2_part_2_3_output[key] = round(task_2_part_2_3_output[key], 4)
    return task_2_part_1_output, task_2_part_2_3_output


def task_3(df: pd.DataFrame):
    del categories['TOTAL']  # we don't want Total category in results
    delta_dic = {}  # Δ<category> = Category average of 2020 - Category average of 2012
    dic = find_average_value_for_each_year_and_category(df)
    for key in categories:  # appending 2020-2012 averages difference in new dictionary
        delta_dic[categories[key]] = dic[f'{categories[key]} {2020}'] - dic[f'{categories[key]} {2012}']

    minimum = min(delta_dic.items(), key=lambda x: x[1])
    maximum = max(delta_dic.items(), key=lambda x: x[1])

    for key in delta_dic:  # converting dictionary to absolute values, so we can find least changed (value closest to 0)
        delta_dic[key] = abs(delta_dic[key])

    least_changed = min(delta_dic.items(), key=lambda x: x[1])

    return minimum, maximum, least_changed


if __name__ == '__main__':
    #print(task_1(df_in_millions))
    #print(task_1(df_in_percentages))

    #print(task_2(df_in_percentages))

    #print(task_3(df_in_percentages))
    print(df_in_millions)
