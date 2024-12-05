import pygame
from src.systems.rendering import render_magnesio
from src.game.constants import *

class Magnesio:
    def __init__(self, position):
        self.position = position
        self.heal_value = 1
        self.size = 100
        self.consumed = False
        self.image = pygame.transform.scale(
            pygame.image.load('assets/sprites/objects/magnesio2.png'),
            (self.size, self.size)
            )
        
        self.rect = pygame.Rect(*self.position, self.size,self.size)

    def update(self, screen, player, camera):
        dif = self.position - player.position
        distance = dif.length()
        self.rect.topleft = self.position
        if distance < 100 and player.life < max_life:
            player.life += self.heal_value
            self.consumed = True
        
    

