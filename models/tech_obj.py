from models import base_obj
import pygame
"""tech_obj class which defines tech and inherits from base_obj"""


class tech_obj(base_obj):
    """tech_obj class"""

    def __init__(self, image, pos, name):
        super().__init__(image, pos)
        self.name = name
        # self.question_id = question_id