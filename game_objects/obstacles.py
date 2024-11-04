import pygame
import random

class Cloud(pygame.sprite.Sprite):
    def __init__(self, screen_height):
       super().__init__()
       self.image = pygame.Surface((40, 30))
       self.color = (255, 255, 255)
       self.image.fill((255, 255, 255))  
       self.rect = self.image.get_rect()
       # Velocidade 
       self.speed_x = 10
       # Posição
       self.rect.x = 0
       self.rect.y = random.randint(100, screen_height)
       
    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.rect.x, self.rect.y, 40, 30))
       
    def move(self):
       self.rect.x += self.speed_x
       
clouds = []
       
def update(screen_height, screen):
    if len(clouds) < 3:
        c = Cloud(screen_height)
        clouds.append(c)
        
    for c in clouds:
        c.move()
        c.render(screen)
    
