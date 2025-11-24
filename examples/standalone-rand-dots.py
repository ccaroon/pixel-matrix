#!/usr/bin/env python
import pygame
import random

from pixel_matrix.color import Color
from pixel_matrix.pixel_matrix import PixelMatrix

matrix = PixelMatrix(
    title = "Standalone Random Dots",
    width = 1024, height = 768
)

# Have to define own event loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    x = random.randint(0, matrix.width)
    y = random.randint(0, matrix.height)

    color = Color.random()

    matrix.set_pixel(x, y, color)
    matrix.update()


matrix.quit()
