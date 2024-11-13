import pygame


class Button:
    def __init__(self, image, position, textInput, font, baseColor, hoveringColor):
        self.image = image
        self.position = pygame.Vector2(*position)
        self.baseColor, self.hoveringColor = baseColor, hoveringColor
        self.font = font
        self.textInput = textInput
        self.text = self.font.render(self.textInput, True, self.baseColor)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.position.x, self.position.y))
        self.textRect = self.text.get_rect(center=(self.position.x, self.position.y))


    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.textRect)


    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False


    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.textInput, True, self.hoveringColor)
        else:
            self.text = self.font.render(self.textInput, True, self.baseColor)
