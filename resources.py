import pygame
import random

# Classe para os sacos de magnésio
class Magnesio(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 255, 255))  # Cor branca para o saco de magnésio
        self.rect = self.image.get_rect()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.reset_position()

    def reset_position(self):
        self.rect.x = random.randint(0, self.screen_width - self.rect.width)
        self.rect.y = random.randint(0, self.screen_height - self.rect.height)

# Classe para a barra de magnésio
class MagnesioBar:
    def __init__(self, max_magnesio):
        self.max_magnesio = max_magnesio
        self.current_magnesio = 0
        self.width = 200
        self.height = 20
        self.x = 10
        self.y = 10

    def increase_magnesio(self):
        if self.current_magnesio < self.max_magnesio:
            self.current_magnesio += 1

    def draw(self, surface):
        # Barra de fundo (vazia)
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.width, self.height))
        # Barra preenchida com magnésio coletado
        filled_width = (self.current_magnesio / self.max_magnesio) * self.width
        pygame.draw.rect(surface, (0, 255, 0), (self.x, self.y, filled_width, self.height))
