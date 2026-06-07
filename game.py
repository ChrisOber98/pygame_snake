import pygame

class Game:
    """Class to hold representation of a game and its values / assets."""

    def __init__(self):
        """Initialize the game."""

        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("My Game")
        self.clock = pygame.time.Clock()

        self.running = True

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

        self.screen.fill((0, 0, 0))
        pygame.display.flip()
        self.clock.tick(60)