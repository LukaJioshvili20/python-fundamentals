# Exiting
import sys
# Game functionality
import pygame

# Import settings
from settings import settings_module


class AlienInvasion:
    # Game assets and behavior
    def __init__(self):
        # Init game and create resources
        pygame.init()
        self.settings = settings_module.Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        # Main Loop/started
        while True:
            # keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # update screen background
            self.screen.fill(self.settings.background_color)
            # update screen
            pygame.display.flip()


if __name__ == '__main__':
    # Run the game
    ai = AlienInvasion()
    ai.run_game()
