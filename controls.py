import pygame

def handle_movement(keys, character_x, character_y, character_speed, screen_width, screen_height):
    # Controles do personagem usando W, A, S, D ou setas
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and character_x > 0:  # Esquerda
        character_x -= character_speed
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and character_x < screen_width - 50:  # Direita
        character_x += character_speed
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and character_y < screen_height - 50:  # Baixo
        character_y += character_speed
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and character_y > screen_height * 0.2:  # Cima (com limite)
        character_y -= character_speed

    return character_x, character_y
