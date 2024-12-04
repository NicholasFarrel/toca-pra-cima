import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.game.constants import *
from src.game.settings import *
import pygame
import math


def handle_input_for_pause_menu(pause_menu_assets):
    return_button = pause_menu_assets['return_button']
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Enter key to start the game
                print("return")
                pygame.time.wait(300)
                return False # Exit the pause menu and returns to the game

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if event.button == 1:
                if (mouse_position[0] - return_button.position[0] <=  return_button.surface.get_width() and mouse_position[0] - return_button.position[0] >= 0) and (mouse_position[1] - return_button.position[1] <=  return_button.surface.get_height() and mouse_position[1] - return_button.position[1] >= 0):           
                    return False
                
    return True  # Keep the player in the pause menu until they choose to start



def handle_input_for_menu(main_menu_assets):
    start_game_button = main_menu_assets['start_game_button']
    quit_button = main_menu_assets['quit_button']

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Enter key to start the game
                return False  # Exit the main menu and start the game
            elif event.key == pygame.K_q:  # 'Q' to quit the game
                pygame.quit()
                quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if event.button == 1:
                if (mouse_position[0] - start_game_button.position[0] <=  start_game_button.surface.get_width() and mouse_position[0] - start_game_button.position[0] >= 0) and (mouse_position[1] - start_game_button.position[1] <=  start_game_button.surface.get_height() and mouse_position[1] - start_game_button.position[1] >= 0):           
                    return False
                
    return True  # Keep the player in the main menu until they choose to start


def player_movements(player,camera,background,keys):
    a = keys[pygame.K_a]
    w = keys[pygame.K_w]
    s = keys[pygame.K_s]
    d = keys[pygame.K_d]
    space = keys[pygame.K_SPACE]

    if w and not (a or d or s):
        player.last_key_pressed = 'w'
    if s and not (w or a or d):
        player.last_key_pressed = 's'
    if a and not (w or s or d):
        player.last_key_pressed = 'a'
    if d and not (w or a or s):
        player.last_key_pressed = 'd'

    if player.last_key_pressed == 'w' and w and  background.position.y <= player.position.y - player.velocity.y:
        if player.position.y - camera.position.y < 0.2 * SCREEN_HEIGHT and  background.position.y <= camera.position.y - player.velocity.y:
            camera.position.y -= player.velocity.y

        player.position.y -= player.velocity.y
        player.frame += 1 / 5 * player.velocity.y / 10
        player.image = char['climbingFrames'][math.floor(player.frame % len(char['climbingFrames']))]
    
    if player.last_key_pressed == 's' and s and player.position.y + player.velocity.y <= 0:
        if player.position.y - camera.position.y > 0.6 * SCREEN_HEIGHT and camera.position.y + player.velocity.y <= 0:
            camera.position.y += player.velocity.y
            
        player.position.y += player.velocity.y
        player.frame += 1 / 5 * player.velocity.y / 10
        player.image = char['climbingFrames'][math.floor(player.frame % len(char['movingLeftFrames']))]
    
    if player.last_key_pressed == 'a' and a and player.position.x - player.velocity.x >= 0:
        if player.position.x - camera.position.x < 0.1 * SCREEN_WIDTH and camera.position.x - player.velocity.x >= 0:
            camera.position.x -= player.velocity.x

        player.position.x -= player.velocity.x
        player.frame += 1 / 5 * player.velocity.x / 10
        player.image = char['movingLeftFrames'][math.floor(player.frame % len(char['movingLeftFrames']))]
    
    if player.last_key_pressed == 'd' and d and player.position.x + player.image.get_width()+ player.velocity.x <= background.image.get_width():
        if player.position.x - camera.position.x > 0.6 * SCREEN_WIDTH and camera.position.x +4*player.image.get_width() + player.velocity.x <= background.image.get_width():
            camera.position.x += player.velocity.x

        player.position.x += player.velocity.x
        player.frame += 1 / 5 * player.velocity.x / 10
        player.image = char['movingRightFrames'][math.floor(player.frame % len(char['movingLeftFrames']))]

    player.rect.x = player.position.x
    player.rect.y = player.position.y 


def handle_input(player, camera, background, is_paused):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        is_paused = not is_paused
        pygame.time.wait(300)

    if not is_paused:
        player_movements(player,camera,background,keys)
    

    return is_paused
