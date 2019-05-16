import pygame
from Stock import Stock
from Button import Button

pygame.init()

class game(object):
    def __init__(self):
        self.SCREEN_WIDTH = 1000
        self.SCREEN_HEIGHT = 700
        self.win = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption('Virtual Stock Trader')

        #x, y, width, height, window
        self.button = Button(50, 50, 50, 50, 'images/buy.jpg')
        

    def run(self):
        run = True
        while run:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.win.fill((255,255,255))
            self.button.draw(self.win)
            pygame.display.update()

        pygame.quit()

def main():
    if __name__=='__main__':
        g = game()
        g.run()

main()