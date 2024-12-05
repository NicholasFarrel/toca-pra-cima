import pygame

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GRAVITY = 10
GRAVITY_FORCE = pygame.Vector2(0,GRAVITY)

max_life = 10
max_birds = 15
max_feathers = 5
bird_life = 1
damage_length = 100
life = 3
num_magnesios = 100

last_update_time = pygame.time.get_ticks()
frame_index = 0
frame_rate = 10  # Frames per second (adjust as needed)
frame_duration = 2000 // frame_rate  # Duration of each frame in milliseconds


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
    'original_frame_dimension' : (256,256),
    'size' : 100,
}
char['scaled_frame_dimension'] = (1.5*char['size'], 1.5*char['size'])

background = {
    'image_path' : 'assets/sprites/background/Level.png',
    'scaled_dimension' : 2,
}



