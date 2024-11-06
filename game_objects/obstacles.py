import pygame
import random  # posicao = pygame.Vector2(x,y)

class Cloud:
    def __init__(self, screen_height):
        # Posição
        self.position = pygame.Vector2(0-140, random.randint(5, screen_height-100))
        # Velocidade 
        self.speed = random.randint(2, 5)
        
    def render(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (*self.position, 140, 60))
       
    def move(self):
        self.position.x += self.speed
        
    def check_screen(self, screen_width):
        if self.position.x > screen_width:
            return True
        else:
            return False
       
clouds = []
       
def update(screen_width, screen_height, screen):
    if len(clouds) < 80:
        c = Cloud(screen_height)
        clouds.append(c)
        
    clouds[:] = [c for c in clouds if not c.check_screen(screen_width)]
        
    for c in clouds:
        c.move()
        c.render(screen)
        
    
