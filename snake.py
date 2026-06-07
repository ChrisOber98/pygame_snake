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

        self.is_moving_down = False
        self.is_moving_up = False
        self.is_moving_left = False
        self.is_moving_right = False

    def draw(self):
        """Draw Snake to screen."""

        pygame.draw.rect(
            self.screen, 
            self.snake_color, 
            (self.x, self.y, self.width, self.height)
        )

    def update(self):
        """Update snake position."""

        if self.is_moving_down:
            self.y += 1
        if self.is_moving_up:
            self.y -= 1
        if self.is_moving_left:
            self.x -= 1
        if self.is_moving_right:
            self.x += 1

    def reset_movement(self):
        """Reset the snakes movement variables to all False."""

        self.is_moving_down = False
        self.is_moving_up = False
        self.is_moving_left = False
        self.is_moving_right = False




    

