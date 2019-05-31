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

#Grabbing Stock Data
api_key = open('secret.txt', 'r').read()
day = dt.date.today()
companyList = ['AMZN', 'AAPL', 'FB', 'MSFT', 'NFLX']
companyPrices = {}
for company in companyList:
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&outputsize=full&apikey='.format(company) + api_key
    data = re.get(url).json()['Time Series (Daily)']['2019-05-24']
    companyPrices[company] = data


#Pre-loading stock images
fb = pygame.image.load('images/facebook.png')
amzn = pygame.image.load('images/amazon.png')
nflx = pygame.image.load('images/netflix.png')
appl = pygame.image.load('images/apple.png')
msft = pygame.image.load('images/microsoft.png')

class Menu(object):
    def __init__(self, win, screen_width, screen_height):
        self.win = win
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.money = Text(self.win, 20, 40, '50, 000', size=40)
        self.buy_btn = Button(self.win, self.screen_width / 5, 800, GREEN, BRIGHT_GREEN, DARK_GREEN, 'BUY')
        self.sell_btn = Button(self.win, 3 * self.screen_width / 5, 800, RED, BRIGHT_RED, DARK_RED, 'SELL')

        '''Stock Objects'''
        self.companyPrices = companyPrices
        #self.companyPrices = 20
        facebook = Stock(self.win, 30, 300, fb, self.companyPrices['FB'])
        amazon = Stock(self.win, self.screen_width / 5, 300, amzn, self.companyPrices['AMZN'])
        apple = Stock(self.win, 2 * self.screen_width / 5, 300, appl, self.companyPrices['AAPL'])
        microsoft = Stock(self.win, 3 * self.screen_width / 5, 300, msft, self.companyPrices['MSFT'])
        netflix = Stock(self.win, 4.2 * self.screen_width / 5, 300, nflx, self.companyPrices['NFLX'])
        self.stocks = [facebook, amazon, apple, microsoft, netflix]

    def mainMenu(self):
        for stock in self.stocks:
            stock.draw()

    def displayBuySellMenu(self):
        self.buy_btn.draw()
        self.sell_btn.draw()
