import Grid
import sys
import random
from Assignment2.Grid import *
from Assignment2.PrintGrid import *
import copy
from queue import Queue

solutions = []
BF_LIMIT = 8
borderOptimization = False


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

    def drawUserView(self, grid):
        print('当前用户界面')
        for i in range(grid.height):
            for j in range(grid.width):
                curCell = grid.getCell(i, j)
                if curCell.isFlag:
                    print('X  ', end='')
                elif not curCell.isCovered:
                    print(curCell.numOfMines, ' ', end='')
                else:
                    print('🀆  ', end='')
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
                                    print('Game Over at :[', loseI, ',', loseJ, ']')
                                    sys.exit()
                                    # return [successClick, isLose, loseI, loseJ]
                                adj.isCovered = False
        # return [successClick, isLose, loseI, loseJ]
        if successClick:
            return
        self.logicInference()

    def flagMines(self, grid):
        successFlag = False
        for i in range(grid.height):
            for j in range(grid.width):
                cell = grid.getCell(i, j)
                if not cell.isCovered:
                    numOfmines = cell.numOfMines
                    numOfFlags = self.grid.numOfFlags(i, j)
                    if numOfmines - numOfFlags >= 1 and numOfmines == grid.numOfCoveredCell(i, j) + numOfFlags:
                        successFlag = True
                        for ii in range(-1, 2):
                            for jj in range(-1, 2):
                                adj = grid.getCell(i + ii, j + jj)
                                if not adj.isOutside and adj.isCovered and not adj.isFlag:
                                    adj.isFlag = True
                                    self.currentNumOfMine -= 1
        return successFlag

    def logicInference(self):
        print('Enter logic inference')
        global BF_LIMIT
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
        if numOfCellInSquare > BF_LIMIT:
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
            regionsList = self.tankSegregate(boundaryCells, self.grid)

        totalCases = 1
        success = False
        prob_best = 0
        prob_best_index = -1
        prob_best_s = -1

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
                    success = True
                    self.grid.getCell(tempI, tempJ).isCovered = False

            totalCases *= len(solutions)
            if success:
                continue
            maxEmpty = -10000
            index = -1
            for j in range(len(regionsList[i])):
                tempIndex = 0
                for tempList in solutions:
                    if not tempList[j]:
                        tempIndex += 1
                if tempIndex > maxEmpty:
                    maxEmpty = tempIndex
                    index = j

            probability = maxEmpty / len(solutions)

            if probability > prob_best:
                prob_best = probability
                prob_best_index = index
                prob_best_s = i

        if BF_LIMIT == 8 and 8 < numOfCellInSquare <= 13:
            print('Extending brute force horizon')
            BF_LIMIT = 13
            self.logicInference()
            BF_LIMIT = 8
            return

        print('Start Guess')
        [guessI, guessJ] = regionsList[prob_best_s][prob_best_index]
        self.grid.getCell(guessI, guessJ).isCovered = False
        if self.grid.getCell(guessI, guessJ).isMine:
            print('game over')
            sys.exit()

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

    def recurse(self, borderTile, k, grid):
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
        if flagCount > self.totalNumOfMine:
            return
        if k == len(borderTile):
            if not borderOptimization and flagCount < self.totalNumOfMine:
                return
            solutions = []
            for i in range(len(borderTile)):
                s = borderTile[i]
                si = s[0]
                sj = s[1]
                # solutions[i] = knownMine[si][sj]
                solutions[i] = grid.getCell(si, sj).isMine
            solutions.append(solutions)
            return
        q = borderTile[k]
        qi = q[0]
        qj = q[1]

        # knownMine[qi][qj] = True
        grid.getCell(qi, qj).isFlag = True
        self.recurse(borderTile, k + 1, grid)
        # nownMine[qi][qj] = False
        grid.getCell(qi, qj).isFlag = False

        # knownEmpty[qi][qj] = True
        grid.getCell(qi, qj).isCovered = False
        self.recurse(borderTile, k + 1, grid)
        # nownEmpty[qi][qj] = False
        grid.getCell(qi, qj).isCovered = True

    def tankSegregate(self, borderTiles, grid):
        allRegions = []
        covered = []
        while True:
            queue = []
            finishedRegion = []

            for i in range(len(borderTiles)):
                firstT = borderTiles[i]
                if firstT not in covered:
                    queue.append(firstT)
                    break

            if len(queue) == 0:
                break
            while len(queue) != 0:
                curTile = queue.pop(0)
                ci = curTile[0]
                cj = curTile[1]
                finishedRegion.append(curTile)
                covered.append(curTile)

                for i in range(len(borderTiles)):
                    tile = borderTiles[i]
                    ti = tile[0]
                    tj = tile[1]
                    isConnected = False
                    if tile in finishedRegion:
                        continue
                    if abs(ci - ti) > 2 or abs(cj - tj) > 2:
                        isConnected = False
                    else:
                        flag = True
                        while (flag):
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
                        queue.append(tile)
            allRegions.append(finishedRegion)
        return allRegions

    def game(self):
        print('Start')
        self.drawGrid(self.grid)
        print('共有雷:', self.totalNumOfMine, '个')

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
            # while self.flagMines(self.grid):
            #     pass
            # for i in range(sys.maxsize):
            #     successClick, isLose, loseI, loseJ = self.clickCell(self.grid)
            #     self.drawUserView(self.grid)
            #     if isLose:
            #         print('Game Over at ', loseI, loseJ)
            #         sys.exit()
            #     if successClick:
            #         continue
            #     else:
            #         break
            while self.flagMines(self.grid):
                pass
            while self.clickCell(self.grid):
                pass
            self.drawUserView(self.grid)

        # self.drawGrid(self.grid)

        print('Win')


if __name__ == '__main__':
    mineSweeper = MineSweeper()
    # mineSweeper.drawGrid(mineSweeper.grid)
    # gridPrinter = gridList(mineSweeper.grid)
    # drawInitialGrid(gridPrinter, mineSweeper.grid.height, mineSweeper.grid.width)
    mineSweeper.game()
