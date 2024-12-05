# to do:
# main menu : sound options
# load map

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import pygame
import random
from settings import *
from src.systems.rendering import render_scene
from src.systems.input_handler import handle_input
from src.systems.camera import Camera
from src.ui.main_menu import main_menu
from src.ui.finished_menu import finished_menu
from src.ui.game_over_menu import game_over_menu
from src.ui.pause_menu import pause_menu
from src.entities.player import Girl
from src.entities import enemy
from src.game.assets import load_game_assets
from src.levels.level import Background
from src.game.constants import *
from src.entities.objects import Magnesio 

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

is_paused = False
is_dead = False
is_in_main_menu = True
finished = False

pygame.mixer.music.load('assets/audio/music/music.mp3')
pygame.mixer.music.set_volume(0.5)  # Volume de 0.0 a 1.0
pygame.mixer.music.play(loops=-1)  # Reproduz em loop infinito

images=[]
magnesios = []

def main_loop():
    global is_paused, is_in_main_menu, is_dead, finished, magensios

    while True:
        if is_in_main_menu:
            is_dead = False
            finished = False
            is_in_main_menu = main_menu(screen)

            if not is_in_main_menu:
                load_game_assets()
                girl = Girl(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
                camera = Camera(0,0)
                background = Background()
                enemies = enemy.initialize(girl)
                image_folder = 'assets/animation'
                for file_name in sorted(os.listdir(image_folder)):  # Sort ensures the correct order
                    if file_name.endswith((".png", ".jpg", ".jpeg")):  # Filter image files
                        img_path = os.path.join(image_folder, file_name)
                        images.append(pygame.transform.scale(
                            pygame.image.load(img_path),
                            (SCREEN_HEIGHT,SCREEN_WIDTH)))
                        
                for i in range(num_magnesios):
                    magnesios.append(Magnesio(pygame.Vector2(random.randint(0, SCREEN_WIDTH), random.randint(-background.image.get_height(),-SCREEN_HEIGHT//2,))))

        elif is_dead:
            is_in_main_menu = game_over_menu(screen)
        elif finished:
            is_in_main_menu = finished_menu(screen, images)
        elif not is_paused:
                magnesios[:] = [m for m in magnesios if not m.consumed]
                is_paused = handle_input(girl, camera,enemies, background, is_paused)
                render_scene(screen, camera, girl, background, magnesios)
                enemy.update(screen, camera, girl, enemies)
                #print(girl.position.y, background.image.get_height() - SCREEN_HEIGHT)
                if girl.life <= 0:
                    is_dead = True

                elif girl.position.y <= -7449:
                    finished = True 

        else:
            is_paused = pause_menu(screen)
        


        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main_loop()
            

            