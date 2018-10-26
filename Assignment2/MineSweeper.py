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
knownMine = []
knownEmpty = []
class MineSweeper:

    def __init__(self):
        self.grid = Grid(9, 9, 0.123)
        # self.grid.generateSpecificGrid()
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
                                    print('clickCell画图')
                                    self.drawUserView(self.grid)
                                    isLose = True
                                    loseI = i + ii
                                    loseJ = j + jj
                                    print('Game Over at(clickCell method) :[', loseI, ',', loseJ, ']')
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
        print('开始逻辑推理')
        global BF_LIMIT
        global solutions
        global borderOptimization

        if not self.grid.isConsistency():
            return

        boundaryCells = []
        coveredCellList = []


        borderOptimization = False

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
            borderOptimization = True
        else:
            boundaryCells = coveredCellList

        if len(boundaryCells) == 0:
            return

        # get the different regions and solve them one by one

        regionsList = []
        if not borderOptimization:
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

            for p in range(self.grid.height):
                for q in range(self.grid.width):
                    tempCell = self.grid.getCell(p, q)
                    if tempCell.isFlag:
                        knownMine = True
                    else:
                        knownMine = False
                    if not tempCell.isCovered:
                        knownEmpty = True
                    else:
                        knownEmpty = False

            curGrid = copy.deepcopy(self.grid)

            # Key Part
            self.recurse(regionsList[i], 0, curGrid)
            # failed to find a solution
            if len(solutions) == 0:
                return

            for j in range(len(regionsList[i])):
                allMine = True
                allClick = True

                for tempList in solutions:
                    if not tempList[j]:
                        allMine = False
                    if tempList[j]:
                        allClick = False

                [tempI, tempJ] = regionsList[i][j]

                if allMine:
                    self.grid.getCell(tempI, tempJ).isFlag = True
                    self.currentNumOfMine -= 1
                if allClick:
                    success = True
                    print('我逻辑推理后确定点','[',tempI,',',tempJ,']')
                    self.grid.getCell(tempI, tempJ).isCovered = False

            totalCases *= len(solutions)
            if success:
                # todo 我们这里应该跳出logic inference 让他去扩散，而不是在里面继续猜
                return
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

        # if BF_LIMIT == 8 and 8 < numOfCellInSquare <= 13:
        #     print('Extending brute force horizon')
        #     BF_LIMIT = 13
        #     self.logicInference()
        #     BF_LIMIT = 8
        #     return

        print('Start Guess')
        [guessI, guessJ] = regionsList[prob_best_s][prob_best_index]
        self.grid.getCell(guessI, guessJ).isCovered = False
        print("我猜的是：",'[',guessI,',',guessJ,']')
        if self.grid.getCell(guessI, guessJ).isMine:
            print('Game over')
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

    def recurse(self, borderTile, k, curGrid):
        flagCount = 0

        for i in range(curGrid.height):
            for j in range(curGrid.width):
                # if konwnMine[i][j]:
                if curGrid.getCell(i, j).isFlag:
                    flagCount += 1
                # num = tank_board[i][j]
                num = 10
                if not self.grid.getCell(i, j).isCovered:
                    num = self.grid.getCell(i, j).numOfMines

                if curGrid.getCell(i, j).isFlag or curGrid.getCell(i, j).isCovered:
                    continue
                if num == 10:
                    continue

                if (i == 0 and j == 0) or (i == curGrid.height - 1 and j == curGrid.width - 1) \
                        or (i == 0 and j == curGrid.width - 1) or (j == 0 and i == curGrid.height - 1):
                    surround = 3
                elif i == 0 or j == 0 or i == curGrid.height - 1 or j == curGrid.width - 1:
                    surround = 5
                else:
                    surround = 8

                # numFlags = knownMine.numOfFlags(i, j)
                numFlags = curGrid.numOfFlags(i, j)
                # numFree = knownEmpty.numOfFlags(i, j)
                numFree = surround - curGrid.numOfCoveredCell(i, j) - numFlags
                if numFlags > num:
                    return
                if surround - numFree < num:
                    return

        if flagCount > self.totalNumOfMine:
            return

        if k == len(borderTile):
            if not borderOptimization and flagCount < self.totalNumOfMine:
                return
            # if not borderOptimization:
            #     return
            tempSolutions = []
            for i in range(len(borderTile)):
                s = borderTile[i]
                si = s[0]
                sj = s[1]
                tempSolutions.append((curGrid.getCell(si, sj)).isFlag)
            global solutions
            solutions.append(tempSolutions)
            return

        q = borderTile[k]
        qi = q[0]
        qj = q[1]

        # knownMine[qi][qj] = True
        curGrid.getCell(qi, qj).isFlag = True
        self.recurse(borderTile, k + 1, curGrid)
        # nownMine[qi][qj] = False
        curGrid.getCell(qi, qj).isFlag = False

        # knownEmpty[qi][qj] = True
        curGrid.getCell(qi, qj).isCovered = False
        self.recurse(borderTile, k + 1, curGrid)
        # nownEmpty[qi][qj] = False
        curGrid.getCell(qi, qj).isCovered = True

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
                        isConnected = self.findIsConnected(ci, cj, ti, tj)

                    if not isConnected:
                        continue
                    if tile not in queue:
                        queue.append(tile)
            allRegions.append(finishedRegion)
        return allRegions

    def findIsConnected(self, ci, cj, ti, tj):
        for i in range(self.grid.height):
            for j in range(self.grid.width):
                if abs(ci - i) <= 1 and abs(cj - j) <= 1 and abs(ti - i) <= 1 and abs(
                        tj - j) <= 1:
                    isConnected = True
                    return isConnected

        return False

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
        # self.grid.getCell(6, 8).isCovered = False

        while not self.isFinished():
            while self.flagMines(self.grid):
                pass
            while self.clickCell(self.grid):
                pass
            self.drawUserView(self.grid)




        for i in range(self.grid.height):
            for j in range(self.grid.width):
                curCell = self.grid.getCell(i, j)
                if curCell.isFlag != curCell.isMine:
                    print('我们凉凉了',i, j)
                if curCell.isCovered and not curCell.isFlag:
                    print('我们凉凉了',i, j)

        print('Win')
    def isFinished(self):
        for i in range(self.grid.height):
            for j in range(self.grid.width):
                curCell = self.grid.getCell(i, j)
                if curCell.isFlag != curCell.isMine:
                    return False
                if curCell.isCovered and not curCell.isFlag:
                    return False

        return True

if __name__ == '__main__':
    mineSweeper = MineSweeper()
    # mineSweeper.drawGrid(mineSweeper.grid)
    # gridPrinter = gridList(mineSweeper.grid)
    # drawInitialGrid(gridPrinter, mineSweeper.grid.height, mineSweeper.grid.width)
    mineSweeper.game()
    # gridPrinter1 = gridList(mineSweeper.grid)
    # drawInitialGrid(gridPrinter1, mineSweeper.grid.height, mineSweeper.grid.width)
