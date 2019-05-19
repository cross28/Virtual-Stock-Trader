import pygame 
from Text import Text

class Button(object):
    def __init__(self, win, x, y, width, height, default_color, hover_color, clicked_color, msg):
        self.win = win

        self.x = x
        self.y = y
        self.width = width
        self.height = height 

        self.text = Text(self.win, self.x, self.y, size=20)
        self.msg = msg

        self.color = ()
        self.default_color = default_color
        self.hover_color = hover_color
        self.clicked_color = clicked_color

    #Changes colors of mouse is within bounds of the button box
    def mouse_actions(self, mouse, click):
        #Button interaction
        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            self.color = self.hover_color
            if click == 1:
                self.color = self.clicked_color
        else:
            self.color = self.default_color

    def draw(self):
        pygame.draw.rect(self.win, self.color, (self.x, self.y, self.width, self.height))

        # Must set text x and y position in the draw function because the message isn't created yet
        self.text.x = self.x + self.text.get_width()/2
        self.text.y = self.y + self.text.get_height()/2
        self.text.draw(self.msg)