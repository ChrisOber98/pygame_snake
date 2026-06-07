import pygame

from settings import Settings
from snake import Snake

class Game:
    """Class to hold representation of a game and its values / assets."""

    def __init__(self):
        """Initialize the game."""

        # Initial set up
        self.settings = Settings()
        pygame.init()

        # Screen set up
        self.screen = pygame.display.set_mode(
            (self.settings.window_width, self.settings.window_height)
        )
        pygame.display.set_caption(self.settings.window_caption)

        # Clock Set Up 
        self.clock = pygame.time.Clock()

        # Global Variables set up
        self.running = True

        # Snake Sprite
        self.snake = Snake(self)

    def run_game(self):
        """Handles running / maintaining game loop."""

        while self.running:

            self.handle_events()
            self.update_screen()

    def handle_events(self):
        """Function to get events and handle them."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update_screen(self):
        """Update the screen."""

        self.screen.fill(self.settings.screen_bg_color)
        self.snake.draw()
        pygame.display.flip()
        self.clock.tick(self.settings.clock_timing)