import pygame
import random

class Apple:
    """Class to hold and represent a apple on the window."""

    def __init__(self, snake, settings, game, tail):
        """Inits defualt values for apple entity."""

        # Snake Values
        self.snake = snake

        # Setting Values
        self.settings = settings

        # Game Values
        self.screen = game.screen

        # Tail Values
        self.tail = tail

        # Apple Values
        self.col = 0
        self.row = 0
        self.color = self.settings.apple_color

        # Create Rect
        self.rect = pygame.Rect(
            self.get_x_coord(), 
            self.get_y_coord(), 
            self.settings.cell_size, 
            self.settings.cell_size
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

        # Get Random col # from 0 -> num of cols
        num_of_cols = int(self.settings.window_width / self.settings.cell_size)
        rand_col = random.randint(0, num_of_cols - 1)
        while (rand_col == self.snake.col):
            rand_col = random.randint(0, num_of_cols)

            
        # Get Random row # from 0 -> num of rows
        num_of_rows = int(self.settings.window_height / self.settings.cell_size)
        rand_row = random.randint(0, num_of_rows - 1)
        while (rand_row == self.snake.row):
            rand_row = random.randint(0, num_of_rows)

        # Update Snake Position
        self.col = rand_col
        self.row = rand_row
        self.rect = pygame.Rect(
            self.get_x_coord(), 
            self.get_y_coord(), 
            self.settings.cell_size, 
            self.settings.cell_size
        ) 

    def check_collison(self):
        """Check for a collision with the snake."""

        if self.rect.colliderect(self.snake.rect):
            self.update_randomly()
            self.tail.add_body_to_tail(self.snake.previous_rect)

    def get_x_coord(self):
        """Takes the grid representation and returns x coord."""

        return self.col * self.settings.cell_size
    
    def get_y_coord(self):
        """Takes the grid representation and returns y coord."""

        return self.row * self.settings.cell_size

