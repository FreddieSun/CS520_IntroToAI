import random
from Assignment3.Grid import *
from Assignment3.PrintGrid import *


action = 0

class ProbSearch:

    def __init__(self):
        print('init method')
        self.RULE1 = 'rule1'
        self.RULE2 = 'rule2'
        self.RULE3 = 'rule3'
        self.RULE4 = 'rule4'
        self.grid = Grid()
        self.numOfSearches = 0
        self.grid.generateGrid()

    def findTarget(self, grid, i, j):
        prob = random.random()
        if not grid.getCell(i, j).isTarget:
            return False
        else:
            if grid.getCell(i, j).terrain == 1:
                if prob >= 0.1:
                    return True

            if grid.getCell(i, j).terrain == 2:
                if prob >= 0.3:
                    return True

            if grid.getCell(i, j).terrain == 3:
                if prob >= 0.7:
                    return True

            if grid.getCell(i, j).terrain == 4:
                if prob > 0.9:
                    return True
        return False

    def updateProbStable(self, grid, i, j):
        searchedCell = grid.getCell(i, j)
        Pj = searchedCell.Pr1
        Tj = 1 - searchedCell.Pf
        grid.getCell(i, j).Pr1 = Pj * Tj
        grid.getCell(i, j).Pr2 = grid.getCell(i, j).Pr1 * (1 - Tj)
        for ii in range(grid.N):
            for jj in range(grid.N):
                if i == ii and j == jj:
                    continue
                else:
                    otherCell = grid.getCell(ii, jj)
                    Pi = otherCell.Pr1
                    grid.getCell(ii, jj).Pr1 = Pi * (1 + Pj * (1 - Tj) / (1 - Pj))
                    Ti = grid.getCell(ii, jj).Pf
                    grid.getCell(ii, jj).Pr2 = grid.getCell(ii, jj).Pr1 * Ti
        print('updateProb method')
    def updateProbMoving(self,grid,T1,T2,NT1,NT2):
        for ii in range(grid.N):
            for jj in range(grid.N):
                cell = grid.getCell(ii, jj)
                if (cell.terrain == T1 or cell.terrain == T2):
                    cell.Pr1 = 0
                    cell.Pr2 = 0



    def searchCell(self, grid, type):
        returnCell = grid.getCell(0, 0)
        returnI = 0
        returnJ = 0
        if type == self.RULE1:
            for i in range(50):
                for j in range(50):
                    if grid.getCell(i, j).Pr1 > returnCell.Pr1:
                        returnCell = grid.getCell(i, j)
                        returnI = i
                        returnJ = j
                    elif grid.getCell(i, j).Pr1 == returnCell.Pr1:
                        if grid.getCell(i, j).Pr2 > returnCell.Pr2:
                            returnCell = grid.getCell(i, j)
                            returnI = i
                            returnJ = j

        if type == self.RULE2:
            for i in range(50):
                for j in range(50):
                    if grid.getCell(i, j).Pr2 > returnCell.Pr2:
                        returnCell = grid.getCell(i, j)
                        returnI = i
                        returnJ = j
                    elif grid.getCell(i, j).Pr2 == returnCell.Pr2:
                        if grid.getCell(i, j).Pr1 > returnCell.Pr1:
                            returnCell = grid.getCell(i, j)
                            returnI = i
                            returnJ = j

        return [returnI, returnJ]

    def searchCostCell(self, grid, type, i, j):
        global action
        distance = self.getDistance(i, j, self.grid)
        returnCell = grid.getCell(0, 0)
        returnI = 0
        returnJ = 0
        if type == self.RULE3:
            for i in range(50):
                for j in range(50):
                    if grid.getCell(i, j).Pr1 / distance[i * 50 + j] > \
                            returnCell.Pr1 / distance[returnI * 50 + returnJ]:
                        returnCell = grid.getCell(i, j)
                        returnI = i
                        returnJ = j
                    elif grid.getCell(i, j).Pr1 / distance[i * 50 + j] == \
                            returnCell.Pr1 / distance[returnI * 50 + returnJ]:
                        if grid.getCell(i, j).Pr2 / distance[i * 50 + j] > \
                                returnCell.Pr2 / distance[returnI * 50 + returnJ]:
                            returnCell = grid.getCell(i, j)
                            returnI = i
                            returnJ = j

        if type == self.RULE4:
            for i in range(50):
                for j in range(50):
                    if grid.getCell(i, j).Pr2 / distance[i * 50 + j] > \
                            returnCell.Pr2 / distance[returnI * 50 + returnJ]:
                        returnCell = grid.getCell(i, j)
                        returnI = i
                        returnJ = j
                    elif grid.getCell(i, j).Pr2 / distance[i * 50 + j] == \
                            returnCell.Pr2 / distance[
                        returnI * 50 + returnJ]:
                        if grid.getCell(i, j).Pr1 / distance[i * 50 + j] > \
                                returnCell.Pr1 / distance[returnI * 50 + returnJ]:
                            returnCell = grid.getCell(i, j)
                            returnI = i
                            returnJ = j
        action += distance[returnI * 50 + returnJ]
        return [returnI, returnJ]

    def probSearch(self):
        print('probSearch method')
        targetI = 0
        targetJ = 0

        while True:
            self.numOfSearches += 1
            print(str(self.numOfSearches) + 'th search')
            [i, j] = self.searchCell(self.grid, self.RULE2)
            if self.findTarget(self.grid, i, j):
                targetI = i
                targetJ = j
                break
            self.updateProbStable(self.grid, i, j)

        print('Target is founded at ', '[', targetI, ',', targetJ, '], with ', self.numOfSearches, 'searches')
        print('Target cell', self.grid.getCell(targetI, targetJ).terrain)

        if self.grid.getCell(targetI, targetJ).isTarget:
            print('爽')
        else:
            print('我们凉凉了')

    def getDistance(self, i, j, grid):
        distance = []
        for ii in range(grid.N):
            for jj in range(grid.N):
                dis = abs(ii - i) + abs(jj - j) + 1
                distance.append(dis)
        return distance

    def probCostSearch(self):
        [a, b] = self.searchCell(self.grid, self.RULE2)
        while True:
            self.numOfSearches += 1
            if self.findTarget(self.grid, a, b):
                targetI = a
                targetJ = b
                break
            [i, j] = self.searchCostCell(self.grid, self.RULE4, a, b)
            self.updateProbStable(self.grid, a, b)
            print('Next:', i, ',', j)
            [a, b] = [i, j]

        print('Target is founded at ', '[', targetI, ',', targetJ, '], with ', self.numOfSearches, 'searches')
        print('Target cell', self.grid.getCell(targetI, targetJ).terrain)

        if self.grid.getCell(targetI, targetJ).isTarget:
            print('爽')
        else:
            print('我们凉凉了')
        print('Total action is:', action)

    def probMoveSearch(self):
        print('probMoveSearch method')
        targetI = 0
        targetJ = 0

        while True:
            self.numOfSearches += 1
            print(str(self.numOfSearches) + 'th search')
            [i, j] = self.searchCell(self.grid, self.RULE1)
            if self.findTarget(self.grid, i, j):
                targetI = i
                targetJ = j
                break
            [type1, type2] = self.moveTarget(self.grid)

            self.updateProbMoving(self.grid, type1, type2, 1, 1)

        print('Target is founded at ', '[', targetI, ',', targetJ, '], with ', self.numOfSearches, 'searches')
        print('Target cell', self.grid.getCell(targetI, targetJ).terrain)

        if self.grid.getCell(targetI, targetJ).isTarget:
            print('爽')
        else:
            print('我们凉凉了')


    def moveTarget(self, grid):
        i = grid.targetI
        j = grid.targetJ
        terrain1 = grid.getCell(i,j).terrain

        if i != 0 and i != 49 and j != 0 and j != 49: #not bound
            moveto = random.randint(0,3)
            if moveto == 0 :  #left
                j -= 1
            elif moveto == 1 : #up
                i -= 1
            elif moveto == 2 : #right
                j += 1
            else :
                i += 1
        elif i == 0 :
            if j == 0 :
                moveto = random.randint(0,1)
                if moveto == 0 : #right
                    j += 1
                else :  #down
                    i += 1
            elif j == 49 :
                moveto = random.randint(0,1)
                if moveto == 0: #left
                    j -= 1
                else : #down
                    i += 1
            else :
                moveto = random.randint(0,2)
                if moveto == 0: #left
                    j -= 1
                elif moveto == 1 : #right
                    j += 1
                else : #down
                    i += 1
        elif i == 49 :
            if j == 0 :
                moveto = random.randint(0,1)
                if moveto == 0 : #right
                    j += 1
                else :  #up
                    i -= 1
            elif j == 49 :
                moveto = random.randint(0,1)
                if moveto == 0: #left
                    j -= 1
                else : #up
                    i -= 1
            else :
                moveto = random.randint(0,2)
                if moveto == 0: #left
                    j -= 1
                elif moveto == 1 : #right
                    j += 1
                else : #up
                    i -= 1
        elif j == 0:
            if i == 0:
                moveto = random.randint(0, 1)
                if moveto == 0:  # right
                    j += 1
                else:  # down
                    i += 1
            elif i == 49:
                moveto = random.randint(0, 1)
                if moveto == 0:  # right
                    j += 1
                else:  # up
                    i -= 1
            else:
                moveto = random.randint(0, 2)
                if moveto == 0:  # down
                    i += 1
                elif moveto == 1:  # right
                    j += 1
                else:  # up
                    i -= 1

        elif j == 49:
            if i == 0:
                moveto = random.randint(0, 1)
                if moveto == 0:  # left
                    j -= 1
                else:  # down
                    i += 1
            elif i == 49:
                moveto = random.randint(0, 1)
                if moveto == 0:  # left
                    j -= 1
                else:  # up
                    i -= 1
            else:
                moveto = random.randint(0, 2)
                if moveto == 0:  # down
                    i += 1
                elif moveto == 1:  # left
                    j -= 1
                else:  # up
                    i -= 1
        grid.targetI = i
        grid.targetJ = j
        terrain2 = grid.getCell(i,j).terrain
        return [terrain1 , terrain2]


if __name__ == '__main__':
    print('main method')
    probSearch = ProbSearch()
    probSearch.probCostSearch()
