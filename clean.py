import pandas as pd
import numpy as np

# Cleaning data
def cleaning(df:pd.DataFrame):
    df = df[['cofog99','geo','TIME_PERIOD','OBS_VALUE','OBS_FLAG']]
    df = df.dropna(subset=['OBS_VALUE']) # Drop countries that not have OBS_VALUE
    # OBS_VALUE = GDP % or GDP millions

    df = df[['cofog99','geo','TIME_PERIOD','OBS_VALUE']]
    df.rename(
        columns={
            'cofog99':'Category',
            'geo':'Country',
            'TIME_PERIOD':'Year'
            ,'OBS_VALUE':'Value'
        },
        inplace=True)

    return df
# In current data 179 rows contain NaN type
