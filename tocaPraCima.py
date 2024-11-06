import pygame

from scenes.game_scene import GameScene
from game_objects.player import Boy, Girl
from game_objects.powerup import Magnesio
from game_objects import obstacles
from mechanics.stamina import StaminaBar


# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Toca pra Cima")

# Instantiate the character (Boy or Girl in this case)
character = Girl(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)

# Initialize clouds 
obstacles.initialize(character.speed)

# Create magnesium power-ups at fixed positions and add them to the group
magnesio_positions = [(200, 150), (400, 300), (600, 450)]
magnesio_group = pygame.sprite.Group()
for pos in magnesio_positions:
    magnesio = Magnesio(*pos)
    magnesio_group.add(magnesio)

# Instantiate the game scene
game_scene = GameScene(screen, character, magnesio_group)

# Instantiate the stamina bar
stamina_bar = StaminaBar(x=10, y=10, width=200, height=20, max_stamina=character.max_stamina)

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    # Movement flags initialized to False at the start of each frame
    move_up = move_down = move_left = move_right = False

    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the game loop

    # Capture movement inputs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        move_up = True
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        move_down = True
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        move_left = True
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        move_right = True

    # Update the game scene based on movement inputs
    game_scene.update(move_up, move_down, move_left, move_right)

    # Check collisions with magnesium power-ups and apply stamina effect
    collected_magnesios = pygame.sprite.spritecollide(character, magnesio_group, True)
    for magnesio in collected_magnesios:
        magnesio.apply_effect(character)  # Restore the character's stamina

    # Update the stamina bar
    stamina_bar.update(character.stamina)

    # Draw the scene, character, and stamina bar
    game_scene.draw()
    character.draw(screen)
    stamina_bar.draw(screen)  # Draw the stamina bar on top of the scene

    obstacles.update(SCREEN_WIDTH, SCREEN_HEIGHT, screen, game_scene.bg_y_offset)

    pygame.display.flip()  # Refresh the display
    clock.tick(60)  # Keep the game running at 60 FPS



pygame.quit()

