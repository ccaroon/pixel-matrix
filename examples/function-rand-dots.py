#!/usr/bin/env python
from pixel_matrix.color import Color
from pixel_matrix.program import Program

import random

def random_dots(matrix):
    x = random.randint(0, matrix.width)
    y = random.randint(0, matrix.height)

    color = Color.random()

    matrix.set_pixel(x, y, color)
    matrix.update()


Program.exec_func(
    random_dots,
    width=1024, height=1024,
    title="Random Dots"
)
