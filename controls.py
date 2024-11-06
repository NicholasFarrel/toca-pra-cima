import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import Config
import pygame

def handle_movement(position, character_speed):
    keys = pygame.key.get_pressed()
    # Controles do personagem usando W, A, S, D ou setas
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and position.x > 0:  # Esquerda
        position.x -= character_speed
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and position.x < Config.SCREEN_WIDTH - 50:  # Direita
        position.x += character_speed
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and position.y < Config.SCREEN_HEIGHT - 50:  # Baixo
        position.y += character_speed
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and position.y > Config.SCREEN_HEIGHT * 0.2:  # Cima (com limite)
        position.y -= character_speed

    return position
