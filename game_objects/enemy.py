import pygame
import random

class Vulture:
    def __init__(self, screen_width, screen_height, health = 100, speed = 2, damage = 10, size = 10):
        self.x = 0 if random.randint(0,1) else screen_width
        self.position = pygame.Vector2(self.x, random.randint(0, screen_height))
        self.health = health
        self.speed = (pygame.Vector2(screen_width/2, screen_height/2 ) - self.position)*random.uniform(0,1)
        self.damage = damage
        self.rect = pygame.Rect(self.position.x, self.position.y, size, size)
        self.color = (255,0,0)
        self.size = size
        self.velocitie = pygame.Vector2(0,0)
        self.acceleration = pygame.Vector2(0,0)

    def move(self, player_position):
        dif = player_position - self.position
        distance = dif.length()
        dif.normalize_ip()
        self.acceleration += dif/(distance) * 3
        self.velocitie += self.acceleration * 5  
        self.position += self.velocitie*0.01 

    def check_corners(self, screen_width, screen_height):
        if (self.position.x < 0 or self.position.x > screen_width or self.position.y < 0 or self.position.y > screen_height):
            return True
        return False
    
    def render(self, screen):
        pygame.draw.rect(screen, self.color, (*self.position, self.size, self.size))


vultures = []


def update(screen, screen_width, screen_height, player_position):
    #vulpures:
    
    if len(vultures) < 10:
        
        v = Vulture(screen_width, screen_height)
        vultures.append(v)
    
    for v in vultures:
        v.move(player_position)
        v.render(screen)
        #if(v.check_corners(screen_width,screen_height)): vultures.remove(v)


    
