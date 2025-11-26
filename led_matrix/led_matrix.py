import pygame

class LEDMatrix:
    DEFAULT_WIDTH = 1280
    DEFAULT_HEIGHT = 720

    LED_SHAPE_SQUARE = "square"
    LED_SHAPE_CIRCLE = "circle"
    VALID_LED_SHAPES = (
        LED_SHAPE_CIRCLE,
        LED_SHAPE_SQUARE
    )

    def __init__(self, **kwargs):
        """
        A Virtual LED Matrix.

        Can be used to simulate a physical LED Matrix.

        The LED Matrix's origin is at the top-left (0,0). The bottom-right
        is located at (width, height).

        Args:
            N/A

        KWArgs:
            width (int): Width of matrix in LEDs
            height (int): Height of matrix in LEDs
            title (str): Title for the LED Matrix Window
            led_size (int): The size of each LED (in pixels). Default: 1
            led_spacing (int): The spacing between LEDs (in pixels). Default: 0
            led_shape (str): LED_SHAPE_(SQUARE|CIRCLE). Default: SQUARE

        NOTE: The width & height of the GUI Window is dependent upon the LED
              size, shape and spacing.

        NOTE: LED Size == 1 for any shape LED => Single screen pixel
        """
        pygame.init()

        self.__led_size = kwargs.pop("led_size", 1)
        self.__led_shape = kwargs.pop("led_shape", self.LED_SHAPE_SQUARE).lower()
        self.__led_spacing = kwargs.pop("led_spacing", 0)

        self.__width = kwargs.pop("width", self.DEFAULT_WIDTH)
        self.__height = kwargs.pop("height", self.DEFAULT_HEIGHT)

        surface_width = (self.__width * self.__led_size) + (self.__led_spacing * (self.__width - 1))
        surface_height = (self.__height * self.__led_size) + (self.__led_spacing * (self.__height - 1))

        title = kwargs.pop("title", f"LED Matrix ({self.width},{self.height})")
        if title:
            pygame.display.set_caption(title)


        print(f"Surface Dims: ({surface_width}x{surface_height})")
        print(f"LED Dims: ({self.width},{self.height})")
        self.__surface = pygame.display.set_mode(
            (surface_width, surface_height)
        )


    @property
    def width(self):
        """ LED Matrix's width in LEDs """
        return self.__width


    @property
    def height(self):
        """ LED Matrix's height in LEDs """
        return self.__height


    def set_background(self, color):
        """
        Set the background color of the LED Matrix.

        NOTE: Does not turn on each LED. Sets the Virtual LED Matrix's Window
              background color.
        """
        self.__surface.fill(color)


    def set_led(self, led_x, led_y, color):
        """
        Set the LED at the given location to the given color

        Args:
            led_x (int): X coordinate of the LED
            led_y (int): Y coordinate of the LED
            color (pygame.Color): The color to set the LED to
        """
        if self.__led_size > 1:
            match self.__led_shape:
                case self.LED_SHAPE_CIRCLE:
                    offset = self.__led_size / 2

                    cx = (led_x * self.__led_size) + offset + (led_x * self.__led_spacing)
                    cy = (led_y * self.__led_size) + offset + (led_y * self.__led_spacing)

                    pygame.draw.circle(
                        self.__surface, color,
                        (cx, cy), self.__led_size / 2
                    )
                case self.LED_SHAPE_SQUARE:
                    rx = (led_x * self.__led_size) + (led_x * self.__led_spacing)
                    ry = (led_y * self.__led_size) + (led_y * self.__led_spacing)

                    pygame.draw.rect(
                        self.__surface, color,
                        pygame.Rect(rx, ry,
                            self.__led_size, self.__led_size
                        )
                    )
                case _:
                    raise ValueError(f"Unsupported value for led_shape: [{self.__led_shape}]")
        else:
            x = led_x + (led_x * self.__led_spacing)
            y = led_y + (led_y * self.__led_spacing)
            self.__surface.set_at((x, y), color)


    def update(self):
        """ Update the LED Matrix with the latest changes """
        pygame.display.flip()


    def quit(self):
        """ Quit the LED Matrix simulation and exit """
        pygame.quit()
