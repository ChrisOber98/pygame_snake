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
        self.is_holding_key_down = False

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
            if event.type == pygame.KEYDOWN:
                self.snake.reset_movement()
                if event.key == pygame.K_w:
                    self.snake.is_moving_up = True
                if event.key == pygame.K_s:
                    self.snake.is_moving_down = True
                if event.key == pygame.K_a:
                    self.snake.is_moving_left= True
                if event.key == pygame.K_d:
                    self.snake.is_moving_right = True
            if event.type == pygame.KEYUP:
                pass

    def update_screen(self):
        """Update the screen."""

        self.screen.fill(self.settings.screen_bg_color)
        self.snake.update()
        self.snake.draw()
        pygame.display.flip()
        self.clock.tick(self.settings.clock_timing)