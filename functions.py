import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt


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

def cleaningGDPActualValues(dataframe):
    df = dataframe.drop(['DATAFLOW', 'LAST UPDATE', 'freq', 'unit', 'OBS_FLAG', 'na_item'], axis=1)
    df.rename(columns={'geo': 'Country', 'TIME_PERIOD': 'Year', 'OBS_VALUE': 'Value'}, inplace=True)
    return df

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


# Task 1 Answering part 2. Which country spends most of their GDP and in which category of COFOG
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


# gdpFinder finds the actual gdp Value for a specific country and year, using the csv provided
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

# gdpAccurate calculates the GDP for all countries with more precision than the data provided by Eurostat and saves it
# to the working directory. GdpFinder is utilised here. This should be used only once, due to the high cpu cost.
def gdpAccurate(dataset):
    s2 = pd.Series(dtype='float64')
    for i in range(0, len(dataset)):
        x = round(pd.Series([dataset.iloc[i, 3] / gdpFinder(str(dataset.iloc[i, 1]), dataset.iloc[i, 2]) * 100]), 3)
        s2 = pd.concat([s2, x], ignore_index=True)

    s2.to_csv('dfGDPAcc.csv', sep=',')


# Answering task 2 part 1.
def task2Answer1(datasetGDPActual, DatasetGDPperYear):
    pd.set_option('display.precision', 15)
    dfworking = datasetGDPActual.groupby(['Category'])['Value'].sum().reset_index()
    result = dfworking.loc[(dfworking['Value']).idxmin()]
    tenYearGDP = DatasetGDPperYear['Value'].sum()  # Calculating the 10year GDP
    tenYearCategoryValue = datasetGDPActual.groupby(['Category', 'Country'])[
        'Value'].mean().reset_index()  # Calculating the ten year average value for each category and country
    tenYearCategoryValue['Value'] = tenYearCategoryValue[
                                        'Value'] / tenYearGDP  # CAlculating the percentage according to the 10 year EU GDP
    output1 = tenYearCategoryValue.loc[(tenYearCategoryValue['Category'] == str(result['Category']))]  # Finding the category with the smallest expence on the calculated dataframe
    lowest = output1.loc[output1['Value'].idxmin()]  # Finding the country who spends the least money on this category
    highest = output1.loc[output1['Value'].idxmax()]  # finding the country that spends most money on this category

    print('The category with the lowest GDP expense is ' + str(result['Category']) + '.')
    print('The country with the lowest expense spends ' + str(lowest['Value']) + ' of their GDP in this category')
    print('The country with the highest expense spends ' + str(highest['Value']) + ' of their GDP in this category')


# Task 3
def task3(dataset):
    workDataset = dataset.loc[(dataset['Category'] != 'Total')]
    workDataset = workDataset[workDataset['Country'].str.contains('Switzerland') == False]
    workDataset = workDataset.drop('Country', axis=1)
    result = workDataset.groupby(['Category', 'Year'])['Value'].sum().reset_index()
    result['diff'] = result.groupby('Category')['Value'].diff().fillna(0)
    maxReduction = result.loc[result['diff'].idxmin(), ['Category', 'diff']]

    maxIncreace = result.loc[result['diff'].idxmax(), ['Category', 'diff']]
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    mostStable = result.groupby('Category')['Value'].std().idxmin()
    visualisation = workDataset.groupby(['Category', 'Year'])['Value'].sum().reset_index()
    visualisation = visualisation.loc[visualisation['Category'] == 'Public debt transactions']
    print('The category with the biggest funding reduction is ' + str(maxReduction['Category']) + '.')
    print('The category with the largest funding increase is ' + str(maxIncreace['Category']) + '.')
    print('The most stable category in terms of funding is ' + str(mostStable) + '.')
    # Graphing

    x = visualisation['Year']
    y = visualisation['Value']
    plt.plot(x, y, marker = '<')
    plt.ylabel('Million Euros')
    plt.xlabel('Year')
    plt.title('Reduction of funding in Public debt transactions ')
    plt.show()




    return maxReduction, maxIncreace, mostStable