import pygame
import random

# Background Y position offset
backgroundY = 0
# Player speed, to control vertical movement
playerSpeed = 0

class Cloud:
    """
    Represents a cloud object that moves horizontally across the screen.
    
    Attributes:
        size (tuple): Width and height of the cloud.
        position (pygame.Vector2): Position of the cloud on the screen.
        speed (int): Horizontal speed of the cloud.
        daughter (bool): Indicates if the cloud has spawned another cloud.
        image (pygame.Surface): The cloud image to render.
        rect (pygame.Rect): The cloud's rectangular area, used for collision and positioning.
    """
    
    def __init__(self, range):
        """
        Initializes a Cloud instance with random size, position, and speed.
        
        Args:
            range (list): Range of y-coordinates for cloud placement.
        """
        # Size of the cloud with random width and height within specified ranges
        self.size = (random.randint(450, 550), random.randint(150, 250))
        # Cloud's initial position, off the screen to the left
        self.position = pygame.Vector2(-1.5 * self.size[0] - 10, random.randint(range[0], range[1]))
        # Horizontal speed of the cloud
        self.speed = random.randint(1, 2)
        
        # Indicates if the cloud has already spawned a "daughter" cloud
        self.daughter = False

        # Load and transform the cloud image
        self.image = pygame.image.load('sprites/obstacles/cloud.png')
        self.image = pygame.transform.scale(self.image, self.size)
        self.image = pygame.transform.rotate(self.image, random.randint(-10, 10))
        
    def render(self, screen):
        """
        Draws the cloud image on the screen at its current position.
        
        Args:
            screen (pygame.Surface): The game screen to render the cloud on.
        """
        # Draw the cloud image on the screen at its current position
        screen.blit(self.image, self.rect.center)

    @staticmethod
    def initialize(speed):
        """
        Sets the player speed globally, controlling the cloud's vertical movement.
        
        Args:
            speed (int): Speed of the player.
        """
        global playerSpeed
        playerSpeed = speed
       
    def move(self, dy):
        """
        Moves the cloud horizontally based on its speed and vertically if dy matches player speed.
        
        Args:
            dy (int): Change in the y-coordinate to apply to the cloud.
        """
        if abs(dy) == playerSpeed:
            self.position.y += dy
        self.position.x += self.speed
        self.rect = pygame.Rect(*self.position, *self.size)
        
    def check_screen(self, screen_width):
        """
        Checks if the cloud has moved off the right side of the screen.
        
        Args:
            screen_width (int): Width of the game screen.
        
        Returns:
            bool: True if the cloud has moved off screen, False otherwise.
        """
        return self.position.x > screen_width
        
    def touch_screen(self, screen_width):
        """
        Checks if the cloud has touched the right side of the screen.
        
        Args:
            screen_width (int): Width of the game screen.
        
        Returns:
            bool: True if the cloud is near the right edge, False otherwise.
        """
        return self.position.x > (screen_width - 2 * self.size[0])
       
range = [[-10240, 80]]
# Adjusts initial range if there are fewer than 6 values
for value in range:
    if len(range) < 6:
        x = value[1] - 2032
        range.append([-10240, x])

clouds = []

def initialize(speed):
    """
    Initializes the player speed and creates empty cloud lists for each range.
    
    Args:
        speed (int): Speed of the player.
    """
    global playerSpeed
    playerSpeed = speed

    global clouds
    for position in range:
        clouds.append([])

def update(screen_width, screen, bg_y_offset):
    """
    Updates cloud positions, adds new clouds, and renders them on the screen.
    
    Args:
        screen_width (int): Width of the game screen.
        screen (pygame.Surface): The game screen to render the clouds on.
        bg_y_offset (int): Current vertical offset of the background.
    """
    global range, backgroundY

    dy = bg_y_offset - backgroundY
    backgroundY = bg_y_offset

    for i, position in enumerate(range):
        # Move clouds vertically if dy matches player speed
        if abs(dy) == playerSpeed:
            position[0] += dy
            position[1] += dy
    
        # Add a new cloud if there are fewer than 8 in the current position
        if len(clouds[i]) < 8:
            c = Cloud(position)
            clouds[i].append(c)
        
        # Remove clouds that have moved off the screen
        clouds[i][:] = [c for c in clouds[i] if not c.check_screen(screen_width)]
        
        for c in clouds[i]:
            c.move(dy)
            c.render(screen)
            # Spawn a new cloud if the current one is near the right edge and hasn't spawned another cloud
            if c.touch_screen(screen_width) and not c.daughter:
                c2 = Cloud(position)
                clouds[i].append(c2)
                c.daughter = True
