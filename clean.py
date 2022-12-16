import pandas as pd
import numpy as np

# Cleaning data
def cleaning(df:pd.DataFrame):
    df = df[['cofog99','geo','TIME_PERIOD','OBS_VALUE','OBS_FLAG']]
    df = df.dropna(subset=['OBS_VALUE']) # Drop countries that not have OBS_VALUE
    # OBS_VALUE = GDP % or GDP millions

    # """
    # Do something with flag
    # """

    df = df[['cofog99','geo','TIME_PERIOD','OBS_VALUE']]
    df = df.rename(columns={df.columns[0]:'Category'})
    df = df.rename(columns={df.columns[1]:'Country'})
    df = df.rename(columns={df.columns[2]:'Year'})
    df = df.rename(columns={df.columns[3]:'Value'})
    return df
# In current data 179 rows contain NaN type
