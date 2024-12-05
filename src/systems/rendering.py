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


def render_game_over_menu(screen, menu):
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
    

def render_scene(screen,camera, player, background, magnesios):
    screen.fill(BLACK)
    background.rect = pygame.Rect(background.position.x, background.position.y, background.image.get_width(),background.image.get_height())
    
    player.rect.topleft -= camera.position
    background.rect.topleft -= camera.position

    screen.blit(background.image, background.rect)
    for magnesio in magnesios:
        magnesio.update(screen,player, camera)
        magnesio.rect.topleft -= camera.position
        #pygame.draw.rect(screen, BLACK, magnesio.rect, 2)
        render_magnesio(magnesio, screen,camera)

    imageRect = player.rect.copy()
    imageRect.x -= player.size/4
    

    draw_health_bar(screen, 50, 50, player.life, 10, 300, 30)  # Barra de vida
    screen.blit(player.image, imageRect)
    #pygame.draw.rect(screen, BLACK, player.rect, 2)

    player.rect.topleft = player.position
    background.rect.topleft = background.position


def render_magnesio(magnesio, screen, camera):
    magnesio.rect.topleft += camera.position
    #pygame.draw.rect(screen, WHITE, magnesio.rect, 2) 
    screen.blit(magnesio.image, (magnesio.rect.x - camera.position.x, magnesio.rect.y - camera.position.y))



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


def render_win(screen, images):
    global last_update_time, frame_index
    current_time = pygame.time.get_ticks()
    if current_time - last_update_time > frame_duration:
        frame_index = (frame_index + 1) % len(images)  # Loop back to the first image
        last_update_time = current_time

    # Draw the current frame
    screen.fill((0, 0, 0))  # Clear screen with black
    screen.blit(images[frame_index], (0, 0))  # Display the current frame
    pygame.display.flip()


def draw_health_bar(surface, x, y, current_life, max_life, width, height):
    # Cores
    background_color = (50, 50, 50)  # Cor de fundo da barra
    health_color = (0, 200, 0)  # Cor da vida (verde)
    border_color = (255, 255, 255)  # Cor da borda

    # Calcular a largura proporcional à vida atual
    health_width = (current_life / max_life) * width

    # Desenhar o fundo da barra
    pygame.draw.rect(surface, background_color, (x, y, width, height))

    # Desenhar a barra de vida
    pygame.draw.rect(surface, health_color, (x, y, health_width, height))

    # Desenhar a borda
    pygame.draw.rect(surface, border_color, (x, y, width, height), 2)
