import pygame
from Stock import Stock
from Button import Button
from Menu import Menu
WHITE = (255, 255, 255)
pygame.init()

class game(object):
    def __init__(self):
        self.SCREEN_WIDTH = 1500
        self.SCREEN_HEIGHT = 1000
        self.win = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption('Virtual Stock Trader')

        self.menu = Menu(self.win, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        
        
    def run(self):
        run = True
        while run:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False


            '''Drawing and updating the window'''
            self.win.fill(WHITE)
            self.menu.display()
            pygame.display.update()


        pygame.quit()



if __name__=='__main__':
    g = game()
    g.run()