import pygame

'''Will handle text output to the menu'''
class Text(object):
    msg = None

    def __init__(self, win, x, y, size=30):
        self.font = pygame.font.Font('Arial.ttf', size)
        self.win = win
        self.x = x
        self.y = y 

    def draw(self, msg, inBox = False):
        self.msg = msg
        text = self.font.render(self.msg, 1, (0,0,0))
        self.win.blit(text, (self.x, self.y))

        # The inBox boolean is for buttons.
        # Will be true if text is for button
        if inBox is True:
            self.x = text.get_rect().width / 2
            self.y = text.get_rect().height / 2