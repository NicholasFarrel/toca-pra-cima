import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pygame
from src.game.settings import *
from src.systems.rendering import render_main_menu, render_pause_menu, render_game_over_menu
from src.systems.input_handler import handle_input_for_menu, handle_input_for_pause_menu, handle_input_for_game_over_menu
from src.game.constants import *
from src.utils.helper_functions import update_colors, Button, Title

pygame.init()

title = Title(pygame.font.SysFont(None, 72),"VOCÊ MORREU",True, WHITE, (SCREEN_WIDTH//2, SCREEN_HEIGHT//4))
start_game_button = Button(None, 48, 'Voltar ao Iniciar', True, BLUE, WHITE, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
quit_button = Button(None, 48, "Quit", True, BLUE, WHITE, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 60))


background = {
    'color' : BLACK,
}

main_menu_assets = {
    'background' : background,  
    'title' : title,
    'start_game_button': start_game_button,
    'quit_button' : quit_button
}
main_menu_assets['buttons'] = [start_game_button, quit_button]
 

def game_over_menu(screen):

    update_colors(main_menu_assets)
    is_in_main_menu = handle_input_for_game_over_menu(main_menu_assets)
    render_game_over_menu(screen, main_menu_assets)

    return is_in_main_menu


