import pygame
import random

class Vulture:
    def __init__(self, screen_width, screen_height, health = 100, damage = 10, size = 30):
        self.x = 0 if random.randint(0,1) else screen_width
        self.position = pygame.Vector2(self.x, random.randint(0, screen_height//2))
        self.health = health
        self.damage = damage
        self.maxVelocitie = 50  
        self.rect = pygame.Rect(self.position.x, self.position.y, size, size)
        self.color = (255,0,0)
        self.size = size
        self.velocitie = pygame.Vector2(0,0)
        self.acceleration = pygame.Vector2(0,0)

    def move(self, player_position):
        #hanlding the moves of the bird
        dif = player_position - self.position
        distance = dif.length()
        self.velocitie.x += dif.x*0.001 
        self.velocitie.y += dif.y*0.0001
        self.position += self.velocitie
        self.dash(player_position, dif) 
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)

    def dash(self, player_position, dif):
        #dash attack
        if(player_position.y - self.position.y < 300 and abs(player_position.x - self.position.x) < 200 ):
            self.velocitie.y = dif.y * 0.1


    def check_corners(self, screen_width, screen_height):
        #checks if the bird leaved the screen
        if ( self.position.y < 0 or self.position.y > screen_height):#self.position.x < 0 or self.position.x > screen_width or self.position.y < 0 or self.position.y > screen_height):
            return True
        return False    
    
    def render(self, screen):
        pygame.draw.rect(screen, self.color, (*self.position, self.size, self.size))


vultures = []


def update(screen, screen_width, screen_height, player_position):
    #vulpures:
    
    if len(vultures) < 2:
        
        v = Vulture(screen_width, screen_height)
        vultures.append(v)
    
    for v in vultures:
        v.move(player_position)
        v.render(screen)
        #if(v.check_corners(screen_width,screen_height)): vultures.remove(v)


    
