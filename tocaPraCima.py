import pygame
from scenes.game_scene import GameScene
from game_objects.player import Boy, Girl
from game_objects.powerup import Magnesio
from game_objects import birds
from mechanics.stamina import StaminaBar
from scenes.pause import Menu

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Toca pra Cima")

# Initialize other game modules
character = Girl(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
Magnesio.initialize([(200, 150), (400, 300), (600, 450)])
menu = Menu()
game_scene = GameScene(screen, character, Magnesio.magnesio_group)
birds.initialize(character)
stamina_bar = StaminaBar(x=10, y=10, width=200, height=20, max_stamina=character.max_stamina)

# Main game loop
clock = pygame.time.Clock()
running = True
paused = True
time = 0

while running:
    
    keys = pygame.key.get_pressed()
    time += 1
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the game loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused
   
    if paused:
        menu.load(screen)
    else:
        game_scene.update()
        stamina_bar.update(character.stamina)
        game_scene.draw()
        character.drawAnimation(screen)
        stamina_bar.draw(screen)  # Draw the stamina bar on top of the scene
        birds.update(screen, game_scene.bg_y_offset, character)
        Magnesio.update(character)
    
    pygame.display.flip()  # Refresh the display
    clock.tick(60)  # Keep the game running at 60 FPS

pygame.quit()
