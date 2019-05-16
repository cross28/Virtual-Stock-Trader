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

    #Changes colors of mouse is within bounds of the button box
    def is_hovering(self, mouse):
        #Button interaction
        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            self.active(True)
        else:
            self.active(False)

        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            self.active(True)
        else:
            self.active(False)

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))