import random
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
                if (i == borderHeight-1 or i == 0 or j == borderWidth-1 or j == 0):
                    self.grid.append(Cell(isOutside))
                rNum = random.random()
                if(0 <= rNum < self.mineP):
                    self.grid.append(Cell(True))
                    self.numOfMine += 1
                else:
                    self.grid.append(Cell(False))

    def isConsistency(self):




