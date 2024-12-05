import pygame
from src.game.settings import *


class Button:
    def __init__(self,file_path,size,label,antialias,selected_color, normal_color, position):
        self.file_path = file_path
        self.size = size
        self.label = label
        self.antialias = antialias
        self.selected_color = selected_color
        self.normal_color = normal_color
        self.font = pygame.font.SysFont(self.file_path, self.size)
        self.surface = self.font.render(self.label, self.antialias, self.normal_color)
        self.position = (position[0] - self.surface.get_width() // 2, position[1])
 
 
class Title:
    def __init__(self,font,label,antialias, color):
        self.font = font
        self.label = label
        self.antialias = antialias
        self.color = color
        self.surface = self.font.render(self.label, self.antialias, self.color)
        self.position = (SCREEN_WIDTH // 2  - self.surface.get_width() // 2, SCREEN_HEIGHT // 4)


def update_colors(menu_assets):
    mouse_position = pygame.mouse.get_pos()

    for button in menu_assets['buttons']:
        if (mouse_position[0] - button.position[0] <=  button.surface.get_width() and mouse_position[0] - button.position[0] >= 0) and (mouse_position[1] - button.position[1] <=  button.surface.get_height() and mouse_position[1] - button.position[1] >= 0):
            button.color = button.selected_color 
        else :
            button.color = button.normal_color
        button.surface = button.font.render(button.label, button.antialias, button.color)
   
