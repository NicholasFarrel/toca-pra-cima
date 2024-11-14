import pygame

class Button:
    """
    A class to represent a clickable button on the screen.

    Attributes:
    ----------
    image : pygame.Surface
        The image or texture for the button.
    position : pygame.Vector2
        The position of the button on the screen (x, y).
    baseColor : tuple
        The color of the button's text when not hovered over.
    hoveringColor : tuple
        The color of the button's text when hovered over.
    font : pygame.font.Font
        The font used to render the button's text.
    textInput : str
        The text displayed on the button.
    text : pygame.Surface
        The rendered text image.
    rect : pygame.Rect
        The rectangle area representing the button for collision detection.
    textRect : pygame.Rect
        The rectangle area representing the text for proper alignment on the button.

    Methods:
    --------
    update(screen):
        Draws the button (image or text) on the screen.
    checkForInput(position):
        Checks if the given position (typically mouse position) is within the button's area.
    changeColor(position):
        Changes the button's text color when the mouse hovers over it.
    """

    def __init__(self, image, position, textInput, font, baseColor, hoveringColor):
        """
        Initialize the Button object.

        Args:
            image (pygame.Surface, optional): The image to be used as the button. Default is None (uses text).
            position (tuple): The position of the button (x, y).
            textInput (str): The text to be displayed on the button.
            font (pygame.font.Font): The font used to render the text.
            baseColor (tuple): The color of the text when not hovered.
            hoveringColor (tuple): The color of the text when hovered.
        """
        self.image = image  # Set the image of the button, or None if using text only
        self.position = pygame.Vector2(*position)  # Convert position to a pygame.Vector2 for convenience
        self.baseColor, self.hoveringColor = baseColor, hoveringColor  # Set base and hovering colors for text
        self.font = font  # Set font for the text on the button
        self.textInput = textInput  # Set the text to be displayed on the button
        self.text = self.font.render(self.textInput, True, self.baseColor)  # Render the text with the base color

        # If no image is provided, use the rendered text as the button's image
        if self.image is None:
            self.image = self.text

        # Create rectangle for the button (to handle position and collision detection)
        self.rect = self.image.get_rect(center=(self.position.x, self.position.y))

        # Create rectangle for the text to properly center it on the button
        self.textRect = self.text.get_rect(center=(self.position.x, self.position.y))

    def update(self, screen):
        """
        Updates the display of the button by drawing it on the screen.

        Args:
            screen (pygame.Surface): The surface to render the button on (typically the main game screen).
        """
        if self.image is not None:
            screen.blit(self.image, self.rect)  # Draw the button's image if it exists
        screen.blit(self.text, self.textRect)  # Draw the text on top of the button

    def checkForInput(self, position):
        """
        Check if the given position is within the bounds of the button.

        Args:
            position (tuple): The x and y coordinates (usually mouse position) to check for input.

        Returns:
            bool: True if the position is within the button's bounds, False otherwise.
        """
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        """
        Change the color of the button's text when the mouse hovers over it.

        Args:
            position (tuple): The x and y coordinates (usually mouse position) to check for hover.
        """
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            # If mouse is hovering over the button, change text color to hovering color
            self.text = self.font.render(self.textInput, True, self.hoveringColor)
        else:
            # If mouse is not hovering, reset text color to base color
            self.text = self.font.render(self.textInput, True, self.baseColor)
