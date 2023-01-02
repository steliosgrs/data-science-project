def gdpFinder(Country, Year):
    import pandas as pd

    from dictionaries import countries
    
    # Reading csv using pandas csv read
    gdpActual = pd.read_csv("gdpActualPerYear.csv")

    # Removing unnecesary data from the dataset, keeping year, country and GDP in
    # millions euros
    gdpActual = gdpActual[['geo', 'TIME_PERIOD', 'OBS_VALUE']]

    # Renaming the columns
    gdpActual = gdpActual.rename(columns={gdpActual.columns[0]: 'Country'})
    gdpActual = gdpActual.rename(columns={gdpActual.columns[1]: 'Year'})
    gdpActual = gdpActual.rename(columns={gdpActual.columns[2]: 'GDP in Million €'})

    # Replacing countries names with their actual names
    gdpActual['Country'] = gdpActual['Country'].replace(countries)
    
    #finding the requested GDP
    value = (gdpActual.loc[(gdpActual['Country'] == Country) & (gdpActual['Year'] == Year)])
    return (value['GDP in Million €'].item())
