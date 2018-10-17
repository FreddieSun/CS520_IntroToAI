import Grid
import sys
import random
from Assignment2.Grid import *


class MineSweeper:
    def __init__(self):
        self.grid = Grid(3, 3, 0.2)
        self.grid.generateGrid()
        self.grid.markMineNumber()
        self.totalNumOfMine = self.grid.numOfMine
        self.currentNumOfMine = self.totalNumOfMine

    def drawGrid(self, grid):
        for i in range(grid.height):
            for j in range(grid.width):
                curCell = grid.getCell(i, j)
                if curCell.isMine:
                    print('X ', end='')
                else:
                    print(curCell.numOfMines, '', end='')
            print('\n')

    def clickCell(self, grid):
        successClick = False
        isLose = False

        for i in range(grid.height):
            for j in range(grid.width):

                curCell = grid.getCell(i, j)

                if curCell.isCovered or curCell.isFlag:
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
        return [successClick, isLose]

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

    def game(self):
        print('Start')
        self.drawGrid(self.grid)

        # random choose a cell which is not bomb
        # in order to trigger the algorithm
        firstTrigger = True
        while firstTrigger:
            i = random.randint(0, self.grid.height - 1)
            j = random.randint(0, self.grid.width - 1)
            currCell = self.grid.getCell(i, j)
            if not currCell.isMine and currCell.numOfMines == 0:
                # click one cell and trigger the algorithm
                self.grid.getCell(i, j).isCovered = False
                firstTrigger = False

        while not self.currentNumOfMine == 0:
            for i in range(sys.maxsize):
                successClick, isLose = self.clickCell(self.grid)
                if isLose:
                    print('Game Over')
                    sys.exit()
                if successClick:
                    continue
                else:
                    break
            while self.flagMines(self.grid):
                pass
        # self.drawGrid(self.grid)

        print('Win')


if __name__ == '__main__':
    mineSweeper = MineSweeper()
    mineSweeper.game()
