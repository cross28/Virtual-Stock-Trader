import pygame
from Button import Button
from Text import Text
from Stock import Stock

import requests as re 
import json
import datetime as dt 

RED = (255, 0, 0)
BRIGHT_RED = (255, 99, 71)
DARK_RED = (139, 0, 0)
GREEN = (0, 255, 0, 0.5)
BRIGHT_GREEN = (50, 205, 50)
DARK_GREEN = (0, 100, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Virtual Stock Trader')

'''
#Grabbing Stock Data
api_key = open('secret.txt', 'r').read()
day = dt.date.today()
companyList = ['AMZN', 'AAPL', 'FB', 'MSFT', 'NFLX']
companyPrices = {}
for company in companyList:
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&outputsize=full&apikey='.format(company) + api_key
    data = re.get(url).json()['Time Series (Daily)']['2019-05-24']
    companyPrices[company] = data
'''

#Pre-loading stock images
fb = pygame.image.load('images/facebook.png')
amzn = pygame.image.load('images/amazon.png')
nflx = pygame.image.load('images/netflix.png')
appl = pygame.image.load('images/apple.png')
msft = pygame.image.load('images/microsoft.png')

#Creating buttons
money = Text(win, 20, 40, '50,000', size=40)
buy_btn = Button(win, SCREEN_WIDTH / 5, 800, GREEN, BRIGHT_GREEN, DARK_GREEN, 'Buy')
sell_btn = Button(win, 3 * SCREEN_WIDTH / 5, 800, RED, BRIGHT_RED, DARK_RED, 'Sell')

#Input box for buying/selling the stocks
inputBoxOuter = Button(win, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, BLACK, BLACK, BLACK, '')
inputBoxInner = Button(win, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, WHITE, WHITE, WHITE, '')
inputBoxOuter.width = 950
inputBoxOuter.height = 200
inputBoxInner.width = 940
inputBoxInner.height = 190
inputBoxInner.x = inputBoxOuter.x + (inputBoxOuter.width - inputBoxInner.width) / 2
inputBoxInner.y = inputBoxOuter.y + (inputBoxOuter.height - inputBoxInner.height) / 2
inputText = Text(win, 30, 90, 'hello', size=60)
inputText.x = inputBoxInner.x + inputText.text.get_rect().width / 2
inputText.y = inputBoxInner.y + inputText.text.get_rect().height / 2

#Stock buttons
companyPrices = {'FB':{'1. open': 20}, 'AMZN':{'1. open': 20}, 'AAPL':{'1. open': 20}, 'MSFT':{'1. open':20}, 'NFLX':{'1. open': 20}}
facebook = Stock(win, 30, 300, fb, companyPrices['FB'])
amazon = Stock(win, SCREEN_WIDTH / 5, 300, amzn, companyPrices['AMZN'])
apple = Stock(win, 2 * SCREEN_WIDTH / 5, 300, appl, companyPrices['AAPL'])
microsoft = Stock(win, 3 * SCREEN_WIDTH / 5, 300, msft, companyPrices['MSFT'])
netflix = Stock(win, 4.2 * SCREEN_WIDTH / 5, 300, nflx, companyPrices['NFLX'])
stocks = [facebook, amazon, apple, microsoft, netflix]

def buySellMenu():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                else:
                    string = inputText.msg + chr(event.key)
                    inputText.changeMessage(string)
                    if event.key == pygame.K_BACKSPACE:
                        string = inputText.changeMessage(string[:-1])

        win.fill(WHITE)
        buy_btn.draw(mainMenu)
        sell_btn.draw(mainMenu)
        inputBoxOuter.draw()
        inputBoxInner.draw()
        inputText.draw()
        pygame.display.update()

def mainMenu():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        
        win.fill(WHITE)
        inputText.changeMessage('')
        for stock in stocks:
            stock.draw(buySellMenu)
        pygame.display.update()


mainMenu()

pygame.quit()
