class LED:
    SHAPE_CIRCLE = "circle"
    SHAPE_SQUARE = "square"

    def __init__(self, position, size, shape, color=(0, 0, 0)):
        """
        Virtual LED

        Args:
            position (tuple): LED's (x,y) position. Top/Left for Square. Center for Circle.
            size (int): The size of the LED. Radius if Circle; Width/Height if Retangle.
            color (): The LED's  initial color
        """
        self.__position = position
        self.__size = size
        self.__shape = shape
        self.color = color

    @property
    def position(self):
        return self.__position

    @property
    def shape(self):
        return self.__shape

    @property
    def size(self):
        return self.__size

    def __point_in_circle(self, point):
        px = point[0]
        py = point[1]
        center_x = self.__position[0]
        center_y = self.__position[1]

        d2 = (px - center_x) ** 2 + (py + center_y) ** 2

        return d2 <= self.__size**2

    def __point_in_rect(self, point):
        px = point[0]
        py = point[1]
        rect_x = self.__position[0]
        rect_y = self.__position[1]

        return (px >= rect_x and px <= rect_x + self.__size) and (py >= rect_y and py <= rect_y + self.__size)

    def point_in_led(self, point):
        """
        Determine if the point(x,y) is inside the LED
        """
        return self.__point_in_circle(point) if self.__shape == self.SHAPE_CIRCLE else self.__point_in_rect(point)


#
