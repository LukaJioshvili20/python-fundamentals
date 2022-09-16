import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # Single Alien
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        # Load Alien image and set its rect attribute
        self.image = pygame.image.load('settings/images/alien.bmp')
        self.rect = self.image.get_rect()

        # Alien default positon
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Saving/Storing alien's X position
        self.x = float(self.rect.x)
