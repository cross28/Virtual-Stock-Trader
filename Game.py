import pygame
import requests as re 
import json
import datetime as dt 
import time

from Button import Button
from Text import Text
from Stock import Stock
from ioBox import ioBox

def write(data):
    with open('settings.json', 'w') as f:
        json.dump(data, f)

#Predefined colors
RED = (255, 0, 0)
BRIGHT_RED = (255, 99, 71)
DARK_RED = (139, 0, 0)
GREEN = (0, 255, 0, 0.5)
BRIGHT_GREEN = (50, 205, 50)
DARK_GREEN = (0, 100, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Window settings
pygame.init()
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Virtual Stock Trader')

#Handling json file.
with open('settings.json') as j:
	f = json.load(j)
fileSave = {}
fileSave['money'] = f['money']
'''
#Grabbing Stock Data
api_key = open('secret.txt', 'r').read()
day = dt.date.today()
companyList = ['AMZN', 'AAPL', 'FB', 'MSFT', 'NFLX']
companyPrices = {}
for company in companyList:
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&outputsize=full&apikey='.format(company) + api_key
    data = re.get(url).json()['Time Series (Daily)']['2019-05-24']
    companyPrices[company] = data.
api_key.close()
'''

#Creating buttons 
money = f['money']
moneyBox = Text(win, 20, 40, '${}'.format(money), size=90)
buy_btn = Button(win, SCREEN_WIDTH / 5, 800, GREEN, BRIGHT_GREEN, DARK_GREEN, 'Buy')
sell_btn = Button(win, 3 * SCREEN_WIDTH / 5, 800, RED, BRIGHT_RED, DARK_RED, 'Sell')

#Input box for buying/selling the stocks
inpBox = ioBox(win, buy_btn.x, SCREEN_HEIGHT / 3, buy_btn.width + sell_btn.width, 200)
screenText = Text(win, inpBox.x, inpBox.y + inpBox.height + 20, 'How many shares would you like to buy?', size=50)

#Stock buttons
companyPrices = {'FB':{'1. open': 20}, 'AMZN':{'1. open': 19}, 'AAPL':{'1. open': 20}, 'MSFT':{'1. open':20}, 'NFLX':{'1. open': 20}}
facebook = Stock(win, 30, 300, 'images/facebook.png', companyPrices['FB'])
amazon = Stock(win, SCREEN_WIDTH / 5, 300, 'images/amazon.png', companyPrices['AMZN'])
apple = Stock(win, 2 * SCREEN_WIDTH / 5, 300, 'images/apple.png', companyPrices['AAPL'])
microsoft = Stock(win, 3 * SCREEN_WIDTH / 5, 300, 'images/microsoft.png', companyPrices['MSFT'])
netflix = Stock(win, 4.2 * SCREEN_WIDTH / 5, 300, 'images/netflix.png', companyPrices['NFLX'])
stocks = [facebook, amazon, apple, microsoft, netflix]
stockNames = ['facebook', 'amazon', 'apple', 'microsoft', 'netflix']

#Loading stocks owned
for stock in stocks:
    i = stocks.index(stock)
    stock.stocksChange(f[stockNames[i]][0])

#Calculate Gain/Loss
gain_loss_text = Text(win, 30, 30, '')
gain_loss = 0
for stock in stockNames:
    i = stockNames.index(stock)
    if f[stock][0] != 0:
        gain_loss += f[stock][0] * (float(f[stock][1]) - float(stocks[i].data))
if gain_loss < 0: #Gain
    gain_loss_text.changeMessage('You gained ${}'.format(gain_loss))
elif gain_loss > 0: #Loss
    gain_loss_text.changeMessage('You lost ${}'.format(abs(gain_loss)))
else: #No gain or loss 
    gain_loss_text.changeMessage('You didn\'t lose any money')

#Updating JSON file with current stock info
for stock in stockNames:
    i = stockNames.index(stock)
    fileSave[stock] = [stocks[i].stocksOwned, stocks[i].data]
write(fileSave)

#Buffers
buffer = ''
index = 0

def buySellMenu():
    global buffer
    global index
    buffer = '' 

    '''The index will act as a buffer for the stock 
       price. Checking to see if the stock was pressed
       has to be checked in the buy/sell menu because
       the main menu ends before checking of the 
       stock.isClicked boolean can return a value.'''
    for stock in stocks:
        if stock.isClicked is True:
            index = stocks.index(stock)
            stock.isClicked = False
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                write(fileSave)
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    write(fileSave)
                    pygame.quit()
                    quit()
                elif event.key != pygame.K_BACKSPACE:
                    #Gets keyboard input for buying and selling
                    if inpBox.text.text.get_rect().width <= inpBox.width - 33:
                        buffer += chr(event.key) 
                        inpBox.updateBox(buffer)
                    else:
                        pass
                else:
                    buffer = ''
                    inpBox.updateBox(buffer)

        win.fill(WHITE)
        buy_btn.draw(mainMenu)
        sell_btn.draw(mainMenu) 
        stocks[index].drawSelected()       
        screenText.draw()
        inpBox.draw()
        moneyBox.draw()
        pygame.display.update()

def mainMenu():
    global money
    global buffer
    global fileSave
    global index
    
    '''The money is changed here because
       the buy and sell menu breaks before
       any operations can be performed on it'''
    if buy_btn.isClicked is True and buffer:
        if int(buffer) != 0 and float(buffer) * stocks[index].data <= money:
            stocks[index].stocksChange(int(buffer))
            money -= float(buffer) * float(stocks[index].data)
            moneyBox.changeMessage('${}'.format(money))
            fileSave['money'] = money
            fileSave[stockNames[index]][0] += int(buffer)
            buy_btn.isClicked = False
        else:
            buy_btn.isClicked = False
    elif sell_btn.isClicked is True and buffer:
        if int(buffer) != 0 and 0 <= int(buffer) <= stocks[index].stocksOwned:
            stocks[index].stocksChange(-int(buffer)) 
            money += float(buffer) * float(stocks[index].data)
            moneyBox.changeMessage('${}'.format(money))
            fileSave['money'] = money
            fileSave[stockNames[index]][0] -= int(buffer)
            sell_btn.isClicked = False      
        else:
            sell_btn.isClicked = False
    index = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                write(fileSave)
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    write(fileSave)
                    pygame.quit()
                    quit()

        win.fill(WHITE)   
        for stock in stocks:
            stock.draw(buySellMenu)     
        gain_loss_text.draw()
        moneyBox.draw()
        inpBox.updateBox('')
        pygame.display.update()

if __name__ == '__main__':
    mainMenu()