#!/usr/bin/env python
import argparse
import datetime
import time

import zoneinfo

from led_matrix.color import Color
from led_matrix.glyph import Glyph
from led_matrix.program import Program


class DigitalClock(Program):
    """
    Display a Digital Clock.

    What Time Is it!?
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__color = Color.make(kwargs.get("color", "white"))

    def on_key_down(self, key_name, _):
        if key_name in ("q", "Q"):
            self.exit()

    def loop(self):
        """
        Display / Update the Time

        Args:
            matrix (LEDMatrix): The LEDMatrix to be controlled. Automatically
                                created by Program.
        """
        now = datetime.datetime.now(tz=zoneinfo.ZoneInfo("localtime"))
        time_str = f"{now.hour:2}:{now.minute:02}:{now.second:02}"

        self.matrix.display_string(1, 1, time_str, self.__color, spacing=1)

        self.matrix.update()
        time.sleep(0.5)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Digital Clock")
    parser.add_argument(
        "--color", "-c", type=str, default="chartreuse", help="The color of the digits. Default: Chartreuse"
    )
    parser.add_argument("--size", "-s", type=int, default=5, help="LED Size. Default: 5")
    args = parser.parse_args()

    width = Glyph.strlen("HH:MM:SS", spacing=1) + 1
    height = Glyph.get("X").height + 2

    print("Press 'Q' to exit!")  # noqa: T201
    program = DigitalClock(
        width=width,
        height=height,
        title="Digital Clock",
        noframe=True,
        led_size=args.size,
        led_shape="circle",
        led_spacing=1,
        color=args.color,
    )
    program.execute()
