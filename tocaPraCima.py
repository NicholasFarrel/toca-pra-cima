import pygame
from scenes.game_scene import GameScene
from game_objects.player import Boy, Girl
from game_objects.powerup import Magnesio
from game_objects import birds
from mechanics.stamina import StaminaBar
from config import Config 
from scenes.button import Button
import sys

pygame.init()

screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))

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

    playButton =  Button(
        image = pygame.transform.scale(
            pygame.image.load('sprites/menu/playButton.png'),
            (300,300)
            ),
        position=(Config.SCREEN_WIDTH//2,Config.SCREEN_HEIGHT//2),
        textInput='play',
        font=getFont(10), baseColor = (0,0,100),
        hoveringColor=(0,100,0)
        )
    screen.blit(surface, (0,0))
    while running:
        mousePosition = pygame.mouse.get_pos()

        for button in [playButton]:
            button.changeColor(mousePosition)
            button.update(screen)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.checkForInput(mousePosition):
                    return

        pygame.display.flip()
        

def game():
    global running
    character = Girl(Config.SCREEN_WIDTH // 2, Config.SCREEN_HEIGHT - 100)
    Magnesio.initialize([(200, 150), (400, 300), (600, 450)])
    game_scene = GameScene(screen, character, Magnesio.magnesio_group)
    birds.initialize(character)
    stamina_bar = StaminaBar(x=10, y=10, width=200, height=20, max_stamina=character.max_stamina)
    clock = pygame.time.Clock()

    def update():
        game_scene.update()
        stamina_bar.update(character.stamina)
        game_scene.draw()
        character.drawAnimation(screen)
        stamina_bar.draw(screen)
        birds.update(screen, game_scene.bg_y_offset, character)
        Magnesio.update(character)

    while running:
        update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pause()
    
        pygame.display.flip()
        clock.tick(60)

def main_menu():
    global running
    backgroundImage = pygame.transform.scale(
        pygame.image.load('sprites/menu/Background.png'),
        (Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT)
        )
    
    playButton =  Button(
        image = pygame.transform.scale(
            pygame.image.load('sprites/menu/button.png'),
            (300,100)
            ),
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
