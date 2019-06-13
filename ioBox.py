import pygame
from Button import Button
from Text import Text

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

'''input/output box'''
class ioBox(object):
    def __init__(self, win, x, y, width, height):
        self.win = win
        self.x = x
        self.y = y
        self.width = width 
        self.height = height

        self.ioBoxOuter = Button(self.win, self.x, self.y, BLACK, BLACK, BLACK, '')
        self.ioBoxInner = Button(self.win, self.x, self.y, WHITE, WHITE, WHITE, '')

        self.ioBoxOuter.width = self.width
        self.ioBoxOuter.height = self.height

        self.ioBoxInner.width = self.ioBoxOuter.width - 10
        self.ioBoxInner.height = self.ioBoxOuter.height - 10
        self.ioBoxInner.x = self.ioBoxOuter.x + (self.ioBoxOuter.width - self.ioBoxInner.width) / 2
        self.ioBoxInner.y = self.ioBoxOuter.y + (self.ioBoxOuter.height - self.ioBoxInner.height) / 2

        self.text = Text(self.win, 0, 0, '', size=70)
        self.text.x = self.ioBoxInner.x + self.text.text.get_rect().width / 2 + 10
        self.text.y = self.ioBoxInner.y + self.text.text.get_rect().height / 2 + 40

    def draw(self):
        self.ioBoxOuter.draw()
        self.ioBoxInner.draw()
        self.text.draw()

    def updateBox(self, string):
        self.text.changeMessage(string)
