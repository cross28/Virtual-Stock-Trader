import requests as re 
import json
import datetime as dt

api_key = open('secret.txt', 'r').read()

class Stock(object):
    def __init__(self, win):
        self.win = win
        self.companyList = ['AMZN', 'AAPL', 'FB', 'MSFT', 'NFLX', 'SNAP', 'TSLA', 'TWTR']
    
    def getStockData(self):
        day = dt.date.today()
        for company in self.companyList:
            url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&outputsize=full&apikey='.format(company) + api_key
            data = re.get(url).json()
            data = data["Time Series (Daily)"][str('2019-05-15')]
            self.companyPrices[company] = data
        self.companyPrices = json.dumps(self.companyPrices, indent = 2)
        