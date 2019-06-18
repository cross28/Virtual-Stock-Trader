import pygame

'''Will handle text output to the menu'''
class Text(object):
    def __init__(self, win, x, y, msg, size=30, bold=False):
        self.msg = msg
        self.size = size
        self.default_font = pygame.font.get_fonts()[47] #freesans
        self.bold = bold
        self.font = pygame.font.SysFont(self.default_font, self.size, self.bold)
        self.text = self.font.render(self.msg, True, (0,0,0))
        self.textSize = self.font.size(self.msg)
        self.win = win
        self.x = x
        self.y = y 

    def draw(self):
        self.win.blit(self.text, (self.x, self.y))

    def changeMessage(self, msg):
        self.msg = msg
        self.text = self.font.render(self.msg, True, (0,0,0))
