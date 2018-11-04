import random
from Assignment3.Grid import *
from Assignment3.PrintGrid import *

class ProbSearch:

    def __init__(self):
        print('init method')
        self.grid = Grid()
        self.numOfSearches = 0
        grid.generateGrid()

    def findTarget(self, cell):
        print('findTarget method')

    def updateProb(self, cell):
        print('updateProb method')

    def searchCell(self, grid, type):
        print('searchCell method')

    def probSearch(self):
        print('probSearch method')

        while True:
            self.numOfSearches += 1
            print(self.numOfSearches,'th search')
            cell = self.searchCell()



if __name__ == '__main__':
    print('main method')
