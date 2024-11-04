import pygame
import sys
from controls import handle_movement  # Importação da função de controle
from game_objects import powerup  # Importação das novas classes
from game_objects import birds
from game_objects import player
from config import Config

# Inicialização do Pygame
pygame.init()

# Configurações da tela
screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
pygame.display.set_caption("Toca pra Cima")

# Carregar a textura do cenário
background_texture = pygame.image.load("sprites/mountain_texture.jpg").convert()
texture_width, texture_height = background_texture.get_size()

# Configurações do personagem
character_size = 50
character_x = Config.SCREEN_WIDTH // 2 - character_size // 2
character_y = Config.SCREEN_HEIGHT - character_size
character_speed = 5

# Configurações do cenário
background_y = 0
background_speed = 2  # velocidade do movimento do cenário

# Lista de posições estratégicas para os sacos de magnésio
strategic_positions = [
    (200, -100), (400, -300), (100, -500), (700, -700), (300, -900),
    (500, -1100), (150, -1300), (650, -1500), (250, -1700), (550, -1900)
]

# Criar grupo de sprites e instância da barra de magnésio
magnesio_group = pygame.sprite.Group()
for pos in strategic_positions:
    magnesio = powerup.Magnesio(Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT)
    magnesio.rect.x, magnesio.rect.y = pos  # Posiciona em locais estratégicos
    magnesio_group.add(magnesio)

magnesio_bar = powerup.MagnesioBar(max_magnesio=10)  # Barra de magnésio com capacidade máxima de 10 unidades

# Loop principal do jogo
clock = pygame.time.Clock()
running = True
boy = player.Boy(50, 5)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Processar a movimentação do personagem usando controles externos
    keys = pygame.key.get_pressed()

    # Atualizar posição do cenário e dos sacos de magnésio
    if keys[pygame.K_w] or keys[pygame.K_UP]:  # Move o cenário e os sacos de magnésio para baixo
        if boy.position.y <= Config.SCREEN_HEIGHT * 0.2:
            background_y += background_speed
            for magnesio in magnesio_group:
                magnesio.rect.y += background_speed  # Mover o magnésio conforme o fundo se move

    # Verificar colisão do personagem com os sacos de magnésio
    for magnesio in magnesio_group:
        if boy.rect.colliderect(magnesio.rect):
            magnesio_bar.increase_magnesio()
            magnesio_group.remove(magnesio)  # Remover o saco coletado

    # Desenhar o fundo e o personagem
    for y in range(-texture_height, Config.SCREEN_HEIGHT, texture_height):
        screen.blit(background_texture, (0, y + background_y % texture_height))

    # Desenhar os sacos de magnésio
    magnesio_group.draw(screen)

    # Desenhar a barra de magnésio
    magnesio_bar.draw(screen)

    birds.update(screen, Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT, boy.position)
    player.update(screen,boy)

    pygame.display.flip()
    clock.tick(30)
