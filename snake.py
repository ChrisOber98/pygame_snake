import pygame

class Snake:
    """A class that holds a snake sprite for playing."""

    def __init__(self, settings, game):
        """Initialize default snake sprite."""

        # Settings values
        self.settings = settings

        # Game Values
        self.screen = game.screen

        # Positional Values
        self.col = 0
        self.row = 0

        # Rect Value
        self.rect = pygame.Rect(
            self.get_x_coord(), 
            self.get_y_coord(), 
            self.settings.cell_size, 
            self.settings.cell_size
        )

        # Color Values
        self.color = self.settings.snake_color

        # Directional Values
        self.is_moving_down = False
        self.is_moving_up = False
        self.is_moving_left = False
        self.is_moving_right = False

        # Previous Value
        self.previous_rect = None

    def draw(self):
        """Draw Snake to screen."""

        pygame.draw.rect(
            self.screen, 
            self.settings.snake_color, 
            self.rect
        )

    def update(self):
        """Update snake position."""

        self.previous_rect= self.rect

        if self.is_moving_down:
            self.row += self.settings.snake_speed
        if self.is_moving_up:
            self.row -= self.settings.snake_speed
        if self.is_moving_left:
            self.col -= self.settings.snake_speed
        if self.is_moving_right:
            self.col += self.settings.snake_speed

        self.rect = pygame.Rect(
            self.get_x_coord(), 
            self.get_y_coord(), 
            self.settings.cell_size, 
            self.settings.cell_size
        )

    def reset_movement(self):
        """Reset the snakes movement variables to all False."""

        self.is_moving_down = False
        self.is_moving_up = False
        self.is_moving_left = False
        self.is_moving_right = False


    def get_x_coord(self):
        """Takes the grid representation and returns x coord."""

        return self.col * self.settings.cell_size
    
    def get_y_coord(self):
        """Takes the grid representation and returns y coord."""

        return self.row * self.settings.cell_size
  




    

