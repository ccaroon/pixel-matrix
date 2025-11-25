#!/usr/bin/env python
import time

from pixel_matrix.color import Color
from pixel_matrix.program import Program

class PixelWalker(Program):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__x = 0
        self.__y = 0
        self.__color = Color.make("green")


    def loop(self):
        if self.__x <= self.matrix.width and self.__y <= self.matrix.height:
            self.matrix.set_pixel(self.__x, self.__y, self.__color)

            self.__x += 1

            if self.__x > self.matrix.width:
                self.__x = 0
                self.__y += 1

            self.matrix.update()
            time.sleep(0.05)


if __name__ == "__main__":
    program = PixelWalker(
        title = "Pixel Walker",
        width = 32, height = 32,
        pixel_size = 5,
        pixel_spacing = 5
    )
    program.execute()
