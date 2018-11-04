import random
from Assignment3.Cell import *


class Grid:
    def __init__(self, N):
        self.N = N #50
        self.grid = []
        self.flatP = 0.2
        self.hillP = 0.3
        self.forestP = 0.3
        self.caveP = 0.2
        self.generateGrid()

    def generateGrid(self):
        for i in range(self.N):
            for j in range(self.N):
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
        targeti = random.randint(0,49)
        targetj = random.randint(0,49)
        self.getCell(targeti,targetj).isTarget = True
    def getCell(self, x, y):
        return self.grid[x * self.N + y]