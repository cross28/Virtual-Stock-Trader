import pygame 
from Text import Text

class Stock(object):
    def __init__(self, win, x, y, img, data={}):
        self.win = win
        self.x = x
        self.y = y
        self.width = 150
        self.height = 150

        self.stocksOwned = 0
        self.data = {}
        self.data = data['1. open']
        self.data = round(float(self.data), 2)

        self.img = pygame.transform.scale(pygame.image.load(img), (self.width, self.height))
        self.priceText = Text(self.win, self.x + self.width / 2 - 40, self.y + self.height + 50, 'Price: {0:.2f}'.format(self.data), font='comicsansms')
        self.stocksOwnedText = Text(self.win, self.priceText.x, self.priceText.y + 30, 'Own: {}'.format(self.stocksOwned), font='comicsansms')

        self.isClicked = False

    def draw(self,action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        #Resetting x, y, width, and height values 
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.priceText.x, self.priceText.y = self.x + self.width / 2 - 40, self.y + self.height + 50
        self.stocksOwnedText.x, self.stocksOwnedText.y = self.priceText.x, self.priceText.y + 30

        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            pygame.draw.rect(self.win, (0, 0, 255), (self.x - 25, self.y - 25, self.width + 50, self.height + 50))
            self.win.blit(self.img, (self.x, self.y))
            if click == 1 and action != None:
                self.isClicked = True
                action()       
            else:
                self.isClicked = False            
        else:
            self.win.blit(self.img, (self.x, self.y))
        self.priceText.draw()
        self.stocksOwnedText.draw()

    def stocksChange(self, number):
        self.stocksOwned += number
        self.stocksOwnedText.changeMessage('Own: {}'.format(self.stocksOwned))
        
    #If the stock was chosen, this will transform the image and draw it
    def drawSelected(self):
        x = 900
        y = 250

        self.img = pygame.transform.scale(self.img, (250, 250))
        self.stocksOwnedText.x, self.stocksOwnedText.y = x + 250, y + 80
        self.priceText.x, self.priceText.y = x + 250, y + 50

        self.win.blit(self.img, (x, y))
        self.stocksOwnedText.draw()
        self.priceText.draw()


