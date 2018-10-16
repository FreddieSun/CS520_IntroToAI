import Grid
from Assignment2.Cell import *


class MineSweeper:
    def __init__(self):
        print(1)

    def markMines(self,grid):
        for i in range(grid.height):
            for j in range(grid.width):
                numOfmines = grid.getCell(i,j).numOfMines
                if numOfmines >= 1 and numOfmines == grid.numOfCoveredCell(i,j):
                    for ii in range(-1, 2):
                        for jj in range(-1, 2):
                            adj = grid.getCell(i + ii, j + jj)
                            if not adj.isOutside and adj.isCovered:
                                 adj.isMine = True






if __name__ == '__main__':
    print(1)
