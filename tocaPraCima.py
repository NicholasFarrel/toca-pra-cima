import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo de Escalada 2D")

# Configurações do personagem
character_size = 50
character_x = SCREEN_WIDTH // 2 - character_size // 2
character_y = SCREEN_HEIGHT - character_size
character_speed = 5

# Configurações do cenário
background_y = 0
background_speed = 2  # velocidade do movimento do cenário

# Loop principal do jogo
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controles do personagem usando W, A, S, D ou setas
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and character_x > 0:  # Esquerda
        character_x -= character_speed
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and character_x < SCREEN_WIDTH - character_size:  # Direita
        character_x += character_speed
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and character_y < SCREEN_HEIGHT - character_size:  # Baixo
        character_y += character_speed
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and character_y > SCREEN_HEIGHT * 0.2:  # Cima (com limite)
        character_y -= character_speed
    elif (keys[pygame.K_w] or keys[pygame.K_UP]) and character_y <= SCREEN_HEIGHT * 0.2:
        background_y += background_speed  # Move o cenário para cima

    # Desenho do cenário e do personagem
    screen.fill((135, 206, 235))  # Cor do fundo
    pygame.draw.rect(screen, (0, 128, 0), (character_x, character_y, character_size, character_size))

    pygame.display.flip()
    clock.tick(30)
