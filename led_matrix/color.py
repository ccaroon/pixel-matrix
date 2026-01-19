import random

import pygame


class Color:
    @classmethod
    def make(cls, value):
        return pygame.Color(value)

    @classmethod
    def random(cls):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        return cls.make((r, g, b))
