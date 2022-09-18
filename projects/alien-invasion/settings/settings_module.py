class Settings:
    # Settings store for game
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # Alien Settings
        self.fleet_drop_speed = 10

        # Game speed
        self.speedup_scale = 1.1
        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 1.0
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
