import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pygame
from src.game.settings import *
from src.systems.rendering import render_main_menu, render_pause_menu
from src.systems.input_handler import handle_input_for_menu, handle_input_for_pause_menu
from src.game.constants import *
from src.utils.helper_functions import update_colors, Button, Title, Background

pygame.init()

title = Title(
    pygame.font.Font('assets/fonts/ChunkFive-Regular.otf', 72),"Toca Pra Cima",
    True,(255, 253, 130), (SCREEN_WIDTH//2, SCREEN_HEIGHT//10)
    )
title2 = Title(
    pygame.font.Font('assets/fonts/ChunkFive-Regular.otf', 52),"PLAY",
    True,(0, 0, 0), ((SCREEN_WIDTH//2)+2, SCREEN_HEIGHT//2)
    )
title3 = Title(
    pygame.font.Font('assets/fonts/ChunkFive-Regular.otf', 52),"SAIR",
    True,(0, 0, 0), ((SCREEN_WIDTH//2)+2, SCREEN_HEIGHT//2 + 60)
    )

start_game_button = Button(
    'assets/fonts/ChunkFive-Regular.otf', 48, 
    'PLAY', True, (244, 200, 6), WHITE, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    )

quit_button = Button(
    'assets/fonts/ChunkFive-Regular.otf', 48, 
    "SAIR", True, (244, 200, 6), WHITE, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 60)
    )
background = Background(BLACK, 'assets/sprites/background/start.png')        

main_menu_assets = {
    'background' : background,  
    'title' : title,
    'title2' : title2,
    'title3' : title3,
    'start_game_button': start_game_button,
    'quit_button' : quit_button
}
main_menu_assets['buttons'] = [start_game_button, quit_button]
 

def main_menu(screen):

    update_colors(main_menu_assets)
    is_in_main_menu = handle_input_for_menu(main_menu_assets)
    render_main_menu(screen, main_menu_assets)

    return is_in_main_menu

