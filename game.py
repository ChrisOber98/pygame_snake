import pygame
import random

from settings import Settings
from snake import Snake
from apple import Apple

class Game:
    """Class to hold representation of a game and its values / assets."""

    def __init__(self):
        """Initialize the game."""

        # Initial set up
        pygame.init()

        # Setting Values
        self.settings = Settings()

        # Screen Set Up
        self.screen = pygame.display.set_mode(
            (self.settings.window_width, self.settings.window_height)
        )
        pygame.display.set_caption(self.settings.window_caption)

        # Clock Set Up 
        self.clock = pygame.time.Clock()

        # Global Variables
        self.running = True
        self.is_holding_key_down = False

        # Snake Sprite
        self.snake = Snake(self.settings, self)

        # Apple Sprite
        self.apple = Apple(self.snake, self.settings, self)

    def run_game(self):
        """Handles running / maintaining game loop."""

        while self.running:
            self.handle_events()
            self.update_screen()

    def handle_events(self):
        """Function to get events and handle them."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handle_event_quit()
            if event.type == pygame.KEYDOWN:
                self.handle_event_keydown(event)
            if event.type == pygame.KEYUP:
                pass

    def handle_event_quit(self):
        """Handles what happens when pygame.QUIT happens."""

        self.running = False

    def handle_event_keydown(self, event):
        """Handles what happens when pygame.KEYDOWN happens."""

        self.snake.reset_movement()

        if event.key == pygame.K_w:
            self.snake.is_moving_up = True
        if event.key == pygame.K_s:
            self.snake.is_moving_down = True
        if event.key == pygame.K_a:
            self.snake.is_moving_left= True
        if event.key == pygame.K_d:
            self.snake.is_moving_right = True

    def update_screen(self):
        """Update the screen."""

        self.screen.fill(self.settings.screen_bg_color)
        self.snake.update()
        self.check_out_of_bounds()
        self.apple.draw()
        self.snake.draw()
        pygame.display.flip()
        self.clock.tick(self.settings.clock_timing)

    def check_out_of_bounds(self):
        """Check to see if snake has hit out of bounds."""

        # Check x bounds going off right of screen
        if self.snake.x > self.settings.window_width - self.settings.cell_size:
            self.running = False
            
        # Check x bounds going off left of screen
        if self.snake.x < 0:
            self.running = False

        # Check y bounds going off top of screen
        if self.snake.y > self.settings.window_height - self.settings.cell_size:
            self.running = False

        # Check y bounds going off bottom of screen
        if self.snake.y < 0:
            self.running = False



