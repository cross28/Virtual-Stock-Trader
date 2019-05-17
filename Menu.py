import pygame
from Button import Button
from Stock import Stock
from Text import Text

RED = (255, 0, 0)
BRIGHT_RED = (255, 99, 71)
DARK_RED = (139, 0, 0)

GREEN = (0, 255, 0)
BRIGHT_GREEN = (50, 205, 50)
DARK_GREEN = (0, 100, 0)

BLACK = (0, 0, 0)
class Menu(object):
    def __init__(self):
        self.buy_btn = Button(50, 50, 50, 50, GREEN, BRIGHT_GREEN, DARK_GREEN, 'Buy')
        self.sell_btn = Button(50, 100, 50, 50, RED, BRIGHT_RED, DARK_RED, 'Sell')

        #Text(color, message, x pos, y pos, font(optional), size(optional), is_bold(optional))
        self.text = Text(BLACK, 'Choose which stocks you want to monitor from', 150, 150, size=60, is_bold=True)

        #self.choose_stocks()

   #def choose_stocks_menu():

    def draw(self, win):
        self.buy_btn.draw(win)
        self.sell_btn.draw(win)
        self.text.draw(win)
