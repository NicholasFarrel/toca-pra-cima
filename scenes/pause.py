import pygame
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)
from config import Config


class Menu:
    def __init__(self):
        self.color = (170, 232, 249)
        self.surface = pygame.Surface((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
        self.surface.fill(self.color)
        self.surface.set_alpha(10)
    
    def load(self, screen):
        
        screen.blit(self.surface, (0,0))
        pygame.display.flip()
