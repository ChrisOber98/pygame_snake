import pygame

class Snake:
    """A class that holds a snake sprite for playing."""

    def __init__(self, game):
        """Initialize default snake sprite."""

        self.screen = game.screen

        self.x = 0
        self.y = 0

        self.width = 40
        self.height = 40

        self.snake_color = (255, 234, 0)

    def draw(self):
        """Draw Snake to screen."""

        pygame.draw.rect(
            self.screen, 
            self.snake_color, 
            (self.x, self.y, self.width, self.height)
        )


    

