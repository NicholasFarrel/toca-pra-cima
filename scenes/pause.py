import pygame


class Menu:
    def __init__(self):
        self.paused = True
        self.color = (0,0,0)
    
    def load(self, screen):
        screen.fill(self.color)
    