import pygame

'''Will handle text output to the menu'''
class Text(object):
    def __init__(self, win, x, y, msg, size=30):
        self.msg = msg
        self.font = pygame.font.Font('Arial.ttf', size)
        self.text = self.font.render(self.msg, True, (0,0,0))
        self.win = win
        self.x = x
        self.y = y 

    def draw(self):
        self.win.blit(self.text, (self.x, self.y))
