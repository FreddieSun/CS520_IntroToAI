import random
from Assignment3.Grid import *

action = 0


class ProbSearch:

    def __init__(self):
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

    def updateProbMoving(self, grid, terrianList, moveRegion):
        #print(moveRegion)
        if len(terrianList) == 1:
            T1 = 0
            for i in range(len(terrianList[0])):
                T1 += terrianList[0][i].Pr1
            N = len(terrianList[0])
            for ii in range(grid.N):
                for jj in range(grid.N):
                    cell = grid.getCell(ii, jj)
                    if cell.terrain == moveRegion[0]:
                        cell.Pr1 += (1 - T1) / N
                        cell.Pr2 = cell.Pr1 * cell.Pf
                    else:
                        cell.Pr1 = 0
                        cell.Pr2 = 0
        else:
            T1 = 0
            T2 = 0
            for i in range(len(terrianList[0])):
                T1 += terrianList[0][i].Pr1
            for j in range(len(terrianList[1])):
                T2 += terrianList[1][j].Pr1
            N = len(terrianList[0]) + len(terrianList[1])
            for ii in range(grid.N):
                for jj in range(grid.N):
                    cell = grid.getCell(ii, jj)
                    if cell.terrain == moveRegion[0] or cell.terrain == moveRegion[1]:
                        cell.Pr1 += (1 - T1 - T2) / N
                        cell.Pr2 = cell.Pr1 * cell.Pf
                    else:
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

    def getDistance(self, i, j, grid):
        distance = []
        for ii in range(grid.N):
            for jj in range(grid.N):
                dis = abs(ii - i) + abs(jj - j) + 1
                distance.append(dis)
        return distance

    def probCostSearch(self,rule):#Q1 R3，R4
        rule1 = ''
        rule2 = ''
        if rule =='3':
            rule1 = self.RULE1
            rule2 = self.RULE3
        elif rule =='4':
            rule1 = self.RULE2
            rule2 = self.RULE4
        [a, b] = self.searchCell(self.grid, rule1)
        while True:
            self.numOfSearches += 1
            if self.findTarget(self.grid, a, b):
                targetI = a
                targetJ = b
                break
            [i, j] = self.searchCostCell(self.grid, rule2, a, b)
            self.updateProbStable(self.grid, a, b)
            print('Next search:', i, ',', j)
            [a, b] = [i, j]

        targetTerrian = ''
        if self.grid.getCell(targetI, targetJ).terrain == 1:
            targetTerrian ='flat'
        elif self.grid.getCell(targetI, targetJ).terrain == 2:
            targetTerrian ='hill'
        elif self.grid.getCell(targetI, targetJ).terrain == 3:
            targetTerrian ='forest'
        elif self.grid.getCell(targetI, targetJ).terrain == 4:
            targetTerrian ='cave'

        print('Target is founded at ', '[', targetI, ',', targetJ, '], type [',targetTerrian,'],','with' ,self.numOfSearches, 'searches')
        print('Total action ( move + search ) is:', action)

    def probSearch(self,rule):#Q1 R1，R2
        if rule =='1':
            rule = self.RULE1
        elif rule =='2':
            rule = self.RULE2
        while True:
            self.numOfSearches += 1
            [i, j] = self.searchCell(self.grid, rule)
            print('Next search:', i, ',', j)
            if self.findTarget(self.grid, i, j):
                targetI = i
                targetJ = j
                break
            self.updateProbStable(self.grid, i, j)

        targetTerrian = ''
        if self.grid.getCell(targetI, targetJ).terrain == 1:
            targetTerrian ='flat'
        elif self.grid.getCell(targetI, targetJ).terrain == 2:
            targetTerrian ='hill'
        elif self.grid.getCell(targetI, targetJ).terrain == 3:
            targetTerrian ='forest'
        elif self.grid.getCell(targetI, targetJ).terrain == 4:
            targetTerrian ='cave'

        print('Target is founded at ', '[', targetI, ',', targetJ, '], type [',targetTerrian,'],','with' ,self.numOfSearches, 'searches')

    def probMoveSearch(self,rule):#Q2 R1，R2
        if rule =='1':
            rule = self.RULE1
        elif rule =='2':
            rule = self.RULE2
        Type1 = ''
        Type2 = ''
        while True:

            self.numOfSearches += 1
            [i, j] = self.searchCell(self.grid, rule)
            print('Next search:', i, ',', j)
            print()
            if self.findTarget(self.grid, i, j):
                targetI = i
                targetJ = j
                break
            [type1, type2] = self.moveTarget(self.grid)
            allList = self.getListOfEachTerrainType(self.grid)
            terrainList = []
            if type1 == type2:
                terrainList.append(allList[type1 - 1])
            else:
                terrainList.append(allList[type1 - 1])
                terrainList.append(allList[type2 - 1])

            self.updateProbMoving(self.grid, terrainList,[type1, type2])
            [Type1,Type2]= [type1, type2]
            if (Type1 == '' and Type2 == ''):
                print('The Target is in', '[', self.grid.targetI, ',', self.grid.targetJ, ']')
            else:
                if Type1 == 1:
                    Type1 = 'flat'
                elif Type1 == 2:
                    Type1 = 'hill'
                elif Type1 == 3:
                    Type1 = 'forest'
                elif Type1 == 4:
                    Type1 = 'cave'

                if Type2 == 1:
                    Type2 = 'flat'
                elif Type2 == 2:
                    Type2 = 'hill'
                elif Type2 == 3:
                    Type2 = 'forest'
                elif Type2 == 4:
                    Type2 = 'cave'

                print('The Target moves to ', '[', self.grid.targetI, ',', self.grid.targetJ, ']', 'with type[', Type1,
                      ',',
                      Type2, ']')
        targetTerrian = ''
        if self.grid.getCell(targetI, targetJ).terrain == 1:
            targetTerrian = 'flat'
        elif self.grid.getCell(targetI, targetJ).terrain == 2:
            targetTerrian = 'hill'
        elif self.grid.getCell(targetI, targetJ).terrain == 3:
            targetTerrian = 'forest'
        elif self.grid.getCell(targetI, targetJ).terrain == 4:
            targetTerrian = 'cave'

        print('Target is founded at ', '[', targetI, ',', targetJ, '], type [', targetTerrian, '],', 'with',
              self.numOfSearches, 'searches')

    def probMoveCostSearch(self,rule):  # Q2 R3，R4
        rule1 = ''
        rule2 = ''
        if rule =='3':
            rule1 = self.RULE1
            rule2 = self.RULE3
        elif rule =='4':
            rule1 = self.RULE2
            rule2 = self.RULE4
        [a, b] = self.searchCell(self.grid, rule1)
        Type1 = ''
        Type2 = ''
        while True:
            self.numOfSearches += 1
            if self.findTarget(self.grid, a, b):
                targetI = a
                targetJ = b
                break
            [i, j] = self.searchCostCell(self.grid, rule2, a, b)
            self.updateProbStable(self.grid, a, b)
            print('Next search:', i, ',', j)
            print()
            [type1, type2] = self.moveTarget(self.grid)
            allList = self.getListOfEachTerrainType(self.grid)
            terrainList = []
            if type1 == type2:
                terrainList.append(allList[type1 - 1])
            else:
                terrainList.append(allList[type1 - 1])
                terrainList.append(allList[type2 - 1])

            self.updateProbMoving(self.grid, terrainList, [type1, type2])
            [a, b] = [i, j]
            [Type1,Type2]= [type1, type2]
            if (Type1 == '' and Type2 == ''):
                print('The Target is in', '[', self.grid.targetI, ',', self.grid.targetJ, ']')
            else:
                if Type1 == 1:
                    Type1 = 'flat'
                elif Type1 == 2:
                    Type1 = 'hill'
                elif Type1 == 3:
                    Type1 = 'forest'
                elif Type1 == 4:
                    Type1 = 'cave'

                if Type2 == 1:
                    Type2 = 'flat'
                elif Type2 == 2:
                    Type2 = 'hill'
                elif Type2 == 3:
                    Type2 = 'forest'
                elif Type2 == 4:
                    Type2 = 'cave'

                print('The Target moves to ', '[', self.grid.targetI, ',', self.grid.targetJ, ']', 'with type[', Type1,
                      ',',
                      Type2, ']')


        targetTerrian = ''
        if self.grid.getCell(targetI, targetJ).terrain == 1:
            targetTerrian = 'flat'
        elif self.grid.getCell(targetI, targetJ).terrain == 2:
            targetTerrian = 'hill'
        elif self.grid.getCell(targetI, targetJ).terrain == 3:
            targetTerrian = 'forest'
        elif self.grid.getCell(targetI, targetJ).terrain == 4:
            targetTerrian = 'cave'
        print('Target is founded at ', '[', targetI, ',', targetJ, '], type [', targetTerrian, '],', 'with',
              self.numOfSearches, 'searches')
        print('Total action ( move + search ) is:', action)
    def moveTarget(self, grid):
        i = grid.targetI
        j = grid.targetJ
        terrain1 = grid.getCell(i, j).terrain
        grid.getCell(i,j).isTarget = False

        if i != 0 and i != 49 and j != 0 and j != 49:
            moveto = random.randint(0, 3)
            if moveto == 0:
                j -= 1
            elif moveto == 1:
                i -= 1
            elif moveto == 2:
                j += 1
            else:
                i += 1
        elif i == 0:
            if j == 0:
                moveto = random.randint(0, 1)
                if moveto == 0:
                    j += 1
                else:
                    i += 1
            elif j == 49:
                moveto = random.randint(0, 1)
                if moveto == 0:
                    j -= 1
                else:
                    i += 1
            else:
                moveto = random.randint(0, 2)
                if moveto == 0:
                    j -= 1
                elif moveto == 1:
                    j += 1
                else:
                    i += 1
        elif i == 49:
            if j == 0:
                moveto = random.randint(0, 1)
                if moveto == 0:
                    j += 1
                else:
                    i -= 1
            elif j == 49:
                moveto = random.randint(0, 1)
                if moveto == 0:
                    j -= 1
                else:  # up
                    i -= 1
            else:
                moveto = random.randint(0, 2)
                if moveto == 0:
                    j -= 1
                elif moveto == 1:
                    j += 1
                else:  # up
                    i -= 1
        elif j == 0:
            if i == 0:
                moveto = random.randint(0, 1)
                if moveto == 0:
                    j += 1
                else:
                    i += 1
            elif i == 49:
                moveto = random.randint(0, 1)
                if moveto == 0:
                    j += 1
                else:
                    i -= 1
            else:
                moveto = random.randint(0, 2)
                if moveto == 0:
                    i += 1
                elif moveto == 1:
                    j += 1
                else:  # up
                    i -= 1
        elif j == 49:
            if i == 0:
                moveto = random.randint(0, 1)
                if moveto == 0:
                    j -= 1
                else:
                    i += 1
            elif i == 49:
                moveto = random.randint(0, 1)
                if moveto == 0:
                    j -= 1
                else:
                    i -= 1
            else:
                moveto = random.randint(0, 2)
                if moveto == 0:
                    i += 1
                elif moveto == 1:
                    j -= 1
                else:
                    i -= 1
        grid.targetI = i
        grid.targetJ = j
        terrain2 = grid.getCell(i, j).terrain
        grid.getCell(i,j).isTarget = True
        return [terrain1, terrain2]

    def getListOfEachTerrainType(self, grid):
        listT1 = []
        listT2 = []
        listT3 = []
        listT4 = []
        listT = []
        for i in range(grid.N):
            for j in range(grid.N):
                curCell = grid.getCell(i, j)
                if curCell.terrain == 1:
                    listT1.append(curCell)
                elif curCell.terrain == 2:
                    listT2.append(curCell)
                elif curCell.terrain == 3:
                    listT3.append(curCell)
                else:
                    listT4.append(curCell)
        listT.append(listT1)
        listT.append(listT2)
        listT.append(listT3)
        listT.append(listT4)

        return listT


if __name__ == '__main__':
    print('main method')
    a = input("Input 1 or 2 to choose Q1 or Q2:")
    if a == '1':
        b = input("Input 1 or 2 or 3 or 4 to choose Rule1 or Rule2 or Rule3 or Rule4:")
        if b == '1':
            probSearch = ProbSearch()
            probSearch.probSearch(b)
        elif b == '2':
            probSearch = ProbSearch()
            probSearch.probSearch(b)
        elif b == '3':
            probSearch = ProbSearch()
            probSearch.probCostSearch(b)
        elif b == '4':
            probSearch = ProbSearch()
            probSearch.probCostSearch(b)
        else:
            print("Invalid Input!")

    elif a == '2':
        b = input("Input 1 or 2 or 3 or 4 to choose Rule1 or Rule2 or Rule3 or Rule4:")
        if b == '1':
            probSearch = ProbSearch()
            probSearch.probMoveSearch(b)
        elif b == '2':
            probSearch = ProbSearch()
            probSearch.probMoveSearch(b)
        elif b == '3':
            probSearch = ProbSearch()
            probSearch.probMoveCostSearch(b)
        elif b == '4':
            probSearch = ProbSearch()
            probSearch.probMoveCostSearch(b)
        else:
            print("Invalid Input!")
    else:
        print("Invalid Input!")
