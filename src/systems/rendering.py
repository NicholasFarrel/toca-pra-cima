import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pygame
from src.game.settings import *
from src.game.constants import *

def render_main_menu(screen, menu):
    title = menu['title']
    start_game_button = menu['start_game_button']
    quit_button = menu['quit_button']
    background = menu['background']

    screen.fill(background['color'])
    screen.blit(title.surface, title.position)
    screen.blit(start_game_button.surface, start_game_button.position)
    screen.blit(quit_button.surface, quit_button.position)


def render_pause_menu(screen, pause_menu_assets):
    pause_title = pause_menu_assets['pause_title']
    return_button = pause_menu_assets['return_button']
    pause_background = pause_menu_assets['pause_background']
    
    screen.fill(pause_background['color'])
    screen.blit(pause_title.surface, pause_title.position)
    screen.blit(return_button.surface, return_button.position)
    

def render_scene(screen,camera, player, background):
    screen.fill(BLACK)
    background.rect = pygame.Rect(background.position.x, background.position.y, background.image.get_width(),background.image.get_height())
    
    player.rect.y -= camera.position.y
    player.rect.x -= camera.position.x
    background.rect.y -= camera.position.y
    background.rect.x -= camera.position.x

    screen.blit(background.image, background.rect)

    screen.blit(player.image, player.rect)



