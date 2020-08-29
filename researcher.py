import yfinance as yf
import generalfunction as gf



def research():
    Whattodo = input("Which stock are you interested? ")
    try:
        stock = yf.Ticker(Whattodo)
        information = stock.info
        print('Here is some basic info of the stock {}:'.format(information.get('longName')))
        print('Symbol: {}'.format(information.get('symbol')))
        print('industry: {}'.format(information.get('industry')))
        print('country: {}'.format(information.get('country')))
        print('state: {}'.format(information.get('state')))
        print('city: {}'.format(information.get('city')))
        print('phone:{}'.format(information.get('phone')))
        print('website:{}'.format(information.get('website')))
        print('address:{}'.format(information.get('address1')))
        print('market: {}'.format(information.get('market')))
        print("All data are from Yahoo finance\n")
        q1 = 9
        while q1 != 0:
            q1 = gf.getnumber("Press 1 if you want the open and close prices of the company \nPress 2 if you want the long summary of the company \nPress 3 to show everything\nPress 0 to quit \n")
            if q1 == 1:
                print('Open: {}'.format(information.get('open')))
                print('High: {}'.format(information.get('regularMarketDayHigh')))
                print('Low: {}'.format(information.get('regularMarketDayLow')))
                print('Previous Close: {}'.format(information.get('regularMarketPreviousClose')))
                print('50days average: {}'.format(information.get('fiftyDayAverage')))
                print('52wk high: {}'.format(information.get('fiftyTwoWeekHigh')))
                print('52wk low: {}'.format(information.get('fiftyTwoWeekLow')))
                print('52wk change: {}'.format(information.get('52WeekChange')))
                print('forwardPE: {}'.format(information.get('forwardPE')))
                print('Beta: {}'.format(information.get('beta')))
                print("BookValue: {}".format(information.get('bookValue')))
                print('Regular Market Volume: {}'.format(information.get('regularMarketVolume')))
                print('Average Volume:{}\n'.format(information.get('aveageVolume')))
            elif q1 == 2:
              print('Long business summary: {}\n'.format(information.get('longBusinessSummary')))
            elif q1 ==3:
                for k, v in information.items():
                    print('{}: {}'.format(k,v))



    except IndexError:
        print("Sorry, can not access the data of {}".format(Whattodo))