from functions import task1percentage, task1Actual, task2Answer1, task2Answer2
from dataLoadingAndCleaning import dfGDP, dfActual, dfGDPAcc
if __name__ == '__main__':
    for i in range(2012, 2021):
        print(task1percentage(dfGDP, i))
    for i in range(2012, 2021):
        print(task1Actual(dfActual, i))

    print(task2Answer1(dfGDPAcc))
    print(task2Answer2(dfGDPAcc))




