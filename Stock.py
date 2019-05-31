import pygame 
import time
from Text import Text

class Stock(pygame.sprite.Sprite):
    def __init__(self, win, x, y, img, data={}):
        pygame.sprite.Sprite.__init__(self)
        self.win = win
        self.x = x
        self.y = y
        self.width = 150
        self.height = 150

        self.data = {}
        self.data = data['1. open']
        self.data = round(float(self.data), 2)

        self.img = pygame.transform.scale(img, (self.width, self.height))
        self.text = Text(self.win, self.x + self.width / 2 - 40, self.y + self.height + 50, '{0:.2f}'.format(self.data), bold=True, font='comicsansms')

    def mouseEvents(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            pygame.draw.rect(self.win, (0, 0, 255), (self.x - 25, self.y - 25, self.width + 50, self.height + 50))
            self.win.blit(self.img, (self.x, self.y))
            if click == 1:
                pygame.draw.rect(self.win, (0, 100, 255), (self.x - 25, self.y - 25, self.width + 50, self.height + 50))
                self.win.blit(self.img, (self.x, self.y))
                return True
            else:
                return False
        else:
            self.win.blit(self.img, (self.x, self.y)) 
        
    def draw(self):
        self.mouseEvents()
        self.win.blit(self.img, (self.x, self.y))
        self.text.draw()