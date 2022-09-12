import pygame


class Ship:
    def __init__(self, ai_game):
        # Init Starting position of the ship
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Loading Ship Image
        self.image = pygame.image.load('settings/images/ship.bmp')
        self.rect = self.image.get_rect()
        # Ship location
        self.rect.midbottom = self.screen_rect.midbottom

        # Flag for movement
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Update ship view position
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        # Draw ship to current location
        self.screen.blit(self.image, self.rect)
