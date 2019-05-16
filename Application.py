import pygame
from Stock import Stock
from Button import Button

pygame.init()

WHITE = (255, 255, 255)

RED = (255, 0, 0)
BRIGHT_RED = (255, 99, 71)
DARK_RED = (139, 0, 0)

GREEN = (0, 255, 0)
BRIGHT_GREEN = (50, 205, 50)
DARK_GREEN = (0, 100, 0)

class game(object):
    def __init__(self):
        self.SCREEN_WIDTH = 1000
        self.SCREEN_HEIGHT = 700
        self.win = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption('Virtual Stock Trader')

        #x, y, width, height, default color, hover color, clicked color, text
        self.buy_btn = Button(50, 50, 50, 50, GREEN, BRIGHT_GREEN, DARK_GREEN, 'hello')
        self.sell_btn = Button(50, 100, 50, 50, RED, BRIGHT_RED, DARK_RED, 'goodbye')
        

    def run(self):
        run = True
        while run:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            '''Mouse Events'''
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            self.buy_btn.mouse_actions(mouse, click[0])
            self.sell_btn.mouse_actions(mouse, click[0])


            '''Drawing and updating the window'''
            self.win.fill(WHITE)

            self.buy_btn.draw(self.win)
            self.sell_btn.draw(self.win)

            pygame.display.update()


        pygame.quit()

def main():
    if __name__=='__main__':
        g = game()
        g.run()

main()