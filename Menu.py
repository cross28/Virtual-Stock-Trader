import pygame
from Button import Button
from Stock import Stock

RED = (255, 0, 0)
BRIGHT_RED = (255, 99, 71)
DARK_RED = (139, 0, 0)

GREEN = (0, 255, 0)
BRIGHT_GREEN = (50, 205, 50)
DARK_GREEN = (0, 100, 0)

class Menu(object):
    def __init__(self, win, screen_width, screen_height):
        self.win = win
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.stock = Stock(self.win)

        self.buy_btn = Button(self.win, self.screen_width / 5, 800, GREEN, BRIGHT_GREEN, DARK_GREEN, 'BUY')
        self.sell_btn = Button(self.win, 3 * self.screen_width / 5, 800, RED, BRIGHT_RED, DARK_RED, 'SELL')

        companies = ['amazon', 'apple', 'facebook', 'microsoft', 'netflix', 'snapchat', 'tesla', 'twitter']
        company_data = {}
        for company in companies:
            company_img = pygame.image.load('images/{}.png'.format(company))

    def display(self):
        self.buy_btn.draw()
        self.sell_btn.draw()

