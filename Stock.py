import requests as re 
import json
import datetime as dt

api_key = 'KZRJFKG9B169Z7XY'

class Stock(object):
    def __init__(self, companyList=[]):
        day = dt.date.today()
        self.companyList = companyList
        self.companyPrices = {}
        for company in companyList:
            url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&outputsize=full&apikey='.format(company) + api_key
            data = re.get(url).json()
            data = data["Time Series (Daily)"][str(day)]
            self.companyPrices[company] = data
        #self.companyPrices = json.dumps(self.companyPrices, indent = 2)
