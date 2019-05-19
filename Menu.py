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
    def __init__(self, win, screen_width, screen_height):
        self.win = win
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.buy_btn = Button(self.win, 50, 50, 50, 50, GREEN, BRIGHT_GREEN, DARK_GREEN, 'Buy')
        self.sell_btn = Button(self.win, 50, 100, 50, 50, RED, BRIGHT_RED, DARK_RED, 'Sell')

    def choose_stocks_menu(self):
        text = Text(self.win, 100,100)
        text.draw('Hi')
        self.buy_btn.draw()
        self.sell_btn.draw()

    #def main_menu(self):
        
