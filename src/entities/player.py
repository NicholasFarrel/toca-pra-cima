import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.game.constants import char

import pygame

class Character:
    """
    Represents a base character in the game, handling position, movement speed, and stamina.

    Attributes:
        rect (pygame.Rect): Defines the position and size of the character.
        speed (int): The movement speed of the character.
        max_stamina (int): The maximum stamina value for the character.
        stamina (int): The current stamina value, initialized below maximum for testing.
    """

    def __init__(self, x, y, speed, max_stamina, size): 
        """
        Initializes the character with position, speed, and stamina values.

        Args:
            x (int): The x-coordinate of the top-left corner of the character.
            y (int): The y-coordinate of the top-left corner of the character.
            speed (int): The movement speed of the character.
            max_stamina (int): The maximum stamina value for the character.
        """
        self.life = 3
        self.size = size
        self.rect = pygame.Rect(x , y, size, size)
        self.velocity = pygame.Vector2(speed,speed)
        self.max_stamina = max_stamina
        self.original_frame_dimension = (500,500)
        self.scaled_frame_dimension = (1.5*size, 1.5*size)
        self.position = pygame.Vector2(x,y)
        self.frame = 0
        self.time = 0
        self.image = char['climbingFrames'][0]
        self.jumpFrame = 0
        self.damage = 0
        self.last_key_pressed = None


class Girl(Character):
    """
    Represents the 'Girl' character with unique image, speed, and stamina values.
    Inherits from Character.
    """


    def __init__(self, x, y):
        """
        Initializes the 'Girl' character with a specific image, speed, and max stamina.

        Args:
            x (int): The x-coordinate of the top-left corner of the girl character.
            y (int): The y-coordinate of the top-left corner of the girl character.
        """
        super().__init__(x, y, speed=10, max_stamina=800, size = char['size'])
        
    