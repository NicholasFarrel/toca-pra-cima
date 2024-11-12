import pygame

class Magnesio(pygame.sprite.Sprite):
    """
    Represents a magnesium power-up in the game, which restores stamina to the character upon collection.
    """
    magnesio_group = pygame.sprite.Group()

    def __init__(self, x, y):
        super().__init__()
        
        # Load and scale the magnesium image
        self.image = pygame.transform.scale(
            pygame.image.load("sprites/items/magnesio.png").convert_alpha(),
            (20, 20)
        )
        # Set the initial position of the item
        self.rect = self.image.get_rect(topleft=(x, y))
        
        # Stamina boost value given by the item
        self.stamina_boost = 20

    @classmethod
    def initialize(cls, positions):
        """
        Creates magnesio power-ups at the specified positions.
        
        Args:
            positions (list): A list of (x, y) tuples for power-up locations.
        """
        for pos in positions:
            magnesio = cls(*pos)
            cls.magnesio_group.add(magnesio)

    @classmethod
    def update(cls, character):
        """
        Check for collisions and apply the stamina boost effect if collected.
        
        Args:
            character: The character object to check for collisions with magnesio power-ups.
        """
        collected_magnesios = pygame.sprite.spritecollide(character, cls.magnesio_group, True)
        for magnesio in collected_magnesios:
            magnesio.apply_effect(character)

    def apply_effect(self, character):
        """
        Applies the stamina boost effect to the character.
        
        Args:
            character: The character object whose stamina is to be restored.
        """
        character.stamina = min(character.stamina + self.stamina_boost, character.max_stamina)
