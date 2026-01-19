#!/usr/bin/env python
import random

from led_matrix.color import Color
from led_matrix.program import Program


class RandomLEDs(Program):
    """
    A LEDMatrix Program that turns on random LEDs in random colors.

    Since it's defined as a sub-class of Program it can keep track of
    state and other behavior beyond what you can do with the `Program.exec_func`
    style of writing a LEDMatrix program.

    KWArgs
        Accepts all kwargs that are used by the LEDMatrix class in addition to
        your own arguments needed to initialize your Program. Arguments specific
        to LEDMatrix will be removed from the kwargs dict.
    """

    def __init__(self, **kwargs):
        # Remember to all super().__init__()
        super().__init__(**kwargs)

    # Automatically called by the event loop
    def loop(self):
        row = random.randint(0, self.matrix.height - 1)
        col = random.randint(0, self.matrix.width - 1)

        color = Color.random()

        self.matrix.led_on(row, col, color)
        self.matrix.update()


if __name__ == "__main__":
    program = RandomLEDs(title="Random LEDs #3", width=1920, height=1080)
    program.execute()
