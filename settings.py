class Settings:
    """A class for holding game settings."""

    def __init__(self):
        """Initialze default values for game."""

        # Window Settings
        self.window_width = 765
        self.window_height = 503
        self.window_caption = "Snake Game"

        # Clock Settings
        self.clock_timing = 60

        # Screen Settings
        self.screen_bg_color = (0, 0, 0)


