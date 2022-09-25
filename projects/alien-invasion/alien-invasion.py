# Exiting
import sys
from time import sleep
# Game functionality
import pygame
# Import modules
from settings import settings_module
from games_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    # Game assets and behavior
    def __init__(self):
        # Init game and create resources
        pygame.init()
        self.settings = settings_module.Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")
        # Game Statistics and scoreboard display
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_alien_fleet()
        self.space_background = pygame.transform.scale(self.settings.background_image,
                            self.screen.get_size())
        # Button to start
        self.play_button = Button(self, "Play")

    def run_game(self):
        # Main Loop/started
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        # keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                self._check_play_button(mouse_position)

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_play_button(self, mouse_position):
        button_clicked = self.play_button.rect.collidepoint(mouse_position)

        if button_clicked and not self.stats.game_active:
            self.settings.init_dynamic_settings()

            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # Empty the background screen
            self.aliens.empty()
            self.bullets.empty()

            # Create new fleet
            self._create_alien_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # Check for bullet collisions on aliens
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self.bullets.empty()
            self._create_alien_fleet()
            self.settings.increase_speed()
            # Increase level
            self.stats.level += 1
            self.sb.prep_level()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        # update screen background
        self.screen.blit(self.space_background, (0, 0))
        self.ship.blitme()

        if not self.stats.game_active:
            self.play_button.draw_button()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        self.sb.score_display()
        # update screen
        pygame.display.flip()

    def _create_alien_fleet(self):
        if self.stats.game_active:
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            avaliable_space_x = self.settings.screen_width - (2 * alien_width)
            total_aliens_x = avaliable_space_x // (2 * alien_width)

            # Number of rows of fleet to fit on the screen
            ship_height = self.ship.rect.height
            avaliable_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
            total_rows = avaliable_space_y // (2 * alien_height)

            for row_number in range(total_rows):
                for number_alien in range(total_aliens_x):
                    self._create_alien(number_alien, row_number)

    def _create_alien(self, number_alien, row_number):
        if self.stats.game_active:
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            alien.x = alien_width + 2 * alien_width * number_alien
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
            self.aliens.add(alien)

    def _update_aliens(self):
        # Update alien position when it touches the edge of the screen
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        # Respond to fleet at the edge
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
            break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):

        if self.stats.ships_left > 0:
            # Decrement ships_left and update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()
            # Create a new fleet and center the ship.
            self._create_alien_fleet()
            self.ship.center_ship()
            # Pause.
            sleep(2)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break


if __name__ == '__main__':
    # Run the game
    ai = AlienInvasion()
    ai.run_game()
