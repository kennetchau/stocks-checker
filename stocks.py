"""Codes that allow me to modify my spreadsheet(reworking) as well as looking up the new stock price"""
import warnings
warnings.filterwarnings("ignore",category=FutureWarning)
import yfinance as yf   # downloading data from yahoo finance
import generalfunction as gf
import glob, os
import pandas as pd
from pandas_datareader import data as pdr
import mplfinance as mpf
import financeplayground
import datetime as dt
import pickle
import update


#theFile = openpyxl.load_workbook("stock portfolio.xlsx")
#allSheetNames = theFile.sheetnames
#currentSheet = 0


#for sheet in allSheetNames:
 #   if sheet == "stock portfolio":
  #      currentSheet = theFile[sheet]


#def find_specific_cell(str):
 #   for row in range(1, currentSheet.max_row + 1):
  #      for column in "ABCDE":
   #         cell_name = "{}{}".format(column, row)
    #        if currentSheet[cell_name].value == str:
     #           return cell_name
    #return 0

#def get_column_letter(specificCellLetter):
 #   if specificCellLetter == 0:
  #      return 0
   # letter = specificCellLetter[0:-1]
    #return letter

#def get_role_value(specificCellLetter):
 #   if specificCellLetter == 0:
  #      return 0
   # number = specificCellLetter[1:2]
    #return number

#def get_all_values_by_cell_letter(letter):
 #   for row in range(1, currentSheet.max_row + 1):
  #      for column in letter:
   #         cell_name = "{}{}".format(column, row)
    #        #print(cell_name)
     #       print("cell position {} has value {}".format(cell_name, currentSheet[cell_name].value))


def main():
    yf.pdr_override()
    sp500 = pdr.get_data_yahoo('^GSPC',period = ('30d'))
    print(sp500.tail())
    mpf.plot(sp500,type='line',title='S&P 500')
    action = 1
    while action != 0:
        print("What do you want to do today\n")
        action = gf.getnumber("\npress 1 to search current and historic stock price \npress 2 to download data about a stock \npress 3 to view downloaded data \npress 4 to show the index\npress 5 to get tickers from an index \npress 6 to get all s&p 500 or nasdaq price data (WARNING: THIS WILL TAKE A WHILE)\npress 7 to show the correlation heatmap between stock (WARNING: THIS WILL TAKE A WHILE) \npress 9 to use the calculator \npress 0 to quit ")
        #if action == 1:
            #Whattofind = input("What you want to find? ")
            #specificCellletter = (find_specific_cell(Whattofind))
            #value = get_role_value(specificCellletter)
            #newvalue = input("What the new value? ")
            #currentSheet['C' + str(value)] = float(newvalue)
            #theFile.save('stock portfolio.xlsx')
            #print("The stock " + Whattofind + " value has changed to " +newvalue)
        #elif action == 2:
            #Whattofind = input("What you want to find? ")
            #specificCellletter = (find_specific_cell(Whattofind))
            #value = get_role_value(specificCellletter)
            #price = currentSheet['C' + str(value)].value
            #print("\nThe value of the stock "+ Whattofind +" is "+ str(price) +"\n")

        if action == 1:     #A function to show stock price by asking the user to input the stock symbol, also provide the user the ability to choose the time period
            Whattofind = input("Which stock price are you interested? ")
            whattofindprice = yf.Ticker(Whattofind)
            pricehistory = whattofindprice.history(period="10d")
            print("The price of " + Whattofind + " is\n" + str(pricehistory))
            try:
                mpf.plot(pricehistory, type='candle',volume=True,title=str(Whattofind),ylabel='OHLC Candles',ylabel_lower='Volume',style='charles')
            except:
                print()
            option = input("Would you want more data? y/n")
            while option == "y":
                period = gf.getnumber("How many days of data do you want? ")
                pricehistory = whattofindprice.history(period=(str(period) +"d"))
                print("The price of " + Whattofind + " is\n" + str(pricehistory))
                mpf.plot(pricehistory,type='candle',volume=True,title=str(Whattofind),ylabel='OHLC Candles',ylabel_lower='Volume',style='charles')
                option = input("Would you want more data? y/n")


        elif action == 2:    #A function allows the user to download stock data by asking the user to input the stock symbol and the start and end date then save the data into a csv file
            if not os.path.exists('history/downloadhistory.dat'):
                Whattofind = input(
                    "Which stock/stocks price are you interested? (You can enter one or more stocks just separate the stock symbol with space)")
                startdate = input("Startdate (format: YYYY/MM/DD): ")
                enddate = input("Enddate (format: YYYY/MM/DD): ")
                lastdownload = open('history/downloadhistory.dat', 'wb')
                pickle.dump(str(Whattofind), lastdownload)
                pickle.dump(startdate,lastdownload)
                pickle.dump(enddate,lastdownload)
                lastdownload.close()
            else:
                lastdownload = open('history/downloadhistory.dat','rb')
                history = pickle.load(lastdownload)
                hisstart = pickle.load(lastdownload)
                hisend = pickle.load(lastdownload)
                print("You have previously download data of '{}' from {} to {}, would you like to download it again?".format(history,hisstart, hisend))
                choice = input("y/n\n")
                if choice =='y':
                    question = input("Would you like to download the same period? if yes please press 1, if you would like to update your data to today press 2, if you would like to download the data of specific time period press enter.")
                    Whattofind = history
                    if question == '1':
                        startdate = hisstart
                        enddate = hisend
                    elif question == "2":
                        startdate = hisstart
                        enddate = dt.date.today()
                        enddate = enddate + dt.timedelta(days=1)
                        lastdownload = open('history/downloadhistory.dat', 'wb')
                        pickle.dump(str(Whattofind), lastdownload)
                        pickle.dump(startdate, lastdownload)
                        pickle.dump(enddate, lastdownload)
                        lastdownload.close()
                    else:
                        startdate = input("Startdate (format: YYYY/MM/DD): ")
                        enddate = input("Enddate (format: YYYY/MM/DD): ")
                        lastdownload = open('history/downloadhistory.dat','wb')
                        pickle.dump(str(Whattofind), lastdownload)
                        pickle.dump(startdate, lastdownload)
                        pickle.dump(enddate, lastdownload)
                        lastdownload.close()
                else:
                    Whattofind = input(
                        "Which stock/stocks price are you interested? (You can enter one or more stocks just separate the stock symbol with space)")
                    startdate = input("Startdate (format: YYYY/MM/DD): ")
                    enddate = input("Enddate (format: YYYY/MM/DD): ")
                    lastdownload = open('history/downloadhistory.dat', 'wb')
                    pickle.dump(str(Whattofind), lastdownload)
                    pickle.dump(startdate, lastdownload)
                    pickle.dump(enddate, lastdownload)
                    lastdownload.close()
            startdate = gf.changestringtodate(startdate)
            try:
                enddate = gf.changestringtodate(enddate)
                enddate = enddate + dt.timedelta(days=1)
            except TypeError:
                pass
            data = yf.download(str(Whattofind), start=startdate, end=enddate).to_csv(str(Whattofind) + ".csv")
            print("The data have been saved in the directory "+str(os.getcwd()))

        elif action == 3:   #A function to allow user to open csv files
            print("Which csv do you want to open? (Please type the full name): ")
            currentpathnote = os.getcwd()
            os.chdir(str(currentpathnote))
            for file in glob.glob("*.csv"):
                print(file)
            filename = input("")
            try:
                df = pd.read_csv(filename, header =0, index_col = 'Date', parse_dates=True)
                print(df)
            except ValueError:
                df = pd.read_csv(filename, skiprows= 1)
                print(df)

        elif action == 4: #A function allows the user to search up s&p 500 index history
            choice = 0
            stockidx = financeplayground.get_index()
            sp500 = pdr.get_data_yahoo(stockidx, period=('60d'))
            print(sp500.tail())
            mpf.plot(sp500,type='line',title=stockidx)
            choice  = gf.getnumber("What would you like to do?\nPress 1 to show the candle plot\nPress 2 to download data\n")
            if choice == 1:
                mpf.plot(sp500,type='candle',title = stockidx , style = 'charles')
            if choice == 2:
                lastdownload = open('history/downloadhistory.dat', 'rb')
                history = pickle.load(lastdownload)
                hisstart = pickle.load(lastdownload)
                hisend = pickle.load(lastdownload)
                startdate = gf.changestringtodate(hisstart)
                enddate = gf.changestringtodate(hisend)
                data = yf.download(str(stockidx), start=startdate, end=enddate).to_csv(str(stockidx) + ".csv")

        elif action == 5: #get tickers
            action = gf.getnumber("Which ticket do you want to get?\ns&p press 1\nnasdaq press 2")
            if action == 1:
                financeplayground.save_tickers('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies','sp500tickers.pickle',0)
                with open("ticker/sp500tickers.pickle", "rb") as f:
                    tickers = pickle.load(f)
                    print(tickers)
            if action == 2:
                financeplayground.save_tickers('https://en.wikipedia.org/wiki/NASDAQ-100','nasdaqtickers.pickle',1)
                with open("ticker/nasdaqtickers.pickle", "rb") as f:
                    tickers = pickle.load(f)
                    print(tickers)


        elif action == 6: #download s&p 500 data and automatically compile them into a separate file contain all the adjusted close
            action = gf.getnumber("Which data do you wanna get?\ns&p press 1\nnasdaq press 2\nget all press 3 ")
            if action == 1:
                update.updatesp()
            if action == 2:
                update.updatenasdaq()
            if action == 3:
                update.updateall()


        elif action == 7:
            action = gf.getnumber('s&p 500 press 1\nnasdaq press 2 ')
            if action == 1:
                if not os.path.exists('joined_closed/sp500tickers.pickle_joined_closed.csv'):
                    financeplayground.compile_data('sp500tickers.pickle','stocks_dfs')
                financeplayground.visualize_data('sp500tickers.pickle_joined_closed.csv')
            if action == 2:
                if not os.path.exists('joined_closed/nasdaqtickers.pickle_joined_closed.csv'):
                    financeplayground.compile_data('nasdaqtickers.pickle','stocks_nasdaq')
                financeplayground.visualize_data('nasdaqtickers.pickle_joined_closed.csv')

        #elif action == 8: ## Run a linear regression between a chosen stock and a chosen index
         #   Whattofind = input("Which stock price are you interested? ")
          #  whattofindprice = yf.Ticker(Whattofind)
           # pricehistory = whattofindprice.history(period="5y")
            #stockid = financeplayground.get_index()
            #print(stockid)
            #indexs = pdr.get_data_yahoo(stockid, period=('5y'))
            #pricehistory.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1, inplace=True)
            #indexs.drop(['Open','High','Low','Close','Volume'],1,inplace =True)
            #print(stockid)
            #print(pricehistory)
            #df = pd.DataFrame(pricehistory,stockid,index = 'Date')
            #print(df)




        elif action == 9: #A function that allow the user to use the calculator
            calc = ""
            while calc != 'exit':
                calc = input("Type Calculation (type exit to exit): \n")
                print("Answer: " + str(eval(calc)))


#main()


