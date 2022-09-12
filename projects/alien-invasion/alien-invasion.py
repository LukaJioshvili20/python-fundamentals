# Exiting
import sys
# Game functionality
import pygame

# Import modules
from settings import settings_module
from ship import Ship


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

        self.ship = Ship(self)

    def run_game(self):
        # Main Loop/started
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        # keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # update screen background
        self.screen.fill(self.settings.background_color)
        self.ship.blitme()

        # update screen
        pygame.display.flip()


if __name__ == '__main__':
    # Run the game
    ai = AlienInvasion()
    ai.run_game()
