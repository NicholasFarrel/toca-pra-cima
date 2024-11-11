import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import Config
import pygame

def handle_movement(position, character_speed):
    keys = pygame.key.get_pressed()
    a = keys[pygame.K_a]
    w = keys[pygame.K_w]
    s = keys[pygame.K_s]
    d = keys[pygame.K_d]
    # Controles do personagem usando W, A, S, D ou setas
    if a and not (w or s or d) and position.x > 0:  # Esquerda
        print("esquerda")
        position.x -= character_speed
    if d and not (w or a or s) and position.x < Config.SCREEN_WIDTH - 50:  # Direita
        position.x += character_speed
    if s and not (w or a or d) and position.y < Config.SCREEN_HEIGHT - 50:  # Baixo
        position.y += character_speed
    if w and not (a or d or s) and position.y > Config.SCREEN_HEIGHT * 0.2:  # Cima (com limite)
        print("cima")
        position.y -= character_speed

    return position
