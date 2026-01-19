#!/usr/bin/env python
import argparse
import time

from led_matrix.color import Color
from led_matrix.program import Program


class BinaryClock(Program):
    """
    Display a Binary Clock.
    """

    HOUR_LEDS = (
        ((0, 0), (0, 1), (0, 2), (0, 3)),
        ((1, 0), (1, 1), (1, 2), (1, 3)),
    )

    MINUTE_LEDS = (
        ((2, 0), (2, 1), (2, 2), (2, 3)),
        ((3, 0), (3, 1), (3, 2), (3, 3)),
    )

    SECOND_LEDS = (
        ((4, 0), (4, 1), (4, 2), (4, 3)),
        ((5, 0), (5, 1), (5, 2), (5, 3)),
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__curr_hour = None
        self.__curr_min = None
        self.__curr_sec = None

        colors = kwargs.get("colors", ("red", "green", "blue"))
        self.__color_set = (Color.make(colors[0]), Color.make(colors[1]), Color.make(colors[2]))
        self.__off = Color.make("black")

    def on_key_down(self, key_name, _):
        if key_name in ("q", "Q"):
            self.exit()

    def __set_number(self, number, led_set, on_color):
        # 1. split into digits
        d0 = int(number / 10)
        d1 = number % 10

        # 2. convert digit to binary string, zero-padded to 4 places
        d0_bin = f"{d0:04b}"
        d1_bin = f"{d1:04b}"

        # 3. display on matrix
        for digit, bin_str in enumerate((d0_bin, d1_bin)):
            for idx, bin_value in enumerate(bin_str):
                color = None

                color = self.__off if int(bin_value) == 0 else on_color

                col = led_set[digit][idx][0]
                row = led_set[digit][idx][1]

                self.matrix.led_on(row, col, color)

    def loop(self):
        """
        Display / Update the Time

        Args:
            matrix (LEDMatrix): The LEDMatrix to be controlled. Automatically
                                created by Program.
        """
        now = time.localtime()

        if now.tm_hour != self.__curr_hour:
            self.__curr_hour = now.tm_hour
            self.__set_number(now.tm_hour, self.HOUR_LEDS, self.__color_set[0])

        if now.tm_min != self.__curr_min:
            self.__curr_min = now.tm_min
            self.__set_number(now.tm_min, self.MINUTE_LEDS, self.__color_set[1])

        if now.tm_sec != self.__curr_sec:
            self.__curr_sec = now.tm_sec
            self.__set_number(now.tm_sec, self.SECOND_LEDS, self.__color_set[2])

        self.matrix.update()


if __name__ == "__main__":
    COLOR_CNT = 3
    parser = argparse.ArgumentParser(description="Binary Clock")
    parser.add_argument(
        "--colors",
        "-c",
        type=str,
        default="red,green,blue",
        help="Color Set for the Hour,Min,Sec. Default: red,green,blue",
    )
    parser.add_argument("--size", "-s", type=int, default=50, help="LED Size. Default: 50")
    args = parser.parse_args()

    colors = args.colors.split(",", COLOR_CNT)
    if len(colors) != COLOR_CNT:
        msg = "Please specify --colors as a comma separated list of three colors."
        raise ValueError(msg)

    print("Press 'Q' to exit!")  # noqa: T201
    program = BinaryClock(
        width=6,
        height=4,
        title="Binary Clock",
        noframe=True,
        led_size=args.size,
        led_shape="circle",
        led_spacing=20,
        colors=colors,
    )
    program.execute()
