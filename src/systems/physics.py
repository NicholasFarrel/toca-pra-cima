import pygame
from src.game.constants import *

def check_vulture_corners(vulture, screen_width, screen_height):
        """
        Check if the vulture has moved off the screen vertically.

        Args:
            screen_width (int): The width of the game screen.
            screen_height (int): The height of the game screen.

        Returns:
            bool: True if the vulture is off the screen, False otherwise.
        """
        if vulture.position.y < 0 or vulture.position.y > screen_height:
            return True
        return False


def apply_gravity(object):
    object.velocity += GRAVITY_FORCE*0.001

