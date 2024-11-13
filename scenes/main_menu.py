import pygame
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)
from config import Config
from scenes.button import Button


def getFont(size):
    return pygame.font.Font('sprites/menu/font.ttf', size)


class MainMenu():
    

    def __init__(self):

        self.image = pygame.image.load('sprites/menu/Background.png')
        self.playButton =  Button(
            image = pygame.transform.scale(pygame.image.load('sprites/menu/button.png'),(300,100)),
            position=(Config.SCREEN_WIDTH//2,Config.SCREEN_HEIGHT//2),
            textInput='play',
            font=getFont(10), baseColor = (0,0,100),
            hoveringColor=(0,100,0),
            )
        

    def update(self, screen):
        
        screen.blit(self.image, (0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        mousePosition = pygame.mouse.get_pos()

        for button in [self.playButton]:
            button.changeColor(mousePosition)
            button.update(screen)
            

        pygame.display.flip()
        
        