import pygame
from Button import Button
from Stock import Stock
from Text import Text

import requests as re 
import json
import datetime as dt
import time

RED = (255, 0, 0)
BRIGHT_RED = (255, 99, 71)
DARK_RED = (139, 0, 0)
GREEN = (0, 255, 0, 0.5)
BRIGHT_GREEN = (50, 205, 50)
DARK_GREEN = (0, 100, 0)

api_key = open('secret.txt', 'r').read()
day = dt.date.today()
companyList = ['AMZN', 'AAPL', 'FB', 'MSFT', 'NFLX']
companyPrices = {}
for company in companyList:
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&outputsize=full&apikey='.format(company) + api_key
    data = re.get(url).json()['Time Series (Daily)'][str('2019-05-24')]
    companyPrices[company] = data
companyPrices = json.dumps(companyPrices, indent = 2)

class Menu(object):
    def __init__(self, win, screen_width, screen_height):
        self.win = win
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.money = Text(self.win, 20, 40, '50, 000', size=40)
        self.money.msg = 'Hello'
        self.buy_btn = Button(self.win, self.screen_width / 5, 800, GREEN, BRIGHT_GREEN, DARK_GREEN, 'BUY')
        self.sell_btn = Button(self.win, 3 * self.screen_width / 5, 800, RED, BRIGHT_RED, DARK_RED, 'SELL')

        self.companyPrices = companyPrices
        self.facebook = Stock(self.win, 10, 300, 'images/facebook.png', self.companyPrices)
        self.amazon = Stock(self.win, self.screen_width / 5, 300, 'images/amazon.png', self.companyPrices)
        self.apple = Stock(self.win, 2 * self.screen_width / 5, 300, 'images/apple.png', self.companyPrices)
        self.microsoft = Stock(self.win, 3 * self.screen_width / 5, 300, 'images/microsoft.png', self.companyPrices)
        self.netflix = Stock(self.win, 4.2 * self.screen_width / 5, 300, 'images/netflix.png', self.companyPrices)

    def displayBuySellMenu(self):
        self.buy_btn.draw()
        self.sell_btn.draw()
        self.money.draw()

        self.facebook.draw()
        self.amazon.draw()
        self.apple.draw()
        self.microsoft.draw()
        self.netflix.draw()


