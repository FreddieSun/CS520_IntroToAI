import Grid
from Assignment2.Grid import *


class MineSweeper:
    def __init__(self):
        self.grid = Grid(3, 3, 0.3)
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
        for i in range(grid.height):
            for j in range(grid.width):
                curCell = grid.getCell(i, j)
                if curCell.isMine:
                    print('X ', end='')
                else:
                    print('O ', end='')
            print('\n')

    def clickCell(self, grid):
        successClick = False
        isLose = False

        for i in range(grid.height):
            for j in range(grid.width):

                curCell = grid.getCell(i, j)

                if not curCell.isCovered or curCell.isFlag:
                    continue

                numOfMines = curCell.numOfMines
                numOfActualMines = grid.numOfFlags(i, j)
                numOfCoveredCell = grid.numOfCoveredCell(i, j)

                if numOfMines == numOfActualMines and numOfCoveredCell > 0:
                    successClick = True
                    for ii in range(-1, 2):
                        for jj in range(-1, 2):
                            adj = grid.getCell(i + ii, j + jj)
                            if not adj.isOutside and adj.isCovered:
                                if adj.isMine:
                                    isLose = True
                                    adj.isCovered = False
                                    return [successClick, isLose]
                                adj.isCovered = False
                                self.currentNumOfMine -= 1

                return [successClick, isLose]

    def game(self):
        print('Start')
        self.drawGrid(self.grid)
        while not self.currentNumOfMine == 0:
            while self.clickCell(self.grid)[1] and self.clickCell(self.grid)[0]:
                pass
            while self.flagMines(self.grid):
                pass
        # self.drawGrid(self.grid)
        print('Finish')


if __name__ == '__main__':
    mineSweeper = MineSweeper()
    mineSweeper.game()
