import pygame
import sys
import math
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)
from config import Config
from scenes.button import Button


class Menu:
    def __init__(self):
        #self.color = (170, 232, 249)
        self.color = (255,255,255)
        #self.color = (0,0,0)
        self.surface = pygame.Surface((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
        self.surface.fill(self.color)
        self.surface.set_alpha(120)
        self.active = False
    
    def load(self, screen):
        if not self.active:
            screen.blit(self.surface, (0,0))
            self.active = True
