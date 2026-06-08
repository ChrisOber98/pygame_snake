class Settings:
    """A class for holding game settings."""

    def __init__(self):
        """Initialze default values for game."""

        # Window Settings
        self.window_width = 760
        self.window_height = 500
        self.window_caption = "Snake Game"

        # Clock Settings
        self.clock_timing = 60
        self.move_timer = 100

        # Screen Settings
        self.screen_bg_color = (0, 0, 0)

        # Cell Settings
        self.cell_size = 20

        # Apple Settings
        self.apple_color = (238, 75, 43)

        # Snake Settings
        self.snake_color = (255, 234, 0)
        self.snake_speed = 1


