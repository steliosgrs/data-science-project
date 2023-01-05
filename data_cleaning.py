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



