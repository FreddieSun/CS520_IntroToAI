import random
from Assignment3.Grid import *
from Assignment3.PrintGrid import *


class ProbSearch:

    def __init__(self):
        print('init method')
        self.RULE1 = 'rule1'
        self.RULE2 = 'rule2'
        self.grid = Grid()
        self.numOfSearches = 0
        self.grid.generateGrid()

    def findTarget(self, grid, i, j):
        prob = random.random()
        if not grid.getCell(i, j).isTarget:
            return False
        else:
            if grid.getCell(i, j).terrain == 1:
                if 0 <= prob < 0.1:
                    return False
                else:
                    return True

            if grid.getCell(i, j).terrain == 2:
                if 0 <= prob < 0.3:
                    return False
                else:
                    return True

            if grid.getCell(i, j).terrain == 3:
                if 0 <= prob < 0.7:
                    return False
                else:
                    return True

            if grid.getCell(i, j).terrain == 4:
                if 0 <= prob < 0.9:
                    return False
                else:
                    return True

        print('findTarget method')

    def updateProb(self, grid, i, j):
        searchedCell = grid.getCell(i,j)
        Pj = searchedCell.Pr1
        Tj = 1-searchedCell.Pf
        grid.getCell(i, j).Pr1 = Pj * Tj
        for ii in range(grid.N):
            for jj in range(grid.N):
                otherCell = grid.getCell(ii,jj)
                if i == ii and j == jj:
                    continue
                else:
                    Pi = otherCell.Pr1
                    grid.getCell(ii, jj).Pr1 = Pi * (1 + Pj * (1-Tj) / (1-Pj))
        print('updateProb method')

    def searchCell(self, grid, type):
        returnCell = grid.getCell(0,0)
        returni = 0
        returnj = 0
        if type == 'rule1':
            for i in range(50):
                for j in range(50):
                    if grid.getCell(i,j).Pr1 > returnCell.Pr1:
                        returnCell = grid.getCell(i,j)
                        returni = i
                        returnj = j
                    elif grid.getCell(i,j).Pr1 == returnCell.Pr1:
                        if grid.getCell(i,j).Pr2 > returnCell.Pr2:
                            returnCell = grid.getCell(i,j)
                            returni = i
                            returnj = j
        if type == 'rule2' :
            for i in range(50):
                for j in range(50):
                    if grid.getCell(i, j).Pr2 > returnCell.Pr2:
                        returnCell = grid.getCell(i, j)
                        returni = i
                        returnj = j
                    elif grid.getCell(i, j).Pr2 == returnCell.Pr2:
                        if grid.getCell(i, j).Pr1 > returnCell.Pr1:
                            returnCell = grid.getCell(i, j)
                            returni = i
                            returnj = j

        return [returni , returnj]


        print('searchCell method')
        return [1, 2]

    def probSearch(self):
        print('probSearch method')
        targetI = 0
        targetJ = 0

        while True:
            self.numOfSearches += 1
            print(self.numOfSearches, 'th search')
            [i, j] = self.searchCell(self.grid, self.RULE1)
            if self.findTarget(self.grid, i, j):
                targetI = i
                targetJ = j
                break
            self.updateProb(self.grid, i, j)

        print('Target is founded at ', '[', targetI, ',', targetJ, '], with ', self.numOfSearches, 'searches')


if __name__ == '__main__':
    print('main method')
    probSearch = ProbSearch()
    probSearch.probSearch()
