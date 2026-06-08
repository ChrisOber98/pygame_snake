import pygame
import random

class Apple:
    """Class to hold and represent a apple on the window."""

    def __init__(self, snake, settings, game):
        """Inits defualt values for apple entity."""

        # Snake Values
        self.snake = snake

        # Setting Values
        self.settings = settings

        # Game Values
        self.screen = game.screen

        # Apple Values
        self.x = 0
        self.y = 0
        self.color = self.settings.apple_color
        self.rect = pygame.Rect(
            self.x, self.y, self.settings.cell_size, self.settings.cell_size
        ) 

        # Init behaviors
        self.update_randomly()

    def draw(self):
        """Draw Apple to screen."""

        pygame.draw.rect(
            self.screen, 
            self.color, 
            self.rect
        )

    def update_randomly(self):
        """Update the apples position randomly taking into account the snake."""

        # Get Random x coordinate from 0 -> screen width not including current
        # Snake Poistion
        rand_x = random.randint(
            0, 
            self.settings.window_width - self.settings.cell_size
            )
        while (
            rand_x >= self.snake.get_x_coord() and 
            rand_x <= self.snake.get_x_coord() + self.settings.cell_size
        ):
            rand_x = random.randint(0, self.settings.window_width)
            
        # Get Random y coordinate from 0 -> screen height not including current
        # Snake Poistion
        rand_y = random.randint(
            0, 
            self.settings.window_height - self.settings.cell_size
        )
        while (
            rand_y >= self.snake.get_y_coord() and
            rand_y <= self.snake.get_y_coord() + self.settings.cell_size
        ):
            rand_y = random.randint(0, self.settings.window_height)

        # Update Snake Position
        self.x = rand_x
        self.y = rand_y
        self.rect = pygame.Rect(
            self.x, self.y, self.settings.cell_size, self.settings.cell_size
        ) 

    def check_collison(self):
        """Check for a collision with the snake."""

        if self.rect.colliderect(self.snake.rect):
            self.update_randomly()

