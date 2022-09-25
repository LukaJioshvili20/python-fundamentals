import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        # Init Starting position of the ship
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Loading Ship Image
        self.image = pygame.image.load('settings/images/DurrrSpaceShip_2.bmp')
        self.rect = self.image.get_rect()
        # Ship location
        self.rect.midbottom = self.screen_rect.midbottom

        # horizontal position
        self.x = float(self.rect.x)
        # Flag for [ x ] movement - horizontal
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Update ship view position
        # Update x value from settings
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        # Draw ship to current location
        self.screen.blit(self.image, self.rect)
