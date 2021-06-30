import pygame
import itertools
# Base class for all pygame objects


DIM = (200, 200)


class base_obj():
    """base_obj class"""

    newid = itertools.count().next

    def __init__(self, image, pos):
        self.id = base_obj.newid()
        self.active = False
        self.image = pygame.transform.scale(pygame.image.load(image), DIM)
        self.pos = pygame.Rect(pos[0], pos[1], DIM[0], DIM[1])

    # def correct_message():

    # def wrong_message():

