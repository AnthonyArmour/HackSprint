from models import base_obj
import pygame
"""question class which defines tech and inherits from base_obj"""


class question(base_obj):
    """question class"""

    def __init__(self, image, pos, obj_id):
        super().__init__(image, pos)
        # self.question = question
        self.obj_id = obj_id