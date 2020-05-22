import financeplayground
import pickle
import datetime
import os

def updatesp():
    if not os.path.exists(
            'lastdownloadsp.dat'):  ##check if the user have download the data before, if not automatically download the data
        financeplayground.get_data_from_yahoo('y', 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies',
                                              'sp500tickers.pickle', 'stocks_dfs', 0)
        financeplayground.compile_data('sp500tickers.pickle', 'stocks_dfs')
        timeofcompletion = datetime.datetime.now()
        lastdownloadsp = open('lastdownloadsp.dat', 'wb')
        pickle.dump(str(timeofcompletion), lastdownloadsp)
        lastdownloadsp.close()
    else:
        lastdownloadsp = open('lastdownloadsp.dat',
                              'rb')  ##if the user have download the data before, print the last update date and ask the user if he want to redownload it
        value = pickle.load(lastdownloadsp)
        print("You have download the s&p 500 data at " + value + " do you want to redownload it?")
        choice = input('y/n')
        if choice == 'y':
            financeplayground.get_data_from_yahoo('y', 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies',
                                                  'sp500tickers.pickle', 'stocks_dfs', 0)
            financeplayground.compile_data('sp500tickers.pickle', 'stocks_dfs')
            timeofcompletion = datetime.datetime.now()
            lastdownloadsp = open('lastdownloadsp.dat', 'wb')
            pickle.dump(str(timeofcompletion), lastdownloadsp)
            lastdownloadsp.close()

def updatenasdaq():
    if not os.path.exists(
            'lastdownloadnasdaq.dat'):  ##check if the user have download the data before, if not automatically download the data
        financeplayground.get_data_from_yahoo('y', 'https://en.wikipedia.org/wiki/NASDAQ-100', 'nasdaqtickers.pickle',
                                              'stocks_nasdaq', 1)
        financeplayground.compile_data('nasdaqtickers.pickle', 'stocks_nasdaq')
        timeofcompletion = datetime.datetime.now()
        lastdownloadsp = open('lastdownloadsp.dat', 'wb')
        pickle.dump(str(timeofcompletion), lastdownloadsp)
        lastdownloadsp.close()
    else:
        lastdownloadsp = open('lastdownloadsp.dat',
                              'rb')  ##if the user have download the data before, print the last update date and ask the user if he want to redownload it
        value = pickle.load(lastdownloadsp)
        print("You have download the s&p 500 data at " + value + " do you want to redownload it?")
        choice = input('y/n')
        if choice == 'y':
            financeplayground.get_data_from_yahoo('y', 'https://en.wikipedia.org/wiki/NASDAQ-100',
                                                  'nasdaqtickers.pickle', 'stocks_nasdaq', 1)
            financeplayground.compile_data('nasdaqtickers.pickle', 'stocks_nasdaq')
            timeofcompletion = datetime.datetime.now()
            lastdownloadsp = open('lastdownloadsp.dat', 'wb')
            pickle.dump(str(timeofcompletion), lastdownloadsp)
            lastdownloadsp.close()

def updateall():
    financeplayground.get_data_from_yahoo('y', 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies',
                                          'sp500tickers.pickle', 'stocks_dfs', 0)
    financeplayground.compile_data('sp500tickers.pickle', 'stocks_dfs')
    timeofcompletion = datetime.datetime.now()
    lastdownloadsp = open('lastdownloadsp.dat', 'wb')
    pickle.dump(str(timeofcompletion), lastdownloadsp)
    lastdownloadsp.close()

    financeplayground.get_data_from_yahoo('y', 'https://en.wikipedia.org/wiki/NASDAQ-100', 'nasdaqtickers.pickle',
                                          'stocks_nasdaq', 1)
    financeplayground.compile_data('nasdaqtickers.pickle', 'stocks_nasdaq')
    timeofcompletion = datetime.datetime.now()
    lastdownloadsp = open('lastdownloadsp.dat', 'wb')
    pickle.dump(str(timeofcompletion), lastdownloadsp)
    lastdownloadsp.close()