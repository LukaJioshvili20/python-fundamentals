import pygame
# for File systems
from os import walk

import pygame.image


def import_folder(path):
    surface_list = []
    # Underscores for not needed props
    for (_, __, img_files) in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)
    return surface_list
