import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pygame
import math
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


def draw_bird_animation(bird, screen):
        """
        Draw the bird's animation on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the animation on.
        """
        screen.blit(bird.frames[math.floor(bird.frame % len(bird.frames))], bird.rect.center)
        bird.frame += 1/5 * bird.maxVelocity/10  # Adjust frame speed based on velocity


def render_poop(poop, screen):
    """
        Render the poop on the screen.

        Args:
            screen (pygame.Surface): The surface to render the poop on.
    """
    screen.blit(poop.image, poop.rect.center)
    # pygame.draw.rect(screen, self.color, self.rect)  # Optional: draw the rectangle

def render_vulture(vulture, screen):
        """
        Render the vulture on the screen.

        Args:
            screen (pygame.Surface): The screen to render the vulture on.
        """
       
        screen.blit(vulture.rotatedImage, vulture.rect.center)
        vulture.frame += 1 / 5 * vulture.velocity.length() / 10