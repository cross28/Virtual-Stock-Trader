import pygame 

class Button(object):
    def __init__(self, x, y, width, height, inactive_color, active_color, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        self.text = text

        self.color=()
        self.inactive_color = inactive_color
        self.active_color = active_color

    def active(self, a=False):
        if a is True:
            self.color = self.active_color
        else:
            self.color = self.inactive_color

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))