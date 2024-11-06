import pygame

class GameScene:
    """Manages the game scene, including the background scrolling effect and positioning of magnesium power-ups."""

    def __init__(self, screen, character, magnesio_group):
        """
        Initializes the game scene with the background, character, and magnesium power-ups.

        Args:
            screen (pygame.Surface): The game screen surface to draw onto.
            character (Character): The main character in the game.
            magnesio_group (pygame.sprite.Group): Group containing magnesium power-up sprites.
        """
        # Load and set the background image
        self.background = pygame.image.load("sprites/backgrounds/level_background.png").convert()
        self.background_width, self.background_height = self.background.get_size()

        # Store references to screen, character, and magnesium group
        self.screen = screen
        self.character = character
        self.magnesio_group = magnesio_group

        # Initial background position to start at the bottom of the screen
        self.bg_y_offset = -(self.background_height - screen.get_height())

    def update(self, move_up, move_down, move_left, move_right):
        """
        Updates the position of the background and character based on input.

        Args:
            move_up (bool): True if moving up input is active.
            move_down (bool): True if moving down input is active.
            move_left (bool): True if moving left input is active.
            move_right (bool): True if moving right input is active.
        """
        # Vertical boundaries for the character to start moving the background
        upper_limit = self.screen.get_height() * 0.4
        lower_limit = self.screen.get_height() * 0.6

        # Background scrolls down if the character reaches the upper limit and 'move_up' is True
        if move_up and self.character.rect.y <= upper_limit:
            self.bg_y_offset += self.character.speed
            # Move all magnesium items with the background
            for magnesio in self.magnesio_group:
                magnesio.rect.y += self.character.speed

        # Background scrolls up if the character reaches the lower limit and 'move_down' is True
        elif move_down and self.character.rect.y >= lower_limit:
            self.bg_y_offset -= self.character.speed
            # Move all magnesium items with the background
            for magnesio in self.magnesio_group:
                magnesio.rect.y -= self.character.speed

        # If character is within the central range, it moves up and down without scrolling the background
        elif move_up and self.character.rect.y > upper_limit:
            self.character.rect.y -= self.character.speed
        elif move_down and self.character.rect.y < lower_limit:
            self.character.rect.y += self.character.speed

        # Horizontal movement with boundaries on the screen edges
        if move_left and self.character.rect.x > 0:
            self.character.rect.x -= self.character.speed
        if move_right and self.character.rect.x < self.screen.get_width() - self.character.rect.width:
            self.character.rect.x += self.character.speed

        # Limit background offset within the image's boundaries
        self.bg_y_offset = min(0, max(self.bg_y_offset, -(self.background_height - self.screen.get_height())))

    def draw(self):
        """Draws the background with the calculated offset and the magnesium power-ups."""
        # Draw the background at the current offset position
        self.screen.blit(self.background, (0, self.bg_y_offset))
        # Draw all magnesium items
        self.magnesio_group.draw(self.screen)