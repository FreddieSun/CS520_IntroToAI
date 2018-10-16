import Grid
from Assignment2.Grid import *


class MineSweeper:
    def __init__(self):
        self.grid = Grid(4, 4, 0.2)
        self.grid.generateGrid()
        self.grid.markMineNumber()
        self.totalNumOfMine = self.grid.numOfMine
        self.currentNumOfMine = self.totalNumOfMine

    def flagMines(self, grid):
        flag = False
        for i in range(grid.height):
            for j in range(grid.width):
                cell = grid.getCell(i, j)
                if not cell.isCovered:
                    numOfmines = cell.numOfMines
                    if numOfmines >= 1 and numOfmines == grid.numOfCoveredCell(i, j):
                        flag = True
                        for ii in range(-1, 2):
                            for jj in range(-1, 2):
                                adj = grid.getCell(i + ii, j + jj)
                                if not adj.isOutside and adj.isCovered:
                                    adj.isFlag = True
        return flag

    def drawGrid(self, grid):
        for cell in grid:
            for i in range(grid.height):
                string = ''
                for j in range(grid.width):
                    if grid.getCell(i, j).isFlag:
                        string += '*'
                    else:
                        string += str(cell.numOfMines)
                print(string,'\n')

    def clickCell(self, grid):
        flag = False
        isLose = False

        for i in range(grid.borderHeight):
            for j in range(grid.borderWidth):

                curCell = grid.getCell(i, j)

                if not curCell.isCovered or curCell.isFlag:
                    continue

                numOfMines = curCell.numOfMines
                numOfActualMines = grid.numOfFlags(i, j)
                numOfCoveredCell = grid.numOfCoveredCell(i, j)

                if numOfMines == numOfActualMines and numOfCoveredCell > 0:
                    flag = True
                    for ii in range(-1, 2):
                        for jj in range(-1, 2):
                            adj = grid.getCell(i + ii, j + jj)
                            if not adj.isOutside and adj.isCovered:
                                if adj.isMine:
                                    isLose = True
                                    adj.isCovered = False
                                    return [flag, isLose]
                                adj.isCovered = False
                                self.currentNumOfMine -= 1

                return [flag, isLose]

    def game(self):
        print('Start')

        # self.drawGrid(self.grid)
        while self.currentNumOfMine == 0:
            while self.clickCell(self.grid):
                pass
            while self.flagMines(self.grid):
                pass
        # self.drawGrid(self.grid)
        print('Finish')

if __name__ == '__main__':
    mineSweeper = MineSweeper()
    mineSweeper.game()
