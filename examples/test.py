#!/usr/bin/env python
import argparse

from led_matrix.color import Color
from led_matrix.led import LED
from led_matrix.led_matrix import LEDMatrix
from led_matrix.program import Program


class LEDTester(Program):
    def __init__(self, **kwargs):
        # LEDMatrix options are removed from kwargs when super().__init__()
        # is called.
        super().__init__(**kwargs)

        self.__count = 0

    def on_click_led(self, pos):
        self.matrix.led_on(pos[0], pos[1], Color.random())
        self.matrix.update()

    def loop(self):
        pass
        # self.matrix.led_on(0, 0, "red")
        # self.matrix.led_on(self.matrix.height - 1, self.matrix.width - 1, "green")

        # if self.__count % 2 == 0:
        #     self.matrix.led_on(5, 5, "purple")
        # else:
        #     self.matrix.led_off(5, 5)

        # self.matrix.update()
        # self.__count += 1
        # time.sleep(0.50)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LED Tester")

    parser.add_argument("--width", "-w", type=int, default=10, help="LED Matrix Width")
    parser.add_argument("--height", "-g", type=int, default=10, help="LED Matrix Height")
    parser.add_argument("--size", "-s", type=int, default=25, help="LED Size")
    parser.add_argument("--spacing", "-p", type=int, default=1, help="Space between LEDs")
    parser.add_argument(
        "--shape", "-a", choices=(LEDMatrix.VALID_LED_SHAPES), default=LED.SHAPE_CIRCLE, help="LED Shape"
    )

    args = parser.parse_args()

    program = LEDTester(
        title="LED Tester",
        width=args.width,
        height=args.height,
        led_size=args.size,
        led_spacing=args.spacing,
        led_shape=args.shape,
    )
    program.execute()


#
