# this function finds the N minimun of the dataset. 

def minFinder(dataset, Country, Year, N_smallest):
    data = dataset.loc[(dataset['Country'] == Country) & (dataset['Year'] == Year)]
    dataTemp = data['Percent'].div(gdpFinder(Country, Year))
    data2 = data.drop('Percent', axis=1, inplace=False)
    output = pd.concat([data2, dataTemp], axis=1)
    print(output)
    print(data)
    return output.nsmallest(N_smallest, 'Percent')
