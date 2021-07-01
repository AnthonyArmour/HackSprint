import pygame
"""person_obj class which defines persons and inherits from base_obj"""
DIM = (200, 200)


class person_obj():
    """person_obj class"""

    def __init__(self, images, pos, name):
        self.name = name
        self.active = False
        self.image_1 = pygame.transform.scale(pygame.image.load(images[0]), DIM)
        self.image_2 = pygame.transform.scale(pygame.image.load(images[1]), DIM)
        self.image_3 = pygame.transform.scale(pygame.image.load(images[2]), DIM)
        self.pos = pygame.Rect(pos[0], pos[1], DIM[0], DIM[1])

class tech_obj():
    """Tech obj class"""

    def __init__(self, images, pos, name):
        self.name = name
        self.active = False
        self.image_1 = pygame.transform.scale(pygame.image.load(images[0]), DIM)
        self.image_2 = pygame.transform.scale(pygame.image.load(images[1]), DIM)
        self.image_3 = pygame.transform.scale(pygame.image.load(images[2]), DIM)
        self.pos = pygame.Rect(pos[0], pos[1], DIM[0], DIM[1])

class question():
    """question class"""

    def __init__(self, image, pos, obj_name):
        self.image = pygame.transform.scale(pygame.image.load(image), (300, 200))
        self.pos = pygame.Rect(pos[0], pos[1], 300, 200)
        self.name_id = obj_name
        self.correct = False
