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
        self.borderHeight = self.height+2
        self.borderWidth = self.width+2

    def generateGrid(self):
        for i in range(self.borderHeight):
            for j in range(self.borderWidth):
                if i == self.borderHeight-1 or i == 0 or j == self.borderWidth-1 or j == 0:
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
        return self.grid[(x+ 1) * self.borderWidth + (y+ 1)]

    def markMineNumber(self, x, y):
        cell = self.getCell(x,y)
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                cell = self.getCell(i,j)
                if cell.isOutside == True:
                    continue
                elif cell.isMine == True:
                    cell.numOfMines += 1

    def isConsistency(self):




