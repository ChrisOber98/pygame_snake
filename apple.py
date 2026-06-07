import pygame
import random

class Apple:
    """Class to hold and represent a apple on the window."""

    def __init__(self, snake, settings, game):

        self.snake = snake
        self.settings = settings

        self.screen = game.screen

        self.x = 0
        self.y = 0
        self.height = 40
        self.width = 40
        self.color = 238, 75, 43

        self.update_randomly()

    def draw(self):
        """Draw Apple to screen."""

        pygame.draw.rect(
            self.screen, 
            self.color, 
            (self.x, self.y, self.width, self.height)
        )

    def update_randomly(self):
        """Update the apples position randomly taking into account the snake."""

        rand_x = random.randint(0, self.settings.window_width)
        while (
            rand_x <= self.snake.x and 
            rand_x >= self.snake.x + self.snake.width
        ):
            rand_x = random.randint(0, self.settings.window_width)
            
        rand_y = random.randint(0, self.settings.window_height)
        while (
            rand_y <= self.snake.y and 
            rand_y >= self.snake.y + self.snake.height
        ):
            rand_y = random.randint(0, self.settings.window_height)

        self.x = rand_x
        self.y = rand_y

