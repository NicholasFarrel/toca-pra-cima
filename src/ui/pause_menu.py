import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pygame
from src.game.settings import *
from src.systems.rendering import render_main_menu, render_pause_menu
from src.systems.input_handler import handle_input_for_menu, handle_input_for_pause_menu
from src.game.constants import *
from src.utils.helper_functions import update_colors, Button, Title

pygame.init()

pause_title = Title(pygame.font.SysFont(None, 72),"Menu de Pause", True, WHITE)
return_button = Button(None, 48, "Iniciar Jogo", True, BLUE, WHITE, (SCREEN_WIDTH // 2, SCREEN_HEIGHT//2) )

pause_background = {
    'color' : BLUE
}

pause_menu_assets={
    'pause_title' : pause_title,
    'return_button' : return_button,
    'pause_background' : pause_background
}
pause_menu_assets['buttons'] = [return_button]

def pause_menu(screen):
    #global pause_title

    update_colors(pause_menu_assets)
    is_paused = handle_input_for_pause_menu(pause_menu_assets)
    render_pause_menu(screen, pause_menu_assets)

    return is_paused
