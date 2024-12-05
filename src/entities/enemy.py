import pygame
import random
import math
from src.systems.rendering import load_image, draw_bird_animation, render_poop, render_vulture, render_feathers
from src.game.assets import create_bird_animation
from src.systems.physics import check_vulture_corners, apply_gravity
from src.game.constants import *
from src.game.settings import *

class Feather:
    def __init__(self, position, type, size = 20):
        self.velocity = pygame.Vector2(random.randint(-5,5),random.randint(-1,1))
        self.acceleration = pygame.Vector2(0,0)
        self.position = position
        self.type = type
        self.color = colors[type]
        self.size = size
        self.rect = pygame.Rect(*self.position,size,size)
        self.time = 60 * 10
        self.falling = True
        self.rotate_time = 10
        self.angle = math.degrees(math.atan2(self.velocity.y, self.velocity.x))
        self.image = pygame.transform.scale(
            pygame.image.load(f'assets/sprites/birds/feathers/{self.type}.png'),
            (60,60)
        )
        self.original_image = self.image

    
    def update(self):
        self.acceleration += GRAVITY_FORCE
        self.velocity += GRAVITY_FORCE*0.001
        self.position += self.velocity 
        self.rotate_time -= 1
        self.time -= 1
        if self.rotate_time <= 0:
            self.update_orientation()

    def update_orientation(self):
        # Calculate the new angle
        new_angle = math.degrees(math.atan2(self.velocity.y, self.velocity.x))
        
        # Only update the image if the angle has changed significantly
        if abs(new_angle - self.angle) > 1:  # Adjust threshold as needed
            self.angle = new_angle
            self.image = pygame.transform.rotate(self.original_image, self.angle)
            #self.rect = self.image.get_rect(center=self.position)
        
        # Reset rotate_time to delay the next orientation update
        self.rotate_time = 0  # Adjust as needed

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
        self.frames = create_bird_animation(self)
        self.frame = 0
        self.feathers = []
        self.damage_cooldown = 10



class Vulture(Bird):
    """
    A class to represent a Vulture enemy that inherits from the Bird class.

    Methods include movement, dashing, damage dealing, and rendering.
    """

    def __init__(self, position, type, maxVelocity=4, health=3, damage=1, size=100, color=(255, 0, 0)):
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
        self.type = type
        self.color = colors[type]
        self.imagePath = f'assets/sprites/birds/birdFlying{self.type}Right.png'
        self.scale = 5
        self.original_frame_dimension = (160, 160)
        self.scaled_frame_dimension = (self.scale * 16, self.scale * 16)
        self.dashTime = 0
        self.damageTime = 0
        super().__init__(position, health, size, maxVelocity, color, self.imagePath, self.scale, self.original_frame_dimension, self.scaled_frame_dimension)
        self.damage = damage


    def move(self,player):
        """
        Move the vulture towards the player.

        Args:
            player.position (pygame.Vector2): The position of the player.
            dy (float): The background offset for vertical movement.
        """
        dif = player.position - self.position

        # Set direction based on player position
        if dif.x < 0:
            self.imagePath = f'assets/sprites/birds/birdFlying{self.type}Left.png'
        else:
            self.imagePath = f'assets/sprites/birds/birdFlying{self.type}Right.png'
        self.frames = create_bird_animation(self)

        distance = dif.length()
        self.velocity.x += dif.x * 0.001  # Move slightly towards player in x direction
        self.velocity.y += dif.y * 0.0001  # Move slightly towards player in y direction
        self.position += self.velocity

        if self.velocity.length() > self.maxVelocity:
            self.velocity = self.velocity.normalize() * self.maxVelocity

        if self.dashTime > 20:
            self.velocity = self.velocity.normalize() * self.maxVelocity  # Boost dash speed

        #self.dash(player.position, dif)  # Perform dash attack
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


    def dealDamage(self, player):
        """
        Deal damage to the player if the vulture collides with them.

        Args:
            player (object): The player player.
        """
        if self.damageTime > 60:
            player.life -= self.damage
            self.damageTime = 0


    def dash(self, player, dif):
        """
        Perform a dash attack if the player is within a specific range.

        Args:
            player.position (pygame.Vector2): The position of the player.
            dif (pygame.Vector2): The difference vector between the vulture and player.
        """
        if player.position.y - self.position.y < 200 and player.position.y > self.position.y and abs(player.position.x - self.position.x) < 100:
            self.dashTime += 1
            self.velocity.y = dif.y * 0.1
            self.velocity.x = dif.x * 0.1
        else:
            self.dashTime = 0

    
    def checkCollision(self, v2):
        if v2 == self:
            return
        
        dif = self.position - v2.position

        distance = dif.length()

        if( distance < self.size ):
            
            v2.velocity -= dif/distance * 2
            self.velocity += dif/distance * 2
            v2.acceleration -= dif/distance
            self.acceleration += dif/distance


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
    dealDamage(player):
        Deals damage to the player player when it collides with them.
    render(screen):
        Renders the poop on the screen.
    """

    def __init__(self, position, velocity, damage=1, color=(0, 255, 0), size=13):
        """
        Initialize a Poop object.

        Args:
            position (tuple): Initial position of the poop (x, y).
            velocity (pygame.Vector2): Initial velocity of the poop.
            damage (int, optional): The damage dealt by the poop. Default is 10.
            color (tuple, optional): The color of the poop. Default is green.
            size (int, optional): The size of the poop. Default is 13.
        """
        self.imagePath = 'assets/sprites/birds/birdFlyingBrownRight.png'
        self.position = position
        self.velocity = velocity
        self.damage = damage  # Default damage
        self.image = load_image(self.imagePath, (size, size))
        self.color = color
        self.size = size
        self.rect = pygame.Rect(*self.position, self.size, self.size)
        self.dissapear = False


    def move(self):
        """
        Update the position of the poop with gravity and speed adjustments.

        Args:
            dy (float): The background offset for vertical movement.
        """
        self.velocity += pygame.Vector2(0, 0.2)  # Apply gravity
        self.position += self.velocity

        self.rect = pygame.Rect(*self.position, self.size, self.size)

    def dealDamage(self, player):
        """
        Deal damage to the player player.

        Args:
            player (object): The player player.
        """
        player.life -= self.damage  # Reduce player's life by damage
        self.dissapear = True  # Mark the poop to disappear after hitting the player

    
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

    def __init__(self, position, health=bird_life, size=50, maxVelocity=5, color=(0, 0, 255)):
        """
        Initialize a Pigeon object with given parameters.

        Args:
            position (tuple): Initial position of the pigeon (x, y).
            health (int, optional): Health points of the pigeon. Default is 10.
            size (int, optional): Size of the pigeon. Default is 50.
            maxVelocity (float, optional): Maximum velocity of the pigeon. Default is 5.
            color (tuple, optional): Color of the pigeon. Default is blue.
        """
        self.imagePath = 'assets/sprites/birds/birdFlyingBrownRight.png'
        self.scale = 5
        self.type = 'RED'
        self.original_frame_dimension = (160, 160)
        self.scaled_frame_dimension = (self.scale * 16, self.scale * 16)
        super().__init__(position, health, size, maxVelocity, color, self.imagePath, self.scale, self.original_frame_dimension, self.scaled_frame_dimension)
        self.image = pygame.image.load(self.imagePath)
        self.velocity = pygame.Vector2(random.randint(2, maxVelocity), 0)
        self.poopTime = random.randint(30, 100)  # Random time for poop drops
        self.time = 0
        self.poops = []

    def move(self):
        """
        Move the pigeon and check if it's time to drop poop.

        Args:
            dy (float): The background offset for vertical movement.
        """

        self.position += self.velocity  # Move pigeon in the x-direction
        self.rect = pygame.Rect(*self.position, self.size, self.size)
        self.poop()  # Check for poop drop

    def poop(self):
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
            poop.move()  # Move all existing poops


# List to store vulture and pigeon instances
blueVulturesPosition = []
yellowVulturesPosition = []
pigeonsPosition = []
feathers = []


def update_feathers(screen, camera):
        for feather in feathers:
            feather.update()
        render_feathers(feathers, screen, camera)

def initialize(player):
    """
    Initialize the vultures and pigeons and store them in the respective lists.

    Args:
        player (object): The player player (used to set player speed).
    """
    global playerSpeed
    playerSpeed = player.velocity  # Set the player speed

    vultures = []
    pigeons = []

    # Initialize vultures
    for vPos in blueVulturesPosition:
        v = Vulture(vPos, 'BLUE')
        vultures.append(v)
    for vPos in yellowVulturesPosition:
        v = Vulture(vPos, 'YELLOW')
        vultures.append(v)

    # Initialize pigeons
    for pPos in pigeonsPosition:
        p = Pigeon(pPos)
        pigeons.append(p)

    return [pigeons, vultures]

col = ['BLUE', 'YELLOW', 'RED']

def update(screen, camera, player, enemies):
    """
    Update all enemy positions, check for collisions with the player, and render them.

    Args:
        screen (pygame.Surface): The surface on which to render the enemies.
        bg_y_offset (float): The vertical offset of the background (for parallax scrolling).
        player (object): The player player for collision detection.
    """
    global feathers

    pigeons, vultures = enemies[0], enemies[1]
    feathers[:] = [f for f in feathers if f.time > 0]
    update_feathers(screen,camera)

    for i in range(max_birds - len(vultures)):
        vPos = (-100,random.randint(-SCREEN_HEIGHT + int(camera.position.y), int(camera.position.y)))
        v = Vulture(vPos, col[random.randint(0,len(col)-1)])
        vultures.append(v)


    # Move and render each vulture
    vultures[:] = [v for v in vultures if v.health > 0]
    for v in vultures:
        v.move(player)  # Move vulture towards player
        dif = v.position - player.position
        distance = dif.length()
        if distance < 50:  # Check for collision with player
            v.dealDamage(player)
        
        render_vulture(v,screen, camera)  # Render the vulture
        v.damage_cooldown -= 1
        

        for v2 in vultures:
            v.checkCollision(v2)

    # Move and render each pigeon
    pigeons[:] = [p for p in pigeons if p.health > 0]
    for p in pigeons:
        p.move()  # Move pigeon


        draw_bird_animation(p,screen, camera) # Draw the pigeon's animation

        # Remove poops that have disappeared
        p.poops[:] = [poop for poop in p.poops if not poop.dissapear]

        p.damage_cooldown -= 1

        # Check for collision of each poop with the player
        for poop in p.poops:
            if poop.rect.colliderect(player.rect):  # Check for poop collision with player
                poop.dealDamage(player)

            render_poop(poop,screen,camera)  # Render the poop



