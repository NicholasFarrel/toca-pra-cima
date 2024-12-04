# to do:
# main menu : sound options
# load map

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import pygame
from settings import *
from src.systems.rendering import render_scene
from src.systems.input_handler import handle_input
from src.systems.camera import Camera
from src.ui.main_menu import main_menu
from src.ui.pause_menu import pause_menu
from src.entities.player import Girl
from src.entities import enemy
from src.game.assets import load_game_assets
from src.levels.level import Background

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

is_paused = False
is_in_main_menu = True


def main_loop():
    global is_paused, is_in_main_menu

    while True:
        if is_in_main_menu:
            is_in_main_menu = main_menu(screen)

            if not is_in_main_menu:
                load_game_assets()
                girl = Girl(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
                camera = Camera(0,0)
                background = Background()
                enemy.initialize(girl)
        else:
            if not is_paused:
                is_paused = handle_input(girl, camera, background, is_paused)
                render_scene(screen, camera, girl, background)
                
                enemy.update(screen, camera, girl)
            else:
                is_paused = pause_menu(screen)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main_loop()
            

            