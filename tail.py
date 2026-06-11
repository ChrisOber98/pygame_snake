import pygame

from collections import deque

class Tail:
    """Class to store tail for snake."""

    def __init__(self, snake, game, settings):
        """Initialize default tail values."""

        # Screen Values
        self.game = game
        self.screen = game.screen

        # Setting Values
        self.settings = settings

        # Snake Values
        self.head = snake

        # Tail Values
        self.tail = []

    def draw(self):
        """Draw the tail to the screen."""

        for body in self.tail:
            pygame.draw.rect(
                self.screen, 
                self.settings.snake_color, 
                body
            )

    def add_body_to_tail(self, rect):
        """Add a rect """

        self.tail.insert(0, rect)

    def update(self):
        """Update all body members in the tail."""

        if len(self.tail) == 0:
            return
        elif len(self.tail) == 1:
            self.tail[0] = self.head.previous_rect
        else:
            prev = self.tail[0]
            self.tail[0] = self.head.previous_rect

            for i in range(1, len(self.tail)):
                temp = self.tail[i]
                self.tail[i] = prev
                prev = temp

    def check_collision_w_head(self):
        """Check for a collision with the head."""

        if self.head in self.tail:
            self.game.running = False


        
