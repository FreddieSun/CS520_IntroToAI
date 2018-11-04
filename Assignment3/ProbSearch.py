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
        grid.generateGrid()

    def findTarget(self, grid, i, j):
        print('findTarget method')

    def updateProb(self, grid, i, j):
        print('updateProb method')

    def searchCell(self, grid, type):
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
