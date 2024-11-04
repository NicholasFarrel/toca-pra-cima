import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pygame
import controls
from config import Config

class Boy():
    def __init__(self, size, maxSpeed):
        self.size = size
        self.maxSpeed = maxSpeed
        self.position = pygame.Vector2(Config.SCREEN_WIDTH // 2 - self.size // 2, Config.SCREEN_HEIGHT - self.size)
        self.rect = pygame.Rect(self.position.x, self.position.y , self.size, self.size)
        self.color = (0, 128, 0)

    def update(self):
        self.position = controls.handle_movement(self.position,self.maxSpeed)
        self.rect = pygame.Rect(self.position.x, self.position.y , self.size, self.size)

    def render(self,screen):
        pygame.draw.rect(screen, self.color, self.rect)


def update(screen, boy):
    boy.update()
    boy.render(screen)

    

