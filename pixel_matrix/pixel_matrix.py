import pygame

class PixelMatrix:
    DEFAULT_WIDTH = 1280
    DEFAULT_HEIGHT = 720

    PIXEL_SHAPE_SQUARE = "square"
    PIXEL_SHAPE_CIRCLE = "circle"

    def __init__(self, **kwargs):
        """
        Origin:
            The Pixel Matrix's origin is at the top-left (0,0). The bottom-right
            is located at (width,height).

        Args:

        KWArgs:
            width (int): Width of matrix in pixels
            height (int): Height of matrix in pixels
            title (str): Title for the Graphix Window
            pixel_size (int): The size of each pixel. Default: 1
            pizel_spacing (int): The spacing between pixels. Default: 0
            pixel_shape (str): PIXEL_SHAPE_(SQUARE|CIRCLE). Default: SQUARE

        NOTE: Pixel Size == 1 for any shape pixel => Single Dot
        """
        pygame.init()

        self.__pixel_size = kwargs.pop("pixel_size", 1)
        self.__pixel_shape = kwargs.pop("pixel_shape", self.PIXEL_SHAPE_SQUARE)
        self.__pixel_spacing = kwargs.pop("pixel_spacing", 0)

        # TODO: calc based on size, spacing, etc
        self.__width = kwargs.pop("width", self.DEFAULT_WIDTH)
        self.__height = kwargs.pop("height", self.DEFAULT_HEIGHT)

        surface_width = (self.__width * self.__pixel_size) + (self.__pixel_spacing * (self.__width - 1))
        surface_height = (self.__height * self.__pixel_size) + (self.__pixel_spacing * (self.__height - 1))

        title = kwargs.pop("title", f"Pixel Matrix ({self.width},{self.height})")
        if title:
            pygame.display.set_caption(title)


        print(f"Surface ({surface_width}x{surface_height})")
        self.__surface = pygame.display.set_mode(
            (surface_width, surface_height)
        )


    @property
    def width(self):
        return self.__width


    @property
    def height(self):
        return self.__height


    def set_background(self, color):
        self.__surface.fill(color)


    def set_pixel(self, px, py, color):
        if self.__pixel_size > 1:
            match self.__pixel_shape:
                case self.PIXEL_SHAPE_CIRCLE:
                    cx = px
                    cy = py
                    pygame.draw.circle(
                        self.__surface, color,
                        (cx,cy), self.__pixel_size / 2
                    )
                case self.PIXEL_SHAPE_SQUARE:
                    rx = (px * self.__pixel_size) + (px * self.__pixel_spacing)
                    ry = (py * self.__pixel_size) + (py * self.__pixel_spacing)

                    pygame.draw.rect(
                        self.__surface, color,
                        pygame.Rect(rx, ry,
                            self.__pixel_size, self.__pixel_size
                        )
                    )
                    # print(f"[{rx},{ry}]")
                case _:
                    raise ValueError(f"Unsupported value for pixel_shape: [{self.__pixel_shape}]")
        else:
            self.__surface.set_at((px, py), color)


    def line(self, start_pos, end_pos, color):
        pygame.draw.line(self.__surface, color, start_pos, end_pos)


    def update(self):
        pygame.display.flip()


    def quit(self):
        pygame.quit()






#
