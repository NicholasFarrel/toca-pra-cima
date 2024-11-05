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
        self.rect = pygame.Rect(x, y, 50, 50)
        # Initialize speed and stamina values
        self.speed = speed
        self.max_stamina = max_stamina
        self.stamina = max_stamina - 60  # Initialize stamina for testing purposes

    def draw(self, surface):
        """
        Draws the character on the specified surface.

        Args:
            surface (pygame.Surface): The surface to draw the character onto.
        """
        surface.blit(self.image, self.rect)

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
            (50, 50)
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
        self.image = pygame.transform.scale(
            pygame.image.load("sprites/characters/girl.png").convert_alpha(),
            (50, 50)
        )