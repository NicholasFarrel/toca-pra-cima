import pygame
import os
import sys
# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_dir)
from config import Config

class GameScene:
    """Manages the game scene, including the background scrolling effect and positioning of magnesium power-ups."""

    def __init__(self, screen, character, magnesio_group):
        """
        Initializes the game scene with the background, character, and magnesium power-ups.

        Args:
            screen (pygame.Surface): The game screen surface to draw onto.
            character (Character): The main character in the game.
            magnesio_group (pygame.sprite.Group): Group containing magnesium power-up sprites.
        """

        # Load and set the background image
        self.background = pygame.image.load("sprites/backgrounds/level_0.png").convert()
        zoomFactor = 5
        newWidth = int(self.background.get_width() * zoomFactor)
        newHeight = int(self.background.get_height() * zoomFactor)
        self.bg_x_offset = (Config.SCREEN_WIDTH - newWidth) // 2
        self.bg_y = (Config.SCREEN_HEIGHT - newHeight) // 2
        self.background = pygame.transform.scale(self.background, (newWidth, newHeight))
        self.background_width, self.background_height = self.background.get_size()

        # Store references to screen, character, and magnesium group
        self.screen = screen
        self.character = character
        self.magnesio_group = magnesio_group

        # Initial background positions to start at the bottom-left of the screen
        #self.bg_x_offset = 0
        self.bg_y_offset = -(self.background_height - screen.get_height())


    def update(self):
        """
        Updates the position of the background and character based on input.
        """
        keys = pygame.key.get_pressed()
        a = keys[pygame.K_a]
        w = keys[pygame.K_w]
        s = keys[pygame.K_s]
        d = keys[pygame.K_d]

        # Vertical boundaries for the character to start moving the background
        upper_limit = self.screen.get_height() * 0.4
        lower_limit = self.screen.get_height() * 0.6

        # Horizontal boundaries for the character to start moving the background
        left_limit = self.screen.get_width() * 0.4
        right_limit = self.screen.get_width() * 0.6

        # Background scrolls down if the character reaches the upper limit and 'move_up' is True
        if w and self.character.rect.y <= upper_limit and not (s or d or a):
            self.bg_y_offset += self.character.velocity.y
            for magnesio in self.magnesio_group:
                magnesio.rect.y += self.character.velocity.y

        # Background scrolls up if the character reaches the lower limit and 'move_down' is True
        elif s and self.character.rect.y >= lower_limit:
            self.bg_y_offset -= self.character.velocity.y
            for magnesio in self.magnesio_group:
                magnesio.rect.y -= self.character.velocity.y

        # Background scrolls left if the character reaches the right limit and 'move_right' is True
        if d and self.character.rect.x >= right_limit and not (s or w or a):
            self.bg_x_offset -= self.character.velocity.x
            for magnesio in self.magnesio_group:
                magnesio.rect.x -= self.character.velocity.x

        # Background scrolls right if the character reaches the left limit and 'move_left' is True
        elif a and self.character.rect.x <= left_limit:
            self.bg_x_offset += self.character.velocity.x
            for magnesio in self.magnesio_group:
                magnesio.rect.x += self.character.velocity.x

        # If character is within the central range, it moves without scrolling the background
        if w and self.character.rect.y > upper_limit and not (s or d or a):
            self.character.rect.y -= self.character.velocity.y
        elif s and self.character.rect.y < lower_limit and not (d or w or a):
            self.character.rect.y += self.character.velocity.y

        if a and self.character.rect.x > left_limit and not (s or d or w):
            self.character.rect.x -= self.character.velocity.x
        elif d and self.character.rect.x < right_limit and not (s or w or a):
            self.character.rect.x += self.character.velocity.x

        # Limit background offsets within the image's boundaries
        self.bg_x_offset = min(0, max(self.bg_x_offset, -(self.background_width - self.screen.get_width())))
        self.bg_y_offset = min(0, max(self.bg_y_offset, -(self.background_height - self.screen.get_height())))


    def draw(self):
        """Draws the background with the calculated offsets and the magnesium power-ups."""
        # Draw the background at the current offset position
        self.screen.blit(self.background, (self.bg_x_offset, self.bg_y_offset))
        # Draw all magnesium items
        self.magnesio_group.draw(self.screen)
