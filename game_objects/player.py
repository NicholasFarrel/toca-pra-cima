import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pygame
import controls

class Boy():
    def __init__(self, size, maxSpeed):
        self.size = size
        self.maxSpeed = maxSpeed
        self.position = pygame.Vector2()
