import pygame.font


class Button:
    def __init__(self, ai_game, message):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 75
        self.button_color = (156, 12, 4)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Centering button
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_message(message)

    def _prep_message(self, message):
        self.message_image = self.font.render(message,True, self.text_color, self.button_color)
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect)
