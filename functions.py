import pandas as pd
from tabulate import tabulate

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


# Answering task1 where the highest expense per year is calculated and after that we determine the category.

def task1percentage(dataset, year1, year2):
    resultF = []
    for i in range(year1, (year2+1)):
        result = dataset.loc[(dataset['Category'] == 'Total') & (dataset['Year'] == i)]
        output = result.loc[(result['Value'].idxmax())]
        result2 = dataset.loc[
            (dataset['Country'] == str(output[1])) & (dataset['Category'] != 'Total') & (dataset['Year'] == i)]
        output2 = result2.loc[(result2['Value'].idxmax())]
        resultF.append([i, output[1], output[3], output2[0], output2[3]])
    print('On table 1 following, on the second collumn we can see the country that spends most of their GDP and on the third column'
          'we find the percentage of GDP spent, which complete the first part of the question. \nFollowing, we see the category that'
          ' the country spends most of their GDP and finally on column five we find the percentage spent on that Category, completing part 2 of the assigment. ')
    print(tabulate(resultF, headers=['Year', 'Country', 'GDP percentage spent', 'Category', 'GDP percentage spent on Category ']))



def task1Actual(dataset, year1, year2):
    resultF = []
    for i in range(year1, (year2 + 1)):
        result = dataset.loc[(dataset['Category'] == 'Total') & (dataset['Year'] == i)]
        output = result.loc[(result['Value'].idxmax())]
        result2 = dataset.loc[
            (dataset['Country'] == str(output[1])) & (dataset['Category'] != 'Total') & (dataset['Year'] == i)]
        output2 = result2.loc[(result2['Value'].idxmax())]
        resultF.append([i, output[1], output[3], output2[0], output2[3]])
    print('On the table following we can see the country which spends most of their GDP in actual values, measuring in million Euros. The collumns are '
          'set according to task 1.')
    print(tabulate(resultF, headers=['Year', 'Country', 'Million Euros', 'Category', 'Million Euros']))



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
    temp1 = datasetAcc.groupby(['Category', 'Country']).agg({'Value': 'mean'})  # Grouping dataset by country and category, extracting the mean values of all years
    result = temp1.loc[temp1['Value'] == float(temp1.loc[temp1['Value'] > 0].min())]
    return (result.reset_index())

def task2Answer2(datasetAcc):
    dataset2 = datasetAcc.loc[datasetAcc['Category'] == 'R&D General public services', ['Value']]
    result2 = datasetAcc.loc[datasetAcc['Value'] == float(dataset2.max())]
    return result2

def task3(dataset):
    workDataset = dataset.loc[(dataset['Category'] != 'Total')]
    workDataset = workDataset[workDataset['Country'].str.contains('Switzerland') == False]
    workDataset = workDataset.drop('Country', axis=1)
    result = workDataset.groupby(['Category', 'Year'])['Value'].sum().reset_index()
    result['diff'] = result.groupby('Category')['Value'].diff().fillna(0)
    maxReduction = result.loc[result['diff'].idxmin(), ['Category', 'diff']]

    maxIncreace = result.loc[result['diff'].idxmax(), ['Category', 'diff']]

    mostStable = result.groupby('Category')['Value'].std().idxmin()


    return maxReduction, maxIncreace, mostStable