import pygame
from src.game.constants import *
from src.game.settings import *

class Background:
    def __init__(self):
        self.image = background['image']
        self.position = pygame.Vector2(0,-(self.image.get_height() - SCREEN_HEIGHT))
        self.rect = pygame.Rect(self.position.x, self.position.y, self.image.get_width(),self.image.get_height())
        