import pygame
import random
import math

# Global variables
backgroundY = 0
playerSpeed = 0

def loadImage(imagePath, dimension):
    """
    Load an image from the given path and scale it to the specified dimensions.

    Args:
        imagePath (str): Path to the image file.
        dimension (tuple): Desired dimensions (width, height) for the image.

    Returns:
        pygame.Surface: The loaded and scaled image.
    """
    image = pygame.image.load(imagePath).convert_alpha()  # Load image with transparency
    image = pygame.transform.scale(image, dimension)  # Scale image to given dimensions
    return image


def createAnimation(entity, rotation=0):
    """
    Create an animation by slicing the sprite sheet of the entity into frames.

    Args:
        entity (object): The entity (e.g., bird) with the sprite sheet data.
        rotation (int, optional): Rotation angle for frames. Default is 0.

    Returns:
        list: A list of frames (surfaces) for the animation.
    """
    image = pygame.image.load(entity.imagePath)  # Load the sprite sheet
    frames = [
        pygame.transform.scale(    
            image.subsurface(i * entity.original_frame_dimension[0], 0, *entity.original_frame_dimension),
            entity.scaled_frame_dimension
        )
        for i in range(8)  # Assuming there are 8 frames in the sprite sheet
    ]
    return frames


class Bird:
    """
    A class to represent a generic Bird entity, which could be extended by specific bird types.
    """

    def __init__(self, position, health, size, maxVelocity, color, imagePath, scale, original_frame_dimension, scaled_frame_dimension):
        """
        Initialize a bird with the provided parameters.

        Args:
            position (tuple): Initial position of the bird (x, y).
            health (int): Health of the bird.
            size (int): Size of the bird.
            maxVelocity (float): Maximum speed the bird can travel.
            color (tuple): RGB color of the bird.
            imagePath (str): Path to the bird's sprite sheet.
            scale (float): Scaling factor for the bird's sprite.
            original_frame_dimension (tuple): Original dimensions of each frame in the sprite sheet.
            scaled_frame_dimension (tuple): Scaled dimensions of each frame.
        """
        self.position = pygame.Vector2(position)
        self.health = health
        self.size = size
        self.maxVelocity = maxVelocity
        self.rect = pygame.Rect(*self.position, size, size)
        self.color = color
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
        self.angle = 0
        self.original_frame_dimension = original_frame_dimension
        self.scaled_frame_dimension = scaled_frame_dimension
        self.frames = createAnimation(self)
        self.frame = 0

    def drawAnimation(self, screen):
        """
        Draw the bird's animation on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the animation on.
        """
        screen.blit(self.frames[math.floor(self.frame % len(self.frames))], self.rect.center)
        self.frame += 1/5 * self.maxVelocity/10  # Adjust frame speed based on velocity


class Vulture(Bird):
    """
    A class to represent a Vulture enemy that inherits from the Bird class.

    Methods include movement, dashing, damage dealing, and rendering.
    """

    def __init__(self, position, maxVelocity=10, health=100, damage=10, size=40, color=(255, 0, 0)):
        """
        Initialize a Vulture with the provided parameters.

        Args:
            position (tuple): Initial position of the vulture (x, y).
            maxVelocity (float): Maximum velocity of the vulture.
            health (int): Health points of the vulture.
            damage (int): Damage dealt by the vulture.
            size (int): Size of the vulture.
            color (tuple): RGB color of the vulture.
        """
        self.imagePath = 'sprites/enemies/birdFlying.png'
        self.scale = 5
        self.original_frame_dimension = (160, 160)
        self.scaled_frame_dimension = (self.scale * 16, self.scale * 16)
        self.dashTime = 0
        self.damageTime = 0
        super().__init__(position, health, size, maxVelocity, color, self.imagePath, self.scale, self.original_frame_dimension, self.scaled_frame_dimension)
        self.damage = damage

    def move(self, playerPosition, dy):
        """
        Move the vulture towards the player.

        Args:
            playerPosition (pygame.Vector2): The position of the player.
            dy (float): The background offset for vertical movement.
        """
        dif = playerPosition - self.position

        # Set direction based on player position
        if dif.x < 0:
            self.imagePath = 'sprites/enemies/left.png'
        else:
            self.imagePath = 'sprites/enemies/birdFlying.png'
        self.frames = createAnimation(self)

        distance = dif.length()
        self.velocity.x += dif.x * 0.001  # Move slightly towards player in x direction
        self.velocity.y += dif.y * 0.0001  # Move slightly towards player in y direction
        self.position += self.velocity

        if abs(dy) == playerSpeed:
            self.position.y += dy

        if self.velocity.length() > self.maxVelocity:
            self.velocity = self.velocity.normalize() * self.maxVelocity

        if self.dashTime > 20:
            self.velocity = self.velocity.normalize() * self.maxVelocity  # Boost dash speed

        self.dash(playerPosition, dif)  # Perform dash attack
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)
        self.damageTime += 1

        self.angle = math.atan2(dif.x, dif.y) * 180 / math.pi
        self.orientation(distance)

    def orientation(self, distance):
        """
        Adjust the vulture's orientation based on its movement direction and distance.

        Args:
            distance (float): The distance between the vulture and the player.
        """
        if distance > 20:
            self.angle = self.angle % 30  # Adjust angle in multiples of 30
        self.rotatedImage = pygame.transform.rotate(self.frames[math.floor(self.frame % len(self.frames))], self.angle)

    def dealDamage(self, character):
        """
        Deal damage to the character if the vulture collides with them.

        Args:
            character (object): The player character.
        """
        if self.damageTime > 60:
            character.stamina -= self.damage
            self.damageTime = 0

    def dash(self, playerPosition, dif):
        """
        Perform a dash attack if the player is within a specific range.

        Args:
            playerPosition (pygame.Vector2): The position of the player.
            dif (pygame.Vector2): The difference vector between the vulture and player.
        """
        if playerPosition.y - self.position.y < 200 and playerPosition.y > self.position.y and abs(playerPosition.x - self.position.x) < 100:
            self.dashTime += 1
            self.velocity.y = dif.y * 0.1
            self.velocity.x = dif.x * 0.1
        else:
            self.dashTime = 0

    def check_corners(self, screen_width, screen_height):
        """
        Check if the vulture has moved off the screen vertically.

        Args:
            screen_width (int): The width of the game screen.
            screen_height (int): The height of the game screen.

        Returns:
            bool: True if the vulture is off the screen, False otherwise.
        """
        if self.position.y < 0 or self.position.y > screen_height:
            return True
        return False

    def render(self, screen):
        """
        Render the vulture on the screen.

        Args:
            screen (pygame.Surface): The screen to render the vulture on.
        """
        screen.blit(self.rotatedImage, self.rect.center)
        self.frame += 1 / 5 * self.velocity.length() / 10


class Poop:
    """
    A class to represent the poop projectiles thrown by pigeons.
    
    Attributes:
    ----------
    position : pygame.Vector2
        The position of the poop projectile.
    velocity : pygame.Vector2
        The velocity of the poop projectile.
    damage : int
        The damage dealt by the poop.
    color : tuple
        The color of the poop (RGB).
    size : int
        The size of the poop.
    rect : pygame.Rect
        The rectangular area representing the poop for collision detection.
    dissapear : bool
        A flag to determine whether the poop should disappear after hitting the player.

    Methods:
    --------
    move(dy):
        Updates the position of the poop.
    dealDamage(character):
        Deals damage to the player character when it collides with them.
    render(screen):
        Renders the poop on the screen.
    """

    def __init__(self, position, velocity, damage=10, color=(0, 255, 0), size=13):
        """
        Initialize a Poop object.

        Args:
            position (tuple): Initial position of the poop (x, y).
            velocity (pygame.Vector2): Initial velocity of the poop.
            damage (int, optional): The damage dealt by the poop. Default is 10.
            color (tuple, optional): The color of the poop. Default is green.
            size (int, optional): The size of the poop. Default is 13.
        """
        self.imagePath = 'sprites/enemies/pigeon.png'
        self.position = position
        self.velocity = velocity
        self.damage = 10  # Default damage
        self.image = loadImage(self.imagePath, (size, size))
        self.color = color
        self.size = size
        self.rect = pygame.Rect(*self.position, self.size, self.size)
        self.dissapear = False

    def move(self, dy):
        """
        Update the position of the poop with gravity and speed adjustments.

        Args:
            dy (float): The background offset for vertical movement.
        """
        self.velocity += pygame.Vector2(0, 0.2)  # Apply gravity
        self.position += self.velocity
        if abs(dy) == playerSpeed:
            self.position.y += dy

        self.rect = pygame.Rect(*self.position, self.size, self.size)

    def dealDamage(self, character):
        """
        Deal damage to the player character.

        Args:
            character (object): The player character.
        """
        character.stamina -= self.damage  # Reduce character's stamina by damage
        self.dissapear = True  # Mark the poop to disappear after hitting the character

    def render(self, screen):
        """
        Render the poop on the screen.

        Args:
            screen (pygame.Surface): The surface to render the poop on.
        """
        screen.blit(self.image, self.rect.center)
        # pygame.draw.rect(screen, self.color, self.rect)  # Optional: draw the rectangle


class Pigeon(Bird):
    """
    A class to represent a Pigeon enemy, a type of Bird that can drop poop.

    Attributes:
    ----------
    poopTime : int
        Time interval between each poop drop.
    time : int
        A counter for time until the next poop drop.
    poops : list
        List of Poop objects that the pigeon has dropped.

    Methods:
    --------
    move(dy):
        Updates the pigeon’s position and checks if it’s time to drop poop.
    poop(dy):
        Drops a poop after a specific interval and moves all dropped poops.
    """

    def __init__(self, position, health=10, size=50, maxVelocity=5, color=(0, 0, 255)):
        """
        Initialize a Pigeon object with given parameters.

        Args:
            position (tuple): Initial position of the pigeon (x, y).
            health (int, optional): Health points of the pigeon. Default is 10.
            size (int, optional): Size of the pigeon. Default is 50.
            maxVelocity (float, optional): Maximum velocity of the pigeon. Default is 5.
            color (tuple, optional): Color of the pigeon. Default is blue.
        """
        self.imagePath = 'sprites/enemies/birdFlying.png'
        self.scale = 5
        self.original_frame_dimension = (160, 160)
        self.scaled_frame_dimension = (self.scale * 16, self.scale * 16)
        super().__init__(position, health, size, maxVelocity, color, self.imagePath, self.scale, self.original_frame_dimension, self.scaled_frame_dimension)
        self.image = pygame.image.load(self.imagePath)
        self.velocity = pygame.Vector2(random.randint(2, maxVelocity), 0)
        self.poopTime = random.randint(30, 100)  # Random time for poop drops
        self.time = 0
        self.poops = []

    def move(self, dy):
        """
        Move the pigeon and check if it's time to drop poop.

        Args:
            dy (float): The background offset for vertical movement.
        """
        if abs(dy) == playerSpeed:
            self.position.y += dy
        self.position += self.velocity  # Move pigeon in the x-direction
        self.rect = pygame.Rect(*self.position, self.size, self.size)
        self.poop(dy)  # Check for poop drop

    def poop(self, dy):
        """
        Check if it's time to drop a poop. If it is, create a new Poop object.

        Args:
            dy (float): The background offset for vertical movement.
        """
        if self.time > self.poopTime:
            p = Poop(self.position.copy(), self.velocity.copy())  # Create a new Poop object
            self.poops.append(p)
            self.time = 0
        else:
            self.time += 1
        
        for poop in self.poops:
            poop.move(dy)  # Move all existing poops


# List to store vulture and pigeon instances
vulturesPosition = [(0, 100), (500, 500), (0, 0), (0, 700)]
pigeonsPosition = [(0, 100), (0, 400)]
vultures = []
pigeons = []


def initialize(character):
    """
    Initialize the vultures and pigeons and store them in the respective lists.

    Args:
        character (object): The player character (used to set player speed).
    """
    global playerSpeed
    playerSpeed = character.speed  # Set the player speed

    # Initialize vultures
    for vPos in vulturesPosition:
        v = Vulture(vPos)
        vultures.append(v)

    # Initialize pigeons
    for pPos in pigeonsPosition:
        p = Pigeon(pPos)
        pigeons.append(p)


def update(screen, bg_y_offset, character):
    """
    Update all enemy positions, check for collisions with the player, and render them.

    Args:
        screen (pygame.Surface): The surface on which to render the enemies.
        bg_y_offset (float): The vertical offset of the background (for parallax scrolling).
        character (object): The player character for collision detection.
    """
    global backgroundY

    playerPosition = pygame.math.Vector2(character.rect.center)  # Get player position
    playerRect = character.rect  # Get player rectangle for collision detection

    dy = bg_y_offset - backgroundY  # Calculate vertical movement offset
    backgroundY = bg_y_offset  # Update the background Y offset

    # Move and render each vulture
    for v in vultures:
        v.move(playerPosition, dy)  # Move vulture towards player
        if v.rect.colliderect(playerRect):  # Check for collision with player
            v.dealDamage(character)
        v.render(screen)  # Render the vulture

    # Move and render each pigeon
    for p in pigeons:
        p.move(dy)  # Move pigeon
        p.drawAnimation(screen)  # Draw the pigeon's animation

        # Remove poops that have disappeared
        p.poops[:] = [poop for poop in p.poops if not poop.dissapear]

        # Check for collision of each poop with the player
        for poop in p.poops:
            if poop.rect.colliderect(playerRect):  # Check for poop collision with player
                poop.dealDamage(character)
            poop.render(screen)  # Render the poop
