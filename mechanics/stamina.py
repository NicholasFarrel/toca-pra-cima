import pygame

class StaminaBar:
    """
    Represents a stamina bar for the character, showing current stamina as a colored bar.

    Attributes:
        x (int): The x-coordinate of the stamina bar on the screen.
        y (int): The y-coordinate of the stamina bar on the screen.
        width (int): The total width of the stamina bar when full.
        height (int): The height of the stamina bar.
        max_stamina (int): The maximum stamina value, used for scaling.
        current_width (int): The current width of the bar, representing the current stamina.
    """

    def __init__(self, x, y, width, height, max_stamina):
        """
        Initializes the stamina bar with position, size, and maximum stamina.

        Args:
            x (int): The x-coordinate of the top-left corner of the bar.
            y (int): The y-coordinate of the top-left corner of the bar.
            width (int): The width of the bar when the stamina is at maximum.
            height (int): The height of the bar.
            max_stamina (int): The maximum stamina value, used to calculate the bar's current width.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_stamina = max_stamina
        self.current_width = width  # Starts with full width, representing full stamina

    def update(self, current_stamina):
        """
        Updates the width of the stamina bar to reflect the current stamina level.

        Args:
            current_stamina (int): The current stamina value of the character.
        """
        # Calculate the proportional width of the bar based on current stamina
        self.current_width = (current_stamina / self.max_stamina) * self.width

    def draw(self, surface):
        """
        Draws the stamina bar on the specified surface.

        Args:
            surface (pygame.Surface): The surface to draw the stamina bar onto.
        """
        # Draw the background of the stamina bar (red, representing empty)
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.width, self.height))
        # Draw the current stamina level (green, representing filled portion)
        pygame.draw.rect(surface, (0, 255, 0), (self.x, self.y, self.current_width, self.height))