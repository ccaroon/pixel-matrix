#!/usr/bin/env python
from pixel_matrix.color import Color
from pixel_matrix.program import Program

import random

class RandomLines(Program):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def loop(self):
        sx = random.randint(0, self.matrix.width)
        sy = random.randint(0, self.matrix.height)

        ex = random.randint(0, self.matrix.width)
        ey = random.randint(0, self.matrix.height)

        color = Color.random()

        self.matrix.line((sx,sy), (ex,ey), color)
        self.matrix.update()



if __name__ == "__main__":
    program = RandomLines(
        title = "Random Lines",
        width = 1920, height = 1080
    )
    program.execute()
