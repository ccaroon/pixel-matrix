from abc import ABC, abstractmethod

import pygame

from led_matrix.led_matrix import LEDMatrix


class Program(ABC):
    def __init__(self, **kwargs):
        self.__matrix = LEDMatrix(**kwargs)

    @property
    def matrix(self):
        return self.__matrix

    def on_click_led(self, position):
        """
        Event handler for when an LED is clicked on

        Args:
            position (tuple): (row,col) coordinate of the LED clicked
        """

    def on_mouse_down(self, position):
        """
        Event Handler for Mouse Down

        Args:
            position (tuple): (x, y) coordinate of click mouse down event
        """

    def on_key_down(self, key_name, modifier):
        """
        Event Handler for Key Down

        Args:
            key_name (str): The descriptive name of the key pressed. I.e. "q" | "left" | "space"
            modifier (int): The code of the modifier key that was pressed along with the key. Alt, Shift, Control, etc.

        See:
            * https://www.pygame.org/docs/ref/key.html
        """

    def wait_for(self, event_type):
        while (event := pygame.event.wait()).type != event_type:
            if event.type == pygame.QUIT:
                self.exit()

    @abstractmethod
    def loop(self):
        """Your LEDMatrix Program's main loop."""

    def execute(self):
        """Start the Program Running"""
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.on_mouse_down(pos)

                    led_pos = self.matrix.position_to_led(pos)
                    self.on_click_led(led_pos)
                elif event.type == pygame.KEYDOWN:
                    key_name = pygame.key.name(event.key)
                    # print(f"Key [{event.key}][{key_name}] | Mod [{event.mod}]")
                    self.on_key_down(key_name, event.mod)

            self.loop()

        self.matrix.quit()

    def exit(self):
        pygame.event.post(pygame.event.Event(pygame.QUIT))

    @classmethod
    def exec_func(cls, program_func, **kwargs):
        """Execute a function as a LED Matrix Program"""

        class FuncProgram(Program):
            def loop(self):
                program_func(self.matrix)

        program = FuncProgram(**kwargs)
        program.execute()


#
