import pygame 

class Button(object):
    def __init__(self, x, y, width, height, bg):
        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        self.icon = pygame.image.load(bg)

    def draw(self, win):
        win.blit(self.icon, (self.x, self.y))
        #pygame.draw.rect(win, (255,0,0), (self.x, self.y, self.width, self.height))

    