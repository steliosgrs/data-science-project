import pandas as pd
import numpy as np

# Cleaning data
def cleaning(df:pd.DataFrame):
    df = df[['cofog99','geo','TIME_PERIOD','OBS_VALUE','OBS_FLAG']]
    # df = df[['geo','TIME_PERIOD','OBS_VALUE','OBS_FLAG']]

    
    # Drop category European Union
    df = df[df.geo !='EU27_2020']

    # Drop countries that not have OBS_VALUE
    df = df.dropna(subset=['OBS_VALUE']) 
    df = df[df.OBS_VALUE >= 0]
    # OBS_VALUE = GDP % or GDP millions

    df = df[['cofog99','geo','TIME_PERIOD','OBS_VALUE']]
    # df = df[['geo','TIME_PERIOD','OBS_VALUE']]
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

def cleaning2(df:pd.DataFrame):
    # df = df[['cofog99','geo','TIME_PERIOD','OBS_VALUE','OBS_FLAG']]
    df = df[['geo','TIME_PERIOD','OBS_VALUE','OBS_FLAG']]

    df = df.dropna(subset=['OBS_VALUE']) # Drop countries that not have OBS_VALUE
    df = df[df.OBS_VALUE >= 0]
    # OBS_VALUE = GDP % or GDP millions

    # df = df[['cofog99','geo','TIME_PERIOD','OBS_VALUE']]
    df = df[['geo','TIME_PERIOD','OBS_VALUE']]
    df.rename(
        columns={
            # 'cofog99':'Category',
            'geo':'Country',
            'TIME_PERIOD':'Year'
            ,'OBS_VALUE':'Value'
        },
        inplace=True)

    return df

def cleaningT(df:pd.DataFrame):
    df = df[['geo','TIME_PERIOD','OBS_VALUE','OBS_FLAG']]
    # df = df[['geo','TIME_PERIOD','OBS_VALUE','OBS_FLAG']]
    df = df[df.geo != 'CH']
    df = df.dropna(subset=['OBS_VALUE']) # Drop countries that not have OBS_VALUE
    df = df[df.OBS_VALUE >= 0]
    # OBS_VALUE = GDP % or GDP millions

    df = df[['geo','TIME_PERIOD','OBS_VALUE']]
    # df = df[['geo','TIME_PERIOD','OBS_VALUE']]
    df.rename(
        columns={
            'geo':'Country',
            'TIME_PERIOD':'Year'
            ,'OBS_VALUE':'Value'
        },
        inplace=True)

    return df

def cleaning_task2(df:pd.DataFrame):
    df = df[['cofog99','geo','TIME_PERIOD','OBS_VALUE','OBS_FLAG']]
    # df = df[['geo','TIME_PERIOD','OBS_VALUE','OBS_FLAG']]

    
    # Drop category European Union
    # df = df[df.geo !='EU27_2020']

    # Drop countries that not have OBS_VALUE
    df = df.dropna(subset=['OBS_VALUE']) 
    df = df[df.OBS_VALUE >= 0]
    # OBS_VALUE = GDP % or GDP millions

    df = df[['cofog99','geo','TIME_PERIOD','OBS_VALUE']]
    # df = df[['geo','TIME_PERIOD','OBS_VALUE']]
    df.rename(
        columns={
            'cofog99':'Category',
            'geo':'Country',
            'TIME_PERIOD':'Year'
            ,'OBS_VALUE':'Value'
        },
        inplace=True)

    return df