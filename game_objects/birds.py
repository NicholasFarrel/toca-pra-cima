import pygame
import random

backgroundY = 0
playerSpeed = 0

class Bird():
    def __init__(self, position, health, size, maxVelocitie, color):
        self.position = pygame.Vector2(position[0], position[1])
        self.health = health
        self.size = size
        self.maxVelocity = maxVelocitie
        self.rect = pygame.Rect(*self.position, size, size)
        self.color = color
        self.velocity = pygame.Vector2(0,0)
        self.acceleration = pygame.Vector2(0,0)
        
    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class Vulture(Bird):
    """
    A class to represent a Vulture enemy in the game.

    Attributes:
    -----------
    x : int
        The initial x-coordinate of the vulture, set randomly at the screen's edges.
    position : pygame.Vector2
        The position vector of the vulture.
    health : int
        The health points of the vulture.
    damage : int
        The damage points dealt by the vulture.
    maxVelocity : float
        The maximum velocity the vulture can achieve.
    rect : pygame.Rect
        The rectangular area representing the vulture for collision detection.
    color : tuple
        The color of the vulture.
    size : int
        The size of the vulture.
    velocity : pygame.Vector2
        The current velocity vector of the vulture.
    acceleration : pygame.Vector2
        The acceleration vector of the vulture.

    Methods:
    --------
    move(player_position):
        Updates the vulture's position to move toward the player.
    dash(player_position, dif):
        Performs a dash attack when the player is within a specific range.
    check_corners(screen_width, screen_height):
        Checks if the vulture has moved off the screen vertically.
    render(screen):
        Draws the vulture on the given screen surface.
    """

    def __init__(self, position, maxVelocitie = 10, health=100, damage=10, size=30, color = (255,0,0)):
        """
        Initialize a new vulture with random position and specified attributes.

        Parameters:
        -----------
        screen_width : int
            The width of the game screen.
        screen_height : int
            The height of the game screen.
        health : int, optional
            The health points of the vulture (default is 100).
        damage : int, optional
            The damage points dealt by the vulture (default is 10).
        size : int, optional
            The size of the vulture (default is 30).
        """
        self.dashTime = 0
        super().__init__(position, health, size, maxVelocitie, color)
        self.damage = damage  


    def move(self, player_position, dy):
        """
        Update the vulture's position to move toward the player.

        Parameters:
        -----------
        player_position : pygame.Vector2
            The current position of the player.
        """
        dif = player_position - self.position
        distance = dif.length()
        # Adjust the velocity slightly toward the player's position

        self.velocity.x += dif.x * 0.001
        self.velocity.y += dif.y * 0.0001
        self.position += self.velocity

        if abs(dy) == playerSpeed:
            self.position.y += dy

        if (self.velocity.length() > self.maxVelocity):
            self.velocity = self.velocity.normalize() * self.maxVelocity

        if (self.dashTime > 20):
            self.velocity = self.velocity.normalize() * self.maxVelocity

        self.dash(player_position, dif)
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)

    def dash(self, player_position, dif):
        """
        Perform a dash attack when the player is within a specific range.

        Parameters:
        -----------
        player_position : pygame.Vector2
            The current position of the player.
        dif : pygame.Vector2
            The difference vector between the vulture and the player.
        """
        if (player_position.y - self.position.y < 200 and player_position.y > self.position.y and abs(player_position.x - self.position.x) < 100):
            # Quick movement towards the player
            self.dashTime += 1
            self.velocity.y = dif.y * 0.1
        else:
            self.dashTime = 0


    def check_corners(self, screen_width, screen_height):
        """
        Check if the vulture has moved off the screen vertically.

        Parameters:
        -----------
        screen_width : int
            The width of the game screen.
        screen_height : int
            The height of the game screen.

        Returns:
        --------
        bool
            True if the vulture is off the screen vertically, False otherwise.
        """
        if self.position.y < 0 or self.position.y > screen_height:
            return True
        return False

  


class Poop:
    def __init__(self, position, velocity, damage= 10, color = (0,255,0), size = 13):
        self.position = position
        self.velocity = velocity
        self.damage = 10
        self.color = color
        self.size = size
        self.rect = pygame.Rect(*self.position, self.size, self.size)


    def move(self, dy):
        self.velocity += pygame.Vector2(0,0.2)
        self.position += self.velocity
        if(abs(dy) == playerSpeed):
            self.position.y += dy

        self.rect = pygame.Rect(*self.position, self.size, self.size)


    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)



class Pigeon(Bird):
    def __init__(self, position, health = 10, size = 10, maxVelocity = 5, color = (0,0,255), ):
        super().__init__(position, health, size, maxVelocity, color)
        self.velocity = pygame.Vector2(random.randint(1,maxVelocity), 0)
        self.poopTime = random.randint(30,100)
        self.time = 0
        self.poops = []


    def move(self, dy):
        if(abs(dy) == playerSpeed):
            self.position.y += dy
        self.position += self.velocity 
        self.rect = pygame.Rect(*self.position, self.size, self.size)
        self.poop(dy)

    def poop(self,dy):
        if (self.time > self.poopTime):
            p = Poop(self.position.copy(), self.velocity.copy())
            self.poops.append(p)
            self.time = 0
        else:
            self.time += 1
        
        for poop in self.poops:
            poop.move(dy)







# List to store vulture instances
vulturesPosition = [(0,100),(500,500)]
pigeonsPosition = [(0,100),(0,400)]
vultures = []
pigeons = []

def initialize(speed):
    global playerSpeed 
    playerSpeed = speed
    for vPos in vulturesPosition:
        v = Vulture(vPos)
        vultures.append(v)
    for pPos in pigeonsPosition:
        p = Pigeon(pPos)
        pigeons.append(p)



def update(screen, bg_y_offset, player_position):
    """
    Update the vulture instances, move them, and render them on the screen.

    Parameters:
    -----------
    screen : pygame.Surface
        The surface on which to render the vultures.
    screen_width : int
        The width of the game screen.
    screen_height : int
        The height of the game screen.
    player_position : pygame.Vector2
        The current position of the player.
    """
    global backgroundY

    dy = bg_y_offset - backgroundY
    backgroundY = bg_y_offset

    # Move and render each vulture
    for v in vultures:
        v.move(player_position, dy)
        v.render(screen)

    for p in pigeons:
        p.move(dy)
        p.render(screen)
        for poop in p.poops:
            poop.render(screen)
