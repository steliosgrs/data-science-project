from functions import task1percentage, task1Actual, task2Answer1, task3
from dataLoadingAndCleaning import dfGDP, dfActual, dfGDPAcc, dfGDPActual
if __name__ == '__main__':
    task1percentage(dfGDP, 2012, 2020)
    print('\n')
    task1Actual(dfActual, 2012, 2020)
    print('\n')
    print('Task 2')
    task2Answer1(dfActual, dfGDPActual)
    print('\n')
    print('Task 3')
    task3(dfActual)













