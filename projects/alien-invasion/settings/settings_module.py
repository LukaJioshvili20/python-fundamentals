class Settings:
    # Settings store for game
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (230, 230, 230)
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
