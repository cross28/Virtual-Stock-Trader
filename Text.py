import pygame
import pygame.freetype

'''Will handle text output to the menu'''
class Text(object):
    msg = None
    
    def __init__(self, win, x, y, size=30):
        self.font = pygame.font.SysFont('Arial.ttf', size)
        self.win = win

        self.x = x
        self.y = y 

    def draw(self, msg):
        self.msg = msg
        self.text = self.font.render(self.msg, 1, (0,0,0))
        self.win.blit(self.text, (self.x, self.y))

    def get_width(self):
        return 20

    def get_height(self):
        return 20