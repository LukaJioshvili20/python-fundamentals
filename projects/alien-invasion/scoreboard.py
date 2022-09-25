import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings
        self.text_color = (156, 12, 4)
        self.font = pygame.font.SysFont(None, 48)

        # Prep score image
        self.prep_score()
        self.prep_level()
        self.prep_ships()
        self.prep_high_score()

    def prep_score(self):
        # Rounding to the nearset 10
        rounded_score = round(self.stats.score, -1)
        # 1000 to 1,000 formatter
        score_string = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_string, True, self.text_color, self.settings.background_color)

        # Scoreboard position
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def score_display(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
            self.prep_level()

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_string = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_string, True, self.text_color,
                                                 self.settings.background_color)

        # Centering High score
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        level_string = str(self.stats.level)
        self.level_image = self.font.render(level_string, True, self.text_color, self.settings.background_color)

        # Position the level
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)