#!/usr/bin/env python
import argparse
import time

from led_matrix.color import Color
from led_matrix.glyph import Glyph
from led_matrix.program import Program


class DrawMessage(Program):
    """
    Display a user specified message on an LED Matrix
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__msg = kwargs.get("msg")

    def on_key_down(self, key_name, _):
        if key_name in ("q", "Q"):
            self.exit()

    def loop(self):
        """
        Display the message, redrawing periodically in a different color

        Args:
            matrix (LEDMatrix): The LEDMatrix to be controlled. Automatically
                                created by Program.
        """
        color = Color.random()

        self.matrix.display_string(1, 1, self.__msg, color, spacing=1)

        self.matrix.update()
        time.sleep(0.25)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Message")
    parser.add_argument("msg", type=str, help="The message to display")
    args = parser.parse_args()

    width = Glyph.strlen(args.msg, spacing=1) + 1
    height = Glyph.get("W").height + 2

    program = DrawMessage(width=width, height=height, title=args.msg, led_size=20, led_shape="circle", msg=args.msg)
    program.execute()
