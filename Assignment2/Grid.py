import random
from Assignment2 import Cell


class Grid:
    def __init__(self, height, width, isConsistency, minP):
        self.height = height
        self.width = width
        self.isConsistency = isConsistency
        self.grid = []
        self.mineP = minP
        self.numOfMine = 0
        self.borderHeight = self.height + 2
        self.borderWidth = self.width + 2

    def generateGrid(self):
        for i in range(self.borderHeight):
            for j in range(self.borderWidth):
                if i == self.borderHeight - 1 or i == 0 or j == self.borderWidth - 1 or j == 0:
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

    def getCell(self, x, y):
        return self.grid[(x + 1) * self.borderWidth + (y + 1)]

    def markMineNumber(self, x, y):
        cell = self.getCell(x, y)
        for i in range(3):
            for j in range(3):
                getCell

    def isConsistency(self):
        for i in range(self.height):
            for j in range(self.width):
                numOfCovered = self.numOfCoveredCell(i, j, self.grid)
                numOfFlag = self.numOfFlags(i, j, self.grid)
                # if the current cell shows number of mines around is 0
                # but the actual number of cells covered around > 0
                # then it is not consistency
                if self.getCell(i, j).numOfMines == 0 and numOfCovered > 0:
                    return False
                # if the number of mines showed by the current cells
                # is greater than the number of flags around
                # but the number of covered cells around is 0
                # then it is not consistency
                if self.getCell(i, j).numOfMines > numOfFlag and numOfCovered == 0:
                    return False

        return True

    def numOfCoveredCell(self, i, j, grid):
        result = 0
        for p in range(-1, 1):
            for q in range(-1, 1):
                if self.getCell(i + p, j + q).isCovered:
                    result += 1
        return result

        return 0

    def numOfFlags(self, i, j, grid):
        result = 0
        for p in range(-1, 1):
            for q in range(-1, 1):
                if self.getCell(i + p, j + q).isMine:
                    result += 1
        return result
