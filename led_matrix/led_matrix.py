import pygame

from led_matrix.glyph import Glyph
from led_matrix.led import LED


class LEDMatrix:
    DEFAULT_WIDTH = 1280
    DEFAULT_HEIGHT = 720

    VALID_LED_SHAPES = (LED.SHAPE_CIRCLE, LED.SHAPE_SQUARE)

    def __init__(self, **kwargs):
        """
        A Virtual LED Matrix.

        Can be used to simulate a physical LED Matrix.

        The LED Matrix's origin is at the top-left (0,0). The bottom-right
        is located at (width-1, height-1).

        Args:
            N/A

        KWArgs:
            width (int): Width of matrix in LEDs
            height (int): Height of matrix in LEDs
            title (str): Title for the LED Matrix Window
            led_size (int): The size of each LED (in pixels). Default: 1
            led_spacing (int): The spacing between LEDs (in pixels). Default: 0
            led_shape (str): LED.SHAPE_(SQUARE|CIRCLE). Default: SQUARE
            noframe (bool): If True, window will have no title, border or controls: Default: False

        NOTE: The width & height of the GUI Window is dependent upon the LED
              size, shape and spacing.

        NOTE: LED Size == 1 for any shape LED => Single screen pixel
        """
        pygame.init()

        self.__led_size = kwargs.pop("led_size", 1)
        self.__led_shape = kwargs.pop("led_shape", LED.SHAPE_SQUARE).lower()
        self.__led_spacing = kwargs.pop("led_spacing", 0)

        self.__width = kwargs.pop("width", self.DEFAULT_WIDTH)
        self.__height = kwargs.pop("height", self.DEFAULT_HEIGHT)

        self.__matrix = []
        self.__init_matrix()

        surface_width = (self.__width * self.__led_size) + (self.__led_spacing * (self.__width - 1))
        surface_height = (self.__height * self.__led_size) + (self.__led_spacing * (self.__height - 1))

        title = kwargs.pop("title", f"LED Matrix ({self.width},{self.height})")
        if title:
            pygame.display.set_caption(title)

        # print(f"Surface Dims: ({surface_width}x{surface_height})")
        # print(f"LED Dims: ({self.width},{self.height})")

        flags = 0
        if kwargs.get("noframe", False):
            flags |= pygame.NOFRAME

        self.__surface = pygame.display.set_mode((surface_width, surface_height), flags=flags)

    def __init_matrix(self):
        """
        Create/Init the matrix of LEDs
        """
        for row in range(self.__height):
            led_row = []
            for col in range(self.__width):
                match self.__led_shape:
                    case LED.SHAPE_CIRCLE:
                        offset = self.__led_size / 2

                        cx = (col * self.__led_size) + offset + (col * self.__led_spacing)
                        cy = (row * self.__led_size) + offset + (row * self.__led_spacing)

                        led_row.append(LED((cx, cy), self.__led_size / 2, self.__led_shape))
                    case LED.SHAPE_SQUARE:
                        rx = (col * self.__led_size) + (col * self.__led_spacing)
                        ry = (row * self.__led_size) + (row * self.__led_spacing)

                        led_row.append(LED((rx, ry), self.__led_size, self.__led_shape))
                    case _:
                        msg = f"Unsupported value for led_shape: [{self.__led_shape}]"
                        raise ValueError(msg)

            self.__matrix.append(led_row)

    @property
    def width(self):
        """LED Matrix's width in LEDs"""
        return self.__width

    @property
    def height(self):
        """LED Matrix's height in LEDs"""
        return self.__height

    def fill(self, color):
        # TODO: implement me
        """Fill the LED Matrix with the given color"""

    def set_background(self, color):
        """
        Set the background color of the LED Matrix.

        NOTE: Does not turn on each LED. Sets the Virtual LED Matrix's Window
              background color.
        """
        self.__surface.fill(color)

    def led_on(self, row, col, color):
        """
        Set the LED at the given location to the given color

        Args:
            row (int): Row num of the LED
            col (int): Col num of the LED
            color (pygame.Color): The color to set the LED to
        """
        led = self.__matrix[row][col]
        led.color = color

        if led.size > 1:
            match led.shape:
                case LED.SHAPE_CIRCLE:
                    pygame.draw.circle(self.__surface, color, led.position, led.size)
                case LED.SHAPE_SQUARE:
                    pygame.draw.rect(self.__surface, color, pygame.Rect(led.position, (led.size, led.size)))
                case _:
                    msg = f"Unsupported value for led_shape: [{self.__led_shape}]"
                    raise ValueError(msg)
        else:
            # Single Pixel
            x = col + (col * self.__led_spacing)
            y = row + (row * self.__led_spacing)
            self.__surface.set_at((x, y), color)

    def led_off(self, row, col):
        self.led_on(row, col, "black")

    def position_to_led(self, pos):
        """
        Convert the (x,y) point position to and LED (row,col)
        """
        x = pos[0]
        y = pos[1]

        row = y // (self.__led_size + self.__led_spacing)
        col = x // (self.__led_size + self.__led_spacing)

        return (row, col)

    def update(self):
        """Update the LED Matrix with the latest changes"""
        pygame.display.flip()

    def quit(self):
        """Quit the LED Matrix simulation and exit"""
        pygame.quit()

    def display_string(self, row, col, msg, color, **kwargs):
        chars = list(str(msg))
        spacing = kwargs.get("spacing", 0)
        for idx, char in enumerate(chars):
            glyph = Glyph.get(char)
            # TODO: don't space a space
            # TODO: not working
            # if char == " ":
            #     print(f"display_str: char = '{char}'")
            #     dx = row + (idx * glyph.width)
            # else:
            dc = col + (idx * glyph.width) + (spacing * idx)
            self.display_glyph(row, dc, glyph, color)

    def display_glyph(self, row, col, glyph, color):
        black = pygame.Color("black")
        for data in glyph:
            led_color = color if data["on"] else black
            self.led_on(data["row"] + row, data["col"] + col, led_color)


#
