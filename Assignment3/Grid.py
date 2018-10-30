import random
from Assignment3.Cell import *


class Grid:
    def __init__(self, height, width):
        self.height = 50
        self.width = 50
        self.grid = []
        self.flatP = 0.2
        self.hillP = 0.3
        self.forestP = 0.3
        self.caveP = 0.2


    def generateGrid(self):
        for i in range(self.height):
            for j in range(self.width):
                rNum = random.random()
                # [0.0,0.2)
                if 0 <= rNum < self.flatP:
                    cell = Cell(1)
                    self.grid.append(cell)
                # [0.2,0.5)
                elif self.flatP <= rNum < self.flatP+self.hillP:
                    cell = Cell(2)
                    self.grid.append(cell)
                # [0.5,0.8)
                elif self.flatP+self.hillP <= rNum < self.flatP+self.hillP+self.forestP:
                    cell = Cell(3)
                    self.grid.append(cell)
                # [0.8,1.0)
                else:
                    cell = Cell(4)
                    self.grid.append(cell)
