import sys

import pygame
# initialise the pygame
class Game:
    def __init__(self):
        pygame.init()

#creating the screen
        pygame.display.set_caption("The Platform")
        self.screen = pygame.display.set_mode((800,600))

        self.clock = pygame.time.Clock()
        self.img = pygame.image.load(".venv/Lib/ninja_game/data/images/clouds/cloud_1.png")
#Game loop
    def run(self):
        while True:
         self.screen.blit(self.img,(300, 700))

         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 sys.exit()

                 pygame.display.update()
        self.clock.tick(60)

Game().run()



#Background

