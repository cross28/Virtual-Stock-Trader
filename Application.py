import pygame
from Stock import Stock
from Button import Button

pygame.init()

class game(object):
    def __init__(self, companies=[]):
        self.companies = companies
        self.stock = Stock(self.companies)

        self.win = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('Virtual Stock Trader')

        self.button = Button(50, 50, 50, 50, self.win)
        print(self.stock.companyPrices)

    def run(self):
        run = True
        while run:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.button.draw()
            pygame.display.update()

        pygame.quit()


g = game(['AMZN'])
g.run()