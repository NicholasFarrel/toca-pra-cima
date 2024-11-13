import pygame
from scenes.game_scene import GameScene
from game_objects.player import Boy, Girl
from game_objects.powerup import Magnesio
from game_objects import birds
from mechanics.stamina import StaminaBar
from scenes.pause import Menu
from config import Config 
from scenes.main_menu import MainMenu
from scenes.button import Button
import sys

pygame.init()

screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
mainMenu = MainMenu()

running = True

def getFont(size):
    return pygame.font.Font('sprites/menu/font.ttf', size)


def pause():
    global running

    backgroundColor = (255,255,255)
    #self.color = (0,0,0)
    surface = pygame.Surface((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
    surface.fill(backgroundColor)
    surface.set_alpha(120)
    
    screen.blit(surface, (0,0))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        

        pygame.display.flip()
        

def game():
    global running
    # Screen settings

    # Initialize other game modules
    character = Girl(Config.SCREEN_WIDTH // 2, Config.SCREEN_HEIGHT - 100)
    Magnesio.initialize([(200, 150), (400, 300), (600, 450)])
    menu = Menu()
    game_scene = GameScene(screen, character, Magnesio.magnesio_group)
    birds.initialize(character)
    stamina_bar = StaminaBar(x=10, y=10, width=200, height=20, max_stamina=character.max_stamina)

    # Main game loop
    clock = pygame.time.Clock()
    paused = False


    def update():
        game_scene.update()
        stamina_bar.update(character.stamina)
        game_scene.draw()
        character.drawAnimation(screen)
        stamina_bar.draw(screen)  # Draw the stamina bar on top of the scene
        birds.update(screen, game_scene.bg_y_offset, character)
        Magnesio.update(character)
        

    while running:
        update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the game loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()
    
        pygame.display.flip()  # Refresh the display
        clock.tick(60)  # Keep the game running at 60 

    pygame.quit()


def main_menu():
    global running
    backgroundImage = pygame.image.load('sprites/menu/Background.png')
    
    playButton =  Button(
        image = pygame.transform.scale(pygame.image.load('sprites/menu/button.png'),(300,100)),
        position=(Config.SCREEN_WIDTH//2,Config.SCREEN_HEIGHT//2),
        textInput='play',
        font=getFont(10), baseColor = (0,0,100),
        hoveringColor=(0,100,0)
        )
    
    while running:
        screen.blit(backgroundImage, (0,0))
        mousePosition = pygame.mouse.get_pos()

        for button in [playButton]:
            button.changeColor(mousePosition)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.checkForInput(mousePosition):
                    game()

        pygame.display.flip()


main_menu()
