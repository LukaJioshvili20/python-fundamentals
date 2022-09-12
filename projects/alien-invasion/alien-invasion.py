# Exiting
import sys
# Game functionality
import pygame


class AlienInvasion:
    # Game assets and behavior
    def __init__(self):
        # Init game and create resources
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        self.background_color = (230, 230, 230)
    def run_game(self):
        # Main Loop/started
        while True:
            # keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # update screen background
            self.screen.fill(self.background_color)
            # update screen
            pygame.display.flip()


if __name__ == '__main__':
    # Run the game
    ai = AlienInvasion()
    ai.run_game()
