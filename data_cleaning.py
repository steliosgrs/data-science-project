def clean_data(data):

    columns_to_drop = [
        'DATAFLOW',
        'LAST UPDATE',
        'freq',
        'na_item',
        'unit',
        'sector',
        'OBS_FLAG'
    ]

    # renaming headers
    data.rename(columns={'cofog99': 'Category', 'geo': 'Country', 'TIME_PERIOD': 'Year',
                                'OBS_VALUE': 'Value'}, inplace=True)

    data.drop(columns_to_drop, inplace=True, axis=1)
    data.drop(data[data['Country'] == 'EU27_2020'].index, inplace=True)
    data.drop(data[data['Country'] == 'EA19'].index, inplace=True)

    return data


#   millions and percentages, for now hardcoded at index 23040
def split_df_into_mills_and_percs(data):

    df_in_millions = data.iloc[:23040, :]
    df_in_percentages = data.iloc[23040:, :]
    return df_in_millions, df_in_percentages




