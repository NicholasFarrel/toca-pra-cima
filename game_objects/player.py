import pygame
import math


def createAnimation(entity, rotation = 0):
    climbingImage = pygame.image.load(entity.imagePath['climbingImage'])
    movingLeftImage = pygame.image.load(entity.imagePath['movingLeftImage'])
    movingRightImage = pygame.image.load(entity.imagePath['movingRightImage'])
    jumpingImage = pygame.image.load(entity.imagePath['jumpingImage'])
    
    climbingFrames = [
        pygame.transform.scale(    
            climbingImage.subsurface(i * entity.original_frame_dimension[0], 0, *entity.original_frame_dimension),
            entity.scaled_frame_dimension
        )
        for i in range(7)
    ]

    movingLeftFrames = [
        pygame.transform.scale(
            movingLeftImage.subsurface(i * entity.original_frame_dimension[0], 0, *entity.original_frame_dimension),
            entity.scaled_frame_dimension
        )
        for i in range(7)
    ]
    
    movingRightFrames = [
        pygame.transform.scale(
            movingRightImage.subsurface(i * entity.original_frame_dimension[0], 0, *entity.original_frame_dimension),
            entity.scaled_frame_dimension
        )
        for i in range(7)
    ]
    
    jumpingFrames = [
        pygame.transform.scale(
            jumpingImage.subsurface(i * entity.original_frame_dimension[0], 0, *entity.original_frame_dimension),
            entity.scaled_frame_dimension
        )
        for i in range(10)
    ]

    return climbingFrames, movingLeftFrames, movingRightFrames, jumpingFrames


class Character:
    """
    Represents a base character in the game, handling position, movement speed, and stamina.

    Attributes:
        rect (pygame.Rect): Defines the position and size of the character.
        speed (int): The movement speed of the character.
        max_stamina (int): The maximum stamina value for the character.
        stamina (int): The current stamina value, initialized below maximum for testing.
    """


    def __init__(self, x, y, speed, max_stamina):
        """
        Initializes the character with position, speed, and stamina values.

        Args:
            x (int): The x-coordinate of the top-left corner of the character.
            y (int): The y-coordinate of the top-left corner of the character.
            speed (int): The movement speed of the character.
            max_stamina (int): The maximum stamina value for the character.
        """
        # Define the character's position and size
        self.rect = pygame.Rect(x, y, 120, 120)
        # Initialize speed and stamina values
        self.speed = speed
        self.max_stamina = max_stamina
        self.stamina = max_stamina - 60  # Initialize stamina for testing purposes
        self.original_frame_dimension = (500,500)
        self.scaled_frame_dimension = (150,150)
        self.position = pygame.Vector2(x,y)
        self.imagePath = {
            'climbingImage' : 'sprites/characters/climbingImage.png',
            'movingLeftImage' : 'sprites/characters/movingLeftImage.png',
            'movingRightImage' : 'sprites/characters/movingRightImage.png',
            'jumpingImage' : 'sprites/characters/jumpingImage.png'
        }
        #'sprites/characters/char.png'
        self.climbingFrames, self.movingLeftFrames, self.movingRightFrames, self.jumpingFrames = createAnimation(self)
        self.frame = 0
        self.time = 0
        self.image = self.climbingFrames[0]
        self.jumpFrame = 0


    def draw(self, surface):                      
        """
        Draws the character on the specified surface.

        Args:
            surface (pygame.Surface): The surface to draw the character onto.
        """
        
        surface.blit(self.image, self.rect)


    def drawAnimation(self, screen):
        self.time += 1
        keys = pygame.key.get_pressed()
        a = keys[pygame.K_a]
        w = keys[pygame.K_w]
        s = keys[pygame.K_s]
        d = keys[pygame.K_d]
        
        if self.time %  9 == 0 and w and not (a or d or s):
            self.frame += 1
           # screen.blit(self.climbingFrames[math.floor(self.frame % len(self.climbingFrames))], self.rect.center)
            self.image = self.climbingFrames[math.floor(self.frame % len(self.climbingFrames))]

        if self.time % 9 == 0 and a and not (w or s or d) :
            self.frame += 1
            #screen.blit(self.movingLeftFrames[math.floor(self.frame % len(self.movingLeftFrames))], self.rect.center) 
            self.image = self.movingLeftFrames[math.floor(self.frame % len(self.movingLeftFrames))]
        
        if self.time % 9 == 0 and d and not (w or a or s):
            self.frame += 1
            #screen.blit(self.movingLeftFrames[math.floor(self.frame % len(self.movingLeftFrames))], self.rect.center) 
            self.image = self.movingRightFrames[math.floor(self.frame % len(self.movingLeftFrames))]
        
        if self.time % 9 == 0 and s and not (w or a or d) :
            self.frame += 1
            #screen.blit(self.movingLeftFrames[math.floor(self.frame % len(self.movingLeftFrames))], self.rect.center) 
            self.image = self.climbingFrames[math.floor(self.frame % len(self.movingLeftFrames))]
        
        self.draw(screen)


class Boy(Character):
    """
    Represents the 'Boy' character with unique image, speed, and stamina values.
    Inherits from Character.
    """

    def __init__(self, x, y):
        """
        Initializes the 'Boy' character with a specific image, speed, and max stamina.

        Args:
            x (int): The x-coordinate of the top-left corner of the boy character.
            y (int): The y-coordinate of the top-left corner of the boy character.
        """
        super().__init__(x, y, speed=2, max_stamina=100)
        # Load and set the character image
        self.image = pygame.transform.scale(
            pygame.image.load("sprites/characters/boy.png").convert_alpha(),
            (20, 20)
        )


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
        super().__init__(x, y, speed=3, max_stamina=80)
        # Load and set the character image
        
        