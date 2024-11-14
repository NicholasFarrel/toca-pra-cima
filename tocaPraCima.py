import pygame
from scenes.game_scene import GameScene
from game_objects.player import Boy, Girl
from game_objects.powerup import Magnesio
from game_objects import birds, obstacles
from mechanics.stamina import StaminaBar
from config import Config 
from scenes.button import Button
import sys

pygame.init()

# Set up the display screen with the given width and height from Config
screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))

running = True

def getFont(size):
    """
    Return a Pygame font object with the specified size.

    Args:
        size (int): The font size.

    Returns:
        pygame.font.Font: The font object.
    """
    return pygame.font.Font('sprites/menu/font.ttf', size)


def pause():
    """
    Display the pause menu when the game is paused.
    It allows the player to resume the game or quit.
    """
    global running

    backgroundColor = (255,255,255)
    surface = pygame.Surface((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
    surface.fill(backgroundColor)
    surface.set_alpha(120)  # Set transparency for the pause overlay

    # Define the "Play" button for resuming the game
    playButton = Button(
        image = pygame.transform.scale(
            pygame.image.load('sprites/menu/playButton.png'),
            (300, 300)
        ),
        position=(Config.SCREEN_WIDTH//2, Config.SCREEN_HEIGHT//2),
        textInput='play',
        font=getFont(10), 
        baseColor=(0, 0, 100),
        hoveringColor=(0, 100, 0)
    )

    screen.blit(surface, (0, 0))  # Render the pause screen
    while running:
        mousePosition = pygame.mouse.get_pos()  # Get the mouse position

        for button in [playButton]:
            button.changeColor(mousePosition)  # Change button color on hover
            button.update(screen)  # Update button state
        
        # Event handling for quitting or resuming the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Resume the game if ESC is pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.checkForInput(mousePosition):  # Resume game when play button is clicked
                    return

        pygame.display.flip()


def game():
    """
    Main game loop. Initializes the game objects, handles the game state,
    updates and draws the scene, and checks for player input.
    """
    global running
    character = Girl(Config.SCREEN_WIDTH // 2, Config.SCREEN_HEIGHT - 100)  # Initialize the player character
    Magnesio.initialize([(200, 150), (400, 300), (600, 450)])  # Initialize powerups (Magnesio)
    game_scene = GameScene(screen, character, Magnesio.magnesio_group)  # Initialize the game scene
    birds.initialize(character)  # Initialize birds (enemies or obstacles)
    stamina_bar = StaminaBar(x=10, y=10, width=200, height=20, max_stamina=character.max_stamina)  # Initialize stamina bar
    clock = pygame.time.Clock()
    obstacles.initialize(character.speed)  # Initialize obstacles

    def update():
        """
        Update and render all game elements.
        """
        game_scene.update()  # Update the game scene
        stamina_bar.update(character.stamina)  # Update the stamina bar
        game_scene.draw()  # Draw the game scene
        character.drawAnimation(screen)  # Draw the player character's animation
        stamina_bar.draw(screen)  # Draw the stamina bar
        birds.update(screen, game_scene.bg_y_offset, character)  # Update and draw birds
        Magnesio.update(character)  # Update and check powerups
        obstacles.update(Config.SCREEN_WIDTH, screen, game_scene.bg_y_offset)  # Update obstacles

    while running:
        update()  # Update game objects
        # Event handling (e.g., quitting or pausing the game)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pause()  # Pause the game if ESC is pressed

        pygame.display.flip()  # Refresh the screen
        clock.tick(60)  # Limit the frame rate to 60 FPS


def main_menu():
    """
    Display the main menu. This menu lets the player start the game or quit.
    """
    global running
    backgroundImage = pygame.transform.scale(
        pygame.image.load('sprites/menu/Background.png'),
        (Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT)
    )

    # Define the "Play" button in the main menu
    playButton = Button(
        image = pygame.transform.scale(
            pygame.image.load('sprites/menu/button.png'),
            (300, 100)
        ),
        position=(Config.SCREEN_WIDTH//2, Config.SCREEN_HEIGHT//2),
        textInput='play',
        font=getFont(10), 
        baseColor=(0, 0, 100),
        hoveringColor=(0, 100, 0)
    )

    while running:
        screen.blit(backgroundImage, (0, 0))  # Render the background image
        mousePosition = pygame.mouse.get_pos()  # Get the mouse position

        for button in [playButton]:
            button.changeColor(mousePosition)  # Change button color on hover
            button.update(screen)  # Update button state
        
        # Event handling for quitting or starting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Quit the game if the window is closed
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.checkForInput(mousePosition):  # Start the game when the play button is clicked
                    game()

        pygame.display.flip()  # Refresh the screen


# Start the main menu loop
main_menu()
