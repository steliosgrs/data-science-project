import pandas as pd


# Cleaning data by Steliosgrs
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


# Answering task1 where the highest expense per year is calculating and after that we calculate the category.

def task1percentage(dataset, year):
    result = dataset.loc[(dataset['Category'] == 'Total') & (dataset['Year'] == year)]
    output = result.loc[(result['Value'].idxmax())]
    result2 = dataset.loc[(dataset['Country'] == str(output[1])) & (dataset['Category'] != 'Total') & (dataset['Year'] == year)]
    output2 = result2.loc[(result2['Value'].idxmax())]
    return 'The country with the highest expenses for the year ' + str(year) + ' is ' + str(output[1]) + \
        ' spending ' + str(output[3]) + ' of their GDP. The category of COFOG that most of the money are spent is ' \
        + str(output2[0]) + ' with a percentage of ' + str(output2[3]) + ' of their GDP.'


def task1Actual(dataset, year):
    result = dataset.loc[(dataset['Category'] == 'Total') & (dataset['Year'] == year)]
    output = result.loc[(result['Value'].idxmax())]
    result2 = dataset.loc[(dataset['Country'] == str(output[1])) & (dataset['Category'] != 'Total') & (dataset['Year'] == year)]
    output2 = result2.loc[(result2['Value'].idxmax())]
    return 'The country with the highest expenses for the year ' + str(year) + ' is ' + str(output[1]) + \
        ' spending ' + str(output[3]) + ' in million of Euros. The COFOG category that most of the money are spent is ' \
        + str(output2[0]) + ' with a value of ' + str(output2[3]) + ' in million on Euros.'



def gdpFinder(Country, Year):
    import pandas as pd
    from dictionaries import countries

    # Reading csv using pandas csv read
    gdpActualPY = pd.read_csv("gdpActualPerYear.csv")

    # Removing unnecesary data from the dataset, keeping year, country and GDP in
    # millions euros
    gdpActualPY = gdpActualPY[['geo', 'TIME_PERIOD', 'OBS_VALUE']]

    # Renaming the columns
    gdpActualPY = gdpActualPY.rename(columns={gdpActualPY.columns[0]: 'Country'})
    gdpActualPY = gdpActualPY.rename(columns={gdpActualPY.columns[1]: 'Year'})
    gdpActualPY = gdpActualPY.rename(columns={gdpActualPY.columns[2]: 'GDP in Million €'})

    # Replacing countries names with their actual
    gdpActualPY['Country'] = gdpActualPY['Country'].replace(countries)

    value = (gdpActualPY.loc[(gdpActualPY['Country'] == str(Country)) & (gdpActualPY['Year'] == Year)])
    return (value['GDP in Million €'].item())

def gdpAccurate(dataset):
    s2 = pd.Series(dtype='float64')
    for i in range(0, len(dataset)):
        x = round(pd.Series([dataset.iloc[i, 3] / gdpFinder(str(dataset.iloc[i, 1]), dataset.iloc[i, 2]) * 100]), 3)
        s2 = pd.concat([s2, x], ignore_index=True)

    s2.to_csv('dfGDPAcc.csv', sep=',')

def task2Answer1(datasetAcc):
    temp1 = datasetAcc.groupby(['Category', 'Country']).agg(
        {'Value': 'mean'})  # Grouping dataset by country and category, extracting the mean values of all years
    result = temp1.loc[temp1['Value'] == float(temp1.loc[temp1['Value'] > 0].min())]
    return result

def task2Answer2(datasetAcc):
    dataset2 = datasetAcc.loc[datasetAcc['Category'] == 'R&D General public services', ['Value']]
    result2 = datasetAcc.loc[datasetAcc['Value'] == float(dataset2.max())]
    print(result2)