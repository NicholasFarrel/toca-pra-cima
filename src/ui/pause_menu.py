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

pause_title = Title(
    pygame.font.Font('assets/fonts/ChunkFive-Regular.otf', 72),"PAUSE", 
    True, WHITE, (SCREEN_WIDTH//2, SCREEN_HEIGHT//4)
    )
return_button = Button(
    'assets/fonts/ChunkFive-Regular.otf', 48, 
    'VOLTAR', True, (244, 200, 6), WHITE, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    )
pause_title2 = Title(
    pygame.font.Font('assets/fonts/ChunkFive-Regular.otf', 52),"VOLTAR",
    True,(0, 0, 0), ((SCREEN_WIDTH//2)+2, SCREEN_HEIGHT//2 + 60)
    )

pause_background = {
    'color' : (189, 98, 46)
}

pause_menu_assets={
    'pause_title' : pause_title,
    'return_button' : return_button,
    'pause_title2' : pause_title2,
    'pause_background' : pause_background
}
pause_menu_assets['buttons'] = [return_button]

def pause_menu(screen):
    #global pause_title

    update_colors(pause_menu_assets)
    is_paused = handle_input_for_pause_menu(pause_menu_assets)
    render_pause_menu(screen, pause_menu_assets)

    return is_paused
