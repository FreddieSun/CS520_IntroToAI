import Grid
import sys
import random
from Assignment2.Grid import *
from Assignment2.PrintGrid import *
import copy
import Queue


class MineSweeper:
    def __init__(self):
        self.grid = Grid(5, 5, 0.123)
        self.grid.generateGrid()
        self.grid.markMineNumber()
        self.totalNumOfMine = self.grid.numOfMine
        self.currentNumOfMine = self.totalNumOfMine

    def drawGrid(self, grid):
        for i in range(grid.height):
            for j in range(grid.width):
                curCell = grid.getCell(i, j)
                if curCell.isMine:
                    print('X  ', end='')
                else:
                    print(curCell.numOfMines, ' ', end='')
            print('\n')

    # 点开这个cell周围的点
    def clickCell(self, grid):
        successClick = False
        isLose = False
        loseI = 0
        loseJ = 0

        for i in range(grid.height):
            for j in range(grid.width):

                curCell = grid.getCell(i, j)
                # 如果这个点还没被点开或者是旗子，跳过
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
                            if not adj.isOutside and adj.isCovered and not adj.isFlag:
                                if adj.isMine:
                                    isLose = True
                                    loseI = i + ii
                                    loseJ = j + jj
                                    return [successClick, isLose, loseI, loseJ]
                                adj.isCovered = False
        return [successClick, isLose, loseI, loseJ]

    def logicInference(self):
        print('Enter logic inference')

        if not self.grid.isConsistency():
            return

        boundaryCells = []
        coveredCellList = []

        boundaryOptimization = False

        # add all the covered cell into the lise
        # add all the boundary cell into the list
        for i in range(self.grid.height):
            for j in range(self.grid.width):
                curCell = self.grid.getCell(i, j)
                if curCell.isCovered and not curCell.isFlag:
                    coveredCellList.append([i, j])
                if self.isBoundary(self.grid, i, j) and not curCell.isFlag:
                    boundaryCells.append([i, j])

        # todo
        numOfCellInSquare = len(coveredCellList) - len(boundaryCells)
        if numOfCellInSquare > 8:
            boundaryOptimization = True
        else:
            boundaryCells = coveredCellList

        if len(boundaryCells) == 0:
            return

        # get the different regions and solve them one by one

        regionsList = []
        if not boundaryOptimization:
            regionsList.append(boundaryCells)
        else:
            regionsList = self.getRegions(boundaryCells)

        # todo 各种变量的声明

        # for each separate region, find the result
        for i in range(len(regionsList)):
            solutions = []
            curGrid = copy.deepcopy(self.grid)

            self.recurse(regionsList[i], 0, self.grid)

            # failed to find a solution
            if len(solutions) == 0:
                return

            for j in range(len(regionsList[i])):
                allMine = True
                allClick = True

                for tempList in solutions:
                    if not tempList[j]:
                        allMine = False
                    if tempList[i]:
                        allClick = False

                [tempI, tempJ] = regionsList[i][j]

                if allMine:
                    self.grid.getCell(tempI, tempJ).isFlag = True
                if allClick:
                    # todo success
                    self.grid.getCell(tempI, tempJ).isCovered = False

    def getRegions(self, boundaryCells):
        print('This is getRegions')
        regionsList = []
        return regionsList

    def flagMines(self, grid):
        flag = False
        for i in range(grid.height):
            for j in range(grid.width):
                cell = grid.getCell(i, j)
                if not cell.isCovered:
                    numOfmines = cell.numOfMines
                    if numOfmines >= 1 and numOfmines == grid.numOfCoveredCell(i, j) + grid.numOfFlags(i, j):
                        flag = True
                        for ii in range(-1, 2):
                            for jj in range(-1, 2):
                                adj = grid.getCell(i + ii, j + jj)
                                if not adj.isOutside and adj.isCovered:
                                    adj.isFlag = True
                                    self.currentNumOfMine -= 1
        return flag

    def isBoundary(self, grid, i, j):
        cell = grid.getCell(i, j)
        if not cell.isCovered:
            return False

        if i != 0 and not grid.getCell(i - 1, j).isCovered:
            return True
        if j != 0 and not grid.getCell(i, j - 1).isCovered:
            return True
        if i != grid.height - 1 and not grid.getCell(i + 1, j).isCovered:
            return True
        if j != grid.width - 1 and not grid.getCell(i, j + 1).isCovered:
            return True
        if i != 0 and j != 0 and not grid.getCell(i - 1, j - 1).isCovered:
            return True
        if i != 0 and j != grid.width - 1 and not grid.getCell(i - 1, j + 1).isCovered:
            return True
        if i != grid.height - 1 and j != 0 and not grid.getCell(i + 1, j - 1).isCovered:
            return True
        if i != grid.height - 1 and j != grid.width - 1 and not grid.getCell(i + 1, j + 1).isCovered:
            return True

        return False

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
                print('点开的点是', i, j)
                firstTrigger = False

        while not self.currentNumOfMine == 0:
            for i in range(sys.maxsize):
                successClick, isLose, loseI, loseJ = self.clickCell(self.grid)
                if isLose:
                    print('Game Over at ', loseI, loseJ)
                    sys.exit()
                if successClick:
                    continue
                else:
                    break
            while self.flagMines(self.grid):
                pass
        # self.drawGrid(self.grid)

        print('Win')

        def Recurse(self, borderTile, k, grid):
            flagCount = 0
            for i in range(grid.height):
                for j in range(grid.width):
                    # if konwnMine[i][j]:
                    if grid.getCell(i, j).isFlag:
                        flagCount += 1
                    # num = tank_board[i][j]
                    num = grid.getCell(i, j).numOfMines
                    if num < 0:
                        continue
                    if (i == 0 and j == 0) or (i == grid.height - 1 and j == grid.width - 1):
                        surround = 3
                    elif i == 0 or j == 0 or i == grid.height - 1 or j == grid.width - 1:
                        surround = 5
                    else:
                        surround = 8
                    # numFlags = knownMine.numOfFlags(i, j)
                    numFlags = grid.numOfFlags(i, j)
                    # numFree = knownEmpty.numOfFlags(i, j)
                    numFree = grid.numOfFlags(i, j)
                    if numFlags > num:
                        return
                    if surround - numFree < num:
                        return
            if flagCount > TOT_MINES:
                return
            if k == len(borderTile):
                if not borderOptimization and flagCount < TOT_MINES:
                    return
                solution = []
                for i in range(len(borderTile)):
                    s = borderTile[i]
                    si = s[0]
                    sj = s[1]
                    # solution[i] = knownMine[si][sj]
                    solution[i] = grid.getCell(si, sj).isMine
                tank_solutions.append(solution)
                return
            q = borderTile[k]
            qi = q[0]
            qj = q[1]

            # knownMine[qi][qj] = True
            grid.getCell(qi, qj).isFlag = True
            Recurse(borderTile, k + 1, grid)
            # nownMine[qi][qj] = False
            grid.getCell(qi, qj).isFlag = False

            # knownEmpty[qi][qj] = True
            grid.getCell(qi, qj).isCovered = False
            Recurse(borderTile, k + 1, grid)
            # nownEmpty[qi][qj] = False
            grid.getCell(qi, qj).isCovered = True

        def tankSegregate(borderTiles, grid):
            allRegions = []
            covered = []
            while True:
                queue = Queue.Queue()
                finishedRegion = []
                for firstT in borderTiles:
                    if firstT not in covered:
                        queue.put(firstT)
                        break
                if queue.empty():
                    break
                while not queue.empty():
                    curTile = queue.get()
                    ci = curTile[0]
                    cj = curTile[1]
                    finishedRegion.append(curTile)
                    covered.append(curTile)
                    for tile in borderTiles:
                        ti = tile[0]
                        tj = tile[1]
                        isConnected = False
                        if tile in finishedRegion:
                            continue
                        if abs(ci - ti) > 2 or abs(cj - tj) > 2:
                            isConnected = False
                        else:
                            flag = True
                            while(flag):
                                for i in range(grid.height):
                                    for j in range(grid.width):
                                        if grid.getCell(i, j).numOfMines > 0:
                                            if abs(ci - i) <= 1 and abs(cj - j) <= 1 and abs(ti - i) <= 1 and abs(
                                                    tj - i) <= 1:
                                                isConnected = True
                                                flag = False
                        if not isConnected:
                            continue
                        if tile not in queue:
                            queue.put(tile)
                allRegions.append(finishedRegion)
            return allRegions


if __name__ == '__main__':
    mineSweeper = MineSweeper()
    # mineSweeper.drawGrid(mineSweeper.grid)
    # gridPrinter = gridList(mineSweeper.grid)
    # drawInitialGrid(gridPrinter, mineSweeper.grid.height, mineSweeper.grid.width)
    mineSweeper.game()
