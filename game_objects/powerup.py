import pygame

class Magnesio(pygame.sprite.Sprite):
    """
    Represents a magnesium power-up in the game, which restores stamina to the character upon collection.

    Attributes:
        image (pygame.Surface): The image representing the magnesium item.
        rect (pygame.Rect): The rectangular area of the item, used for positioning and collision.
        stamina_boost (int): The amount of stamina restored to the character when collected.
    """

    def __init__(self, x, y):
        """
        Initializes the magnesium power-up with its image, position, and stamina boost value.

        Args:
            x (int): The x-coordinate for the top-left corner of the magnesium item.
            y (int): The y-coordinate for the top-left corner of the magnesium item.
        """
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

    def apply_effect(self, character):
        """
        Applies the stamina boost effect to the character.

        Args:
            character (Character): The character object whose stamina is to be restored.
        
        The character's stamina is increased by `stamina_boost` but does not exceed `max_stamina`.
        """
        character.stamina = min(character.stamina + self.stamina_boost, character.max_stamina)