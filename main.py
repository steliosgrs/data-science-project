from functions import task1percentage, task1Actual, task2Answer1, task2Answer2, task3
from dataLoadingAndCleaning import dfGDP, dfActual, dfGDPAcc, dfGDPActual
if __name__ == '__main__':
    task1percentage(dfGDP, 2012, 2020)
    print('\n')
    task1Actual(dfActual, 2012, 2020)
    print('\n')
    task2Answer1(dfActual, dfGDPActual)
    task2Answer2(dfGDPAcc)
    task3(dfActual)












