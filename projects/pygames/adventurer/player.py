import pygame
from support import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, surface, create_jump_particles):
        super().__init__()
        self.import_character_assets()
        # For picking image for each frame
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

        # Dust particles
        self.import_dust_run_particles()
        self.dust_frame_index = 0
        self.dust_animation_speed = 0.1
        self.display_surface = surface
        self.create_jump_particles = create_jump_particles
        # Player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

        # Player movement statues
        self.status = 'idle'
        self.facing_right = True
        self.collide_on_ground = False
        self.collide_on_ceiling = False
        self.collide_on_left = False
        self.collide_on_right = False

    def import_character_assets(self):
        character_path = 'graphics/character/'
        self.animations = {'idle': [], 'run': [], 'jump': [], 'fall': []}

        # Accessing folder of animations
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def import_dust_run_particles(self):
        self.dust_run_particles = import_folder('graphics/character/dust_particles/run')

    def run_dust_animation(self):
        if self.status == 'run':
            self.dust_frame_index += self.dust_animation_speed
            if self.dust_frame_index >= len(self.dust_run_particles):
                self.dust_frame_index = 0

            dust_particle = self.dust_run_particles[int(self.dust_frame_index)]

            if self.facing_right:
                pos = self.rect.bottomleft - pygame.math.Vector2(6, 10)
                self.display_surface.blit(dust_particle, pos)
            else:
                pos = self.rect.bottomright - pygame.math.Vector2(6, 10)
                flipped_dust_particle = pygame.transform.flip(dust_particle, True, False)
                self.display_surface.blit(flipped_dust_particle, pos)

    # Picking animation types
    def animate_character(self):
        animation = self.animations[self.status]
        # Looping trough frames
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

        # Set the Rect
        if self.collide_on_ground and self.collide_on_right:
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)
        elif self.collide_on_ground and self.collide_on_left:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.collide_on_ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        elif self.collide_on_ceiling and self.collide_on_right:
            self.rect = self.image.get_rect(topright=self.rect.topright)
        elif self.collide_on_ceiling and self.collide_on_left:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        elif self.collide_on_ceiling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.facing_right = False
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.facing_right = True
            self.direction.x = 1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            if self.collide_on_ground:
                self.jump()
                self.create_jump_particles(self.rect.midbottom)

    # Player movement Type ...
    def get_status(self):
        if self.direction.y < 0:
            self.status = "jump"
        elif self.direction.y > 1:
            self.status = "fall"
        else:
            if self.direction.x != 0:
                self.status = "run"
            else:
                self.status = "idle"

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.get_status()
        self.animate_character()
        self.run_dust_animation()
