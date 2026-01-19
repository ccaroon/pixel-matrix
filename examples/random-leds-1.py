#!/usr/bin/env python
import random

import pygame

from led_matrix.color import Color
from led_matrix.led_matrix import LEDMatrix

# Construct a LEDMatrix instance
matrix = LEDMatrix(title="Random LEDs #1", width=1024, height=768)

# Define the event loop. Must interact with pygame directly to get events.
# Then use the LEDMatrix instance, `matrix`, to control the LEDs.
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    row = random.randint(0, matrix.height - 1)
    col = random.randint(0, matrix.width - 1)

    color = Color.random()

    matrix.led_on(row, col, color)
    matrix.update()

matrix.quit()
