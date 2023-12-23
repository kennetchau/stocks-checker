# stocks-checker
## General
Edited: 08/28/2020
Added function to research stocks

This is originally a subprogram of the project 'Simple virtual assistance', it includes functions such as searching up and analyzing stock price data, downloading all the ohlc data within a time period for a selected stock, analyzing correlation between stocks and downloading price data of all the stocks in the s&amp;p 500 and nasdaq. 

The program use panda, yfinance to get price data from yahoo finance. Use mplfinance to plot ohlc graphs. Beautiful soup for web scraping(getting all ticker symbol of S&P 500 from wikipedia)

Built with:
* beautiful soup 
* yfinance
* mplfinance
* panda
* numpy 
* datetime
* matplotlib
* os
* pickle

## Install requires packages:
Use the package manager pip to install the requirenment package
```bash
pip install -r requirenments.txt
```

## How to use
After install the required packages, click stocks.py to open the program 
The program will show the s&p index of the last 30 days. 
![opening](https://github.com/kennetchau/stocks-checker/blob/master/examples/showing%20s%26p%20price%20history.PNG)


Close the graph and you will be present with functions such as search current and historic stock price, download data about a stock, get all s&p or nasdaq price data and others 
![option](https://github.com/kennetchau/stocks-checker/blob/master/examples/option.PNG)

Here are some examples of the output:

###### Getting stock history
![stock history](https://github.com/kennetchau/stocks-checker/blob/master/examples/getting%20more%20stock%20history.PNG)

###### Downloading data 
![downloaddata](https://github.com/kennetchau/stocks-checker/blob/master/examples/download%20data%20as%20csv%20files.PNG)

###### Showing Correlation heatmap 
![downloaddata](https://github.com/kennetchau/stocks-checker/blob/master/examples/correlation%20heatmap.PNG)

###### Researching Stock
![downloaddata](https://github.com/kennetchau/stocks-checker/blob/master/examples/researcheg1.PNG)
![downloaddata](https://github.com/kennetchau/stocks-checker/blob/master/examples/researcheg2.PNG)

## Roadmap
In the future, I would like to incorporate a function to do correlation between a stock and a index. This will allow the user to use how correlated a stock is to a region. Also, I would like to include a research function so the user could pull the balance sheet and income statement of a company if they wish to.

## Contact 
Name: Ming Yin Kenneth Chau 

Email: kenetx@pm.me


