import pygame
from pygame.sprite import Sprite


if __name__ == "__main__":
    

class Alien(Sprite):
    # Single Alien
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Load Alien image and set its rect attribute
        self.image = pygame.image.load('settings/images/xenis-orange-c-1.bmp')
        self.rect = self.image.get_rect()

        # Alien default position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Saving/Storing alien's X position
        self.x = float(self.rect.x)

    # Check if is at the edge of the screen
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        # Alien movement
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
