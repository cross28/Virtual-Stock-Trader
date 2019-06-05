import pygame 
import time
from Text import Text

class Button(object):
    def __init__(self, win, x, y, default_color, hover_color, clicked_color, msg):
        self.win = win
        self.x = x
        self.y = y
        self.width = 200
        self.height = 90

        self.msg = msg
        self.text = Text(self.win, self.x, self.y, self.msg, size=50)
        
        self.color = ()
        self.default_color = default_color
        self.hover_color = hover_color
        self.clicked_color = clicked_color

    #Changes colors of mouse is within bounds of the button box, checks for clicks
    def events(self, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            self.color = self.hover_color
            if click == 1 and action != None:
                self.color = self.clicked_color
                action()
        else:
            self.color = self.default_color

    def draw(self, action=None):
        self.events(action)
        pygame.draw.rect(self.win, self.color, (self.x, self.y, self.width, self.height))

        # Must set text x and y position in the draw function because the message isn't created yet
        self.text.x = self.x + self.text.text.get_rect().width / 2
        self.text.y = self.y + self.text.text.get_rect().height / 2
        self.text.draw()