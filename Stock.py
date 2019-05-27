import pygame 

class Stock(object):
    def __init__(self, win, x, y, img, data={}):
        self.win = win
        self.x = x
        self.y = y

        self.data = {}
        self.data = data

        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, (150, 150))

    def draw(self):
        self.win.blit(self.img, (self.x, self.y))     
        