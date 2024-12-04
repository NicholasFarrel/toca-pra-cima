import pygame

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GRAVITY = 10
GRAVITY_FORCE = pygame.Vector2(0,GRAVITY)

colors ={
    'WHITE' : (255,255,255),
    'BLACK' : (0,0,0),
    'BLUE' : (0,0,255),
    'RED' : (255,0,0),
    'YELLOW' : (117, 95, 5),
}

char = {
    'image_path' : {
            'climbingImage' : 'assets/sprites/player/climbingImage.png',
            'movingLeftImage' : 'assets/sprites/player/movingLeftImage.png',
            'movingRightImage' : 'assets/sprites/player/movingRightImage.png',
            'jumpingImage' : 'assets/sprites/player/jumpingImage.png'
        },
    'original_frame_dimension' : (500,500),
    'size' : 100,
}
char['scaled_frame_dimension'] = (1.5*char['size'], 1.5*char['size'])

background = {
    'image_path' : 'assets/sprites/background/Level.png',
    'scaled_dimension' : 1,
}



