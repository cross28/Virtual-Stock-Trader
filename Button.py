import pygame 

class Button(object):
    def __init__(self, x, y, width, height, win):
        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        self.win = win

    def draw(self):
        pygame.draw.rect(self.win, (255,0,0), (self.x, self.y, self.width, self.height))

    