import pygame

'''Will handle text output to the menu'''
class Text(object):
    def __init__(self, color, msg, x, y, font='comicsans', size=30, is_bold=False):
        self.font = pygame.font.SysFont(font, size, is_bold)
        self.msg = self.font.render(msg, 1, color)

        self.x = x
        self.y = y 

    def draw(self, win):
        win.blit(self.msg, (self.x, self.y))