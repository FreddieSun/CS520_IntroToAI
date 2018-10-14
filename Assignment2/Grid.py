import random
from Assignment2 import Cell
class Grid:
    def __init__(self, height, width, isConsistency,minP):
        self.height = height
        self.width = width
        self.isConsistency = isConsistency
        self.grid = []
        self.mineP = minP
        self.numOfMine = 0

    def generateGrid(self):
        borderHeight = self.height+2
        borderWidth = self.width+2
        for i in range(borderHeight):
            for j in range(borderWidth):
                if i == borderHeight-1 or i == 0 or j == borderWidth-1 or j == 0:
                    cell = Cell
                    cell.isOutside = True
                    cell.isMine = False
                    self.grid.append(cell)
                rNum = random.random()
                if 0 <= rNum < self.mineP:
                    cell = Cell
                    cell.isMine = True
                    self.grid.append(cell)
                    self.numOfMine += 1
                else:
                    cell = Cell
                    cell.isMine = False
                    self.grid.append(cell)

    def isConsistency(self):




