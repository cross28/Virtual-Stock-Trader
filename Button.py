import pygame 

class Button(object):
    def __init__(self, x, y, width, height, default_color, hover_color, clicked_color, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        self.text = text

        self.color=()
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

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))