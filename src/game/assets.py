import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.game.constants import *
import pygame


def createAnimation(rotation = 0):
   
    climbingImage = pygame.image.load(char['image_path']['climbingImage'])
    movingLeftImage = pygame.image.load(char['image_path']['movingLeftImage'])
    movingRightImage = pygame.image.load(char['image_path']['movingRightImage'])
    jumpingImage = pygame.image.load(char['image_path']['jumpingImage'])
    
    climbingFrames = [
        pygame.transform.scale(    
            climbingImage.subsurface(i * char['original_frame_dimension'][0], 0, *char['original_frame_dimension']),
            char['scaled_frame_dimension']
        )
        for i in range(7)
    ]

    movingLeftFrames = [
        pygame.transform.scale(
            movingLeftImage.subsurface(i * char['original_frame_dimension'][0], 0, *char['original_frame_dimension']),
            char['scaled_frame_dimension']
        )
        for i in range(7)
    ]
    
    movingRightFrames = [
        pygame.transform.scale(
            movingRightImage.subsurface(i * char['original_frame_dimension'][0], 0, *char['original_frame_dimension']),
            char['scaled_frame_dimension']
        )
        for i in range(7)
    ]
    
    jumpingFrames = [
        pygame.transform.scale(
            jumpingImage.subsurface(i * char['original_frame_dimension'][0], 0, *char['original_frame_dimension']),
            char['scaled_frame_dimension']
        )
        for i in range(10)
    ]

    return climbingFrames, movingLeftFrames, movingRightFrames, jumpingFrames


def load_game_assets():
    char['climbingFrames'], char['movingLeftFrames'], char['movingRightFrames'], char['jumpingFrames'] = createAnimation()
    
    background['raw_image'] = pygame.image.load(background['image_path'])
    b_dim = background['raw_image'].get_size()
    background['image'] = pygame.transform.scale(
        background['raw_image'],
        (b_dim[0]*background['scaled_dimension'], b_dim[1]* background['scaled_dimension'])
    )
    

    