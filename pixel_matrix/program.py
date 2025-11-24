import pygame

from abc import ABC, abstractmethod

from pixel_matrix.pixel_matrix import PixelMatrix

class Program(ABC):
    def __init__(self, **kwargs):
        self.__matrix = PixelMatrix(**kwargs)


    @property
    def matrix(self):
        return self.__matrix


    @abstractmethod
    def loop(self, pixel_matrix):
        """  Your PixelMatrix Program's main loop. """


    def execute(self):
        """ Start the Program Running """
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.loop()

        self.matrix.quit()


    @classmethod
    def exec_func(cls, program_func, **kwargs):
        """ Execute a function as a Pixel Matrix Program """
        class FuncProgram(Program):
            def loop(self):
                program_func(self.matrix)


        program = FuncProgram(**kwargs)
        program.execute()




#
