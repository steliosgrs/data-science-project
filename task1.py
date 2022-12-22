from cleaning import dfActual, dfGDP
from dictionaries import financialSectors

def task1(datasetGDP, datasetActual):

        # Find the country that spends max GDP per year
    group = datasetGDP.groupby(dfGDP.Category) # grouping by category
    tempdf = group.get_group('Total')   # creating a temporary df with only total GDP values

    categories = list(financialSectors.values())
    temp = []
    for i in range(2012, 2021):
        gdpEachYear = tempdf.loc[tempdf['Year'] == i, :] # Sorting the GDP per Year
        maxGDP = gdpEachYear.loc[gdpEachYear['Percent'].idxmax()] # finding the max GDP per year

        # Task 2.1 Finding the sector that the country that spends the max gdp spends most of their funding
        for x in range(1, 80):
            category = group.get_group(str(categories[x]))  # Sorting the dataset by category
            catPerCountry = category.loc[
                ((category['Country'] == str(maxGDP[1])) & (category['Year'] == i))]  # Filtering the max GDP country and Year
            y = catPerCountry['Percent'].item() # creating a temporary value to be saved
            temp.append(y) # adding the result to a list

        print( maxGDP[1], maxGDP[2], maxGDP[3], categories[temp.index(max(temp))], max(temp))
        temp = []  # reseting temp list to zero

    # Find the country that spends max GDP per year
    group = datasetActual.groupby(dfGDP.Category)  # grouping by category
    tempdf = group.get_group('Total')  # creating a temporary df with only total GDP values

    categories = list(financialSectors.values())
    temp = []
    for i in range(2012, 2021):
        gdpEachYear = tempdf.loc[tempdf['Year'] == i, :]  # Sorting the GDP per Year
        maxGDP = gdpEachYear.loc[gdpEachYear['Percent'].idxmax()]  # finding the max GDP per year

        # Task 2.1 Finding the sector that the country that spends the max gdp spends most of their funding
        for x in range(1, 80):
            category = group.get_group(str(categories[x]))  # Sorting the dataset by category
            catPerCountry = category.loc[
                ((category['Country'] == str(maxGDP[1])) & (
                            category['Year'] == i))]  # Filtering the max GDP country and Year
            y = catPerCountry['Percent'].item()  # creating a temporary value to be saved
            temp.append(y)  # adding the result to a list


        print(maxGDP[1], maxGDP[2], maxGDP[3], categories[temp.index(max(temp))], max(temp))
        temp = []  # reseting temp list to zero

task1(dfGDP, dfActual)
