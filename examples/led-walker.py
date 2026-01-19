#!/usr/bin/env python
import argparse
import time

import pygame

from led_matrix.color import Color
from led_matrix.led import LED
from led_matrix.led_matrix import LEDMatrix
from led_matrix.program import Program


class LEDWalker(Program):
    def __init__(self, **kwargs):
        # LEDMatrix options are removed from kwargs when super().__init__()
        # is called.
        super().__init__(**kwargs)

        # Variables/state relevant to our program
        self.__col = 0
        self.__row = 0
        self.__color = Color.make(kwargs.get("color", "green"))
        self.__delay = kwargs.get("delay", 0.025)

    def loop(self):
        if self.__col < self.matrix.width and self.__row < self.matrix.height:
            self.matrix.led_on(self.__row, self.__col, self.__color)

            self.__col += 1

            if self.__col >= self.matrix.width:
                self.__col = 0
                self.__row += 1

            self.matrix.update()
            time.sleep(self.__delay)
        else:
            print("Sequence Complete! Close the window to exit.")  # noqa: T201
            self.wait_for(pygame.MOUSEBUTTONDOWN)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LED Walker")

    parser.add_argument("--width", "-w", type=int, default=64, help="LED Matrix Width")
    parser.add_argument("--height", "-g", type=int, default=64, help="LED Matrix Height")
    parser.add_argument("--size", "-s", type=int, default=10, help="LED Size")
    parser.add_argument("--spacing", "-p", type=int, default=1, help="Space between LEDs")
    parser.add_argument("--delay", "-d", type=float, default=0.025, help="Delay between lighting each LED")
    parser.add_argument(
        "--shape", "-a", choices=(LEDMatrix.VALID_LED_SHAPES), default=LED.SHAPE_SQUARE, help="LED Shape"
    )
    parser.add_argument(
        "--color", "-c", type=str, default="green", help="Color of each LED: 'red', '0xffffff', '#00ffff', etc"
    )

    args = parser.parse_args()

    program = LEDWalker(
        title="LED Walker",
        width=args.width,
        height=args.height,
        led_size=args.size,
        led_spacing=args.spacing,
        led_shape=args.shape,
        color=args.color,
        delay=args.delay,
    )
    program.execute()


#
