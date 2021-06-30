from models import base_obj
import pygame
"""person_obj class which defines persons and inherits from base_obj"""


class person_obj(base_obj):
    """person_obj class"""

    def __init__(self, image, pos, name):
        super().__init__(image, pos)
        self.name = name
        # self.title = title