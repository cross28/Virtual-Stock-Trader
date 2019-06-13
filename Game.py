import pygame
import requests as re 
import json
import datetime as dt 
import time

from Button import Button
from Text import Text
from Stock import Stock
from ioBox import ioBox

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
money = 50000
moneyBuffer = ''
moneyBox = Text(win, 20, 40, '${}'.format(money), size=90)
buy_btn = Button(win, SCREEN_WIDTH / 5, 800, GREEN, BRIGHT_GREEN, DARK_GREEN, 'Buy')
sell_btn = Button(win, 3 * SCREEN_WIDTH / 5, 800, RED, BRIGHT_RED, DARK_RED, 'Sell')

#Input box for buying/selling the stocks
inpBox = ioBox(win, buy_btn.x, SCREEN_HEIGHT / 3, buy_btn.width + sell_btn.width, 200)
outBox = ioBox(win, buy_btn.x, 300, buy_btn.width + sell_btn.width, 200)
screenText = Text(win, inpBox.x, inpBox.y + inpBox.height + 20, 'How many shares would you like to buy?', size=50)

#Stock buttons
companyPrices = {'FB':{'1. open': 20}, 'AMZN':{'1. open': 20}, 'AAPL':{'1. open': 20}, 'MSFT':{'1. open':20}, 'NFLX':{'1. open': 20}}
facebook = Stock(win, 30, 300, fb, companyPrices['FB'])
amazon = Stock(win, SCREEN_WIDTH / 5, 300, amzn, companyPrices['AMZN'])
apple = Stock(win, 2 * SCREEN_WIDTH / 5, 300, appl, companyPrices['AAPL'])
microsoft = Stock(win, 3 * SCREEN_WIDTH / 5, 300, msft, companyPrices['MSFT'])
netflix = Stock(win, 4.2 * SCREEN_WIDTH / 5, 300, nflx, companyPrices['NFLX'])
stocks = [facebook, amazon, apple, microsoft, netflix]

def buySellMenu():
    global money
    global moneyBox
    global moneyBuffer

    moneyBuffer = ''

    if buy_btn.isClicked is True and moneyBuffer:
        money -= int(moneyBuffer)
        moneyBox.changeMessage('${}'.format(money))
        buy_btn.isClicked = False
    elif sell_btn.isClicked is True and moneyBuffer:
        money += int(moneyBuffer)
        moneyBox.changeMessage('${}'.format(money))
        sell_btn.isClicked = False

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
                elif event.key != pygame.K_BACKSPACE:
                    if inpBox.text.text.get_rect().width <= inpBox.width - 33:
                        moneyBuffer += chr(event.key) 
                        inpBox.updateBox(moneyBuffer)
                    else:
                        pass
                else:
                    moneyBuffer = ''
                    inpBox.updateBox(moneyBuffer)

        win.fill(WHITE)
        buy_btn.draw(mainMenu)
        sell_btn.draw(mainMenu)        
        screenText.draw()
        inpBox.draw()
        moneyBox.draw()
        pygame.display.update()

def mainMenu():
    global money
    global moneyBox
    global moneyBuffer

    if buy_btn.isClicked is True and moneyBuffer:
        money -= int(moneyBuffer)
        moneyBox.changeMessage('${}'.format(money))
        buy_btn.isClicked = False
    elif sell_btn.isClicked is True and moneyBuffer:
        money += int(moneyBuffer)
        moneyBox.changeMessage('${}'.format(money))
        sell_btn.isClicked = False

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
        for stock in stocks:
            stock.draw(buySellMenu)     
        moneyBox.draw()
        inpBox.updateBox('')
        pygame.display.update()

if __name__ == '__main__':
    mainMenu()
    pygame.quit()
