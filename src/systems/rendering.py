import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pygame
import math
from src.game.settings import *
from src.game.constants import *


def render_main_menu(screen, menu):
    title = menu['title']
    title2 = menu['title2']
    title3 = menu['title3']
    start_game_button = menu['start_game_button']
    quit_button = menu['quit_button']
    background = menu['background']

    screen.fill(background.color)
    screen.blit(background.image, background)
    screen.blit(title.surface, title.position)
    screen.blit(title2.surface, title2.position)
    screen.blit(title3.surface, title3.position)
    screen.blit(start_game_button.surface, start_game_button.position)
    screen.blit(quit_button.surface, quit_button.position)


def render_pause_menu(screen, pause_menu_assets):
    pause_title = pause_menu_assets['pause_title']
    return_button = pause_menu_assets['return_button']
    pause_title2 = pause_menu_assets['pause_title2']
    pause_background = pause_menu_assets['pause_background']
    
    screen.fill(pause_background['color'])
    screen.blit(pause_title.surface, pause_title.position)
    screen.blit(return_button.surface, return_button.position)
    

def render_scene(screen,camera, player, background):
    screen.fill(BLACK)
    background.rect = pygame.Rect(background.position.x, background.position.y, background.image.get_width(),background.image.get_height())
    
    player.rect.topleft -= camera.position
    background.rect.topleft -= camera.position

    screen.blit(background.image, background.rect)

    imageRect = player.rect.copy()
    imageRect.x -= player.size/4
    

    screen.blit(player.image, imageRect)
    #pygame.draw.rect(screen, BLACK, player.rect, 2)

    player.rect.topleft = player.position
    background.rect.topleft = background.position


def load_image(imagePath, dimension):
    """
    Load an image from the given path and scale it to the specified dimensions.

    Args:
        imagePath (str): Path to the image file.
        dimension (tuple): Desired dimensions (width, height) for the image.

    Returns:
        pygame.Surface: The loaded and scaled image.
    """
    image = pygame.image.load(imagePath).convert_alpha()  # Load image with transparency
    image = pygame.transform.scale(image, dimension)  # Scale image to given dimensions
    return image


def draw_bird_animation(bird, screen, camera):
        """
        Draw the bird's animation on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the animation on.
        """
        bird.rect.topleft -= camera.position
        screen.blit(bird.frames[math.floor(bird.frame % len(bird.frames))], bird.rect.center)
        bird.frame += 1/5 * bird.maxVelocity/10  # Adjust frame speed based on velocity
        bird.rect.topleft = bird.position


def render_poop(poop, screen, camera):
    """
        Render the poop on the screen.

        Args:
            screen (pygame.Surface): The surface to render the poop on.
    """
    poop.rect.topleft -= camera.position
    screen.blit(poop.image, poop.rect.center)
    poop.rect.topleft = poop.position


def render_vulture(vulture, screen, camera):
        """
        Render the vulture on the screen.

        Args:
            screen (pygame.Surface): The screen to render the vulture on.
        """
        vulture.rect.topleft -= camera.position
        #pygame.draw.rect(screen, WHITE, vulture.rect,2)
        screen.blit(vulture.rotatedImage, vulture.rect)
        vulture.frame += 1 / 5 * vulture.velocity.length() / 10
        vulture.rect.topleft = vulture.position


def render_feathers(feathers, screen, camera):
    for feather in feathers:
        feather.rect.center = feather.position 
        feather.rect.topleft -= camera.position
        #pygame.draw.rect(screen, feather.color, feather.rect)
        screen.blit(feather.image, feather.rect)