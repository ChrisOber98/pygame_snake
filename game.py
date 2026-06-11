import pygame
import random

from settings import Settings
from snake import Snake, Direction
from apple import Apple
from tail import Tail

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
        self.move_timer = 0

        # Snake Sprite
        self.snake = Snake(self.settings, self)

        # Tail values
        self.tail = Tail(self.snake, self, self.settings)

        # Apple Sprite
        self.apple = Apple(self.snake, self.settings, self, self.tail)

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

        if event.key == pygame.K_w:
            if self.snake.previous_direction != Direction.DOWN:
                self.snake.direction = Direction.UP
        if event.key == pygame.K_s:
            if self.snake.previous_direction != Direction.UP:
                self.snake.direction = Direction.DOWN
        if event.key == pygame.K_a:
            if self.snake.previous_direction != Direction.RIGHT:
                self.snake.direction = Direction.LEFT
        if event.key == pygame.K_d:
            if self.snake.previous_direction != Direction.LEFT:
                self.snake.direction = Direction.RIGHT

    def update_screen(self):
        """Update the screen."""

        self.move_timer += self.clock.tick(self.settings.clock_timing)
        self.screen.fill(self.settings.screen_bg_color)
        self.check_eligable_move()
        self.check_out_of_bounds()
        self.apple.check_collison()
        self.apple.draw()
        self.tail.draw()
        self.snake.draw()
        pygame.display.flip()

    def check_out_of_bounds(self):
        """Check to see if snake has hit out of bounds."""

        # Calc max x and y coordinates for boundary checking
        max_x = self.settings.window_width - self.settings.cell_size
        max_y = self.settings.window_height - self.settings.cell_size

        # Check x bounds going off right of screen
        if self.snake.get_x_coord() > max_x:
            self.running = False
            
        # Check x bounds going off left of screen
        if self.snake.get_x_coord() < 0:
            self.running = False

        # Check y bounds going off top of screen
        if self.snake.get_y_coord() > max_y:
            self.running = False

        # Check y bounds going off bottom of screen
        if self.snake.get_y_coord() < 0:
            self.running = False

    def check_eligable_move(self):
        """Check if an eligabe move is ready to be executed."""

        if self.move_timer >= self.settings.move_timer:
            self.snake.update()
            self.tail.update()
            self.move_timer = 0





