import heapq
import random
import time
from Cell import *
from PIL import Image
import numpy as np

class AStarManhattan:

    def __init__(self, N, p, maze = None):
        self.openList = []
        self.closeList = set()
        heapq.heapify(self.openList)

        if maze == None:
            self.grid = []
            self.N = N
            self.p = p

            # generate the maze
            for i in range(N):
                for j in range(N):
                    b = random.uniform(0, 1)
                    if b <= p:
                        self.grid.append(Cell(i, j, True))
                    else:
                        self.grid.append(Cell(i, j, False))

            # set the start point and the destination point
            self.start = self.getCell(0, 0)
            self.start.__setattr__('isWall', False)
            self.destination = self.getCell(N - 1, N - 1)
            self.destination.__setattr__('isWall', False)

        else:
            self.grid = maze
            self.N = int(np.sqrt(len(maze)))
            self.p = 0
            self.start = maze[0]
            self.destination = maze[self.N * self.N - 1]
        #print the maze
        for i in range(N):
             for j in range(N):
                 print(1 if self.grid[i * self.N + j].isWall else 0, end = ''),
                 print(' ', end = '')
                 if j % N == N - 1:
                     print('')



    def printMaze(self):
        n = self.N
        maze0 = np.zeros([n, n])
        for i in range(n):
            for j in range(n):
                if self.grid[i * self.N + j].isWall:
                    maze0[i][j] = 1
                else:
                    maze0[i][j] = 0
        mazeDrown = Image.new('RGB', (n, n))
        mazeX = mazeDrown.load()
        for i in range(n):
            for j in range(n):
                if maze0[i][j] == 0:
                    mazeX[j, i] = (255, 255, 255)
                else:
                    mazeX[j, i] = (0, 0, 0)
        path = self.showPath(self.destination)
        print(n)
        mazeDrown.show()
        for i in path:
            mazeX[i] = (134, 205, 133)
        mazeDrown.show()

        # return the cell according to the x and y
    def getCell(self, x, y):
        return self.grid[x * self.N + y]

    # return the adjacent cell of the input cell
    def getAdj(self, cell):
        adjs = []
        if cell.x < self.N - 1 and not self.getCell(cell.x + 1, cell.y).isWall:
            adjs.append(self.getCell(cell.x + 1, cell.y))
        if cell.x > 0 and not self.getCell(cell.x - 1, cell.y).isWall:
            adjs.append(self.getCell(cell.x - 1, cell.y))
        if cell.y < self.N - 1 and not self.getCell(cell.x, cell.y + 1).isWall:
            adjs.append(self.getCell(cell.x, cell.y + 1))
        if cell.y > 0 and not self.getCell(cell.x, cell.y - 1).isWall:
            adjs.append(self.getCell(cell.x, cell.y - 1))
        return adjs

    # get the heuristics value of the input cell
    def getHeuristics(self, cell):
        return abs(cell.x - self.N) + abs(cell.y - self.N)

    # update(relax) the current cell
    def updateCell(self, cell, adj):
        adj.g = cell.g + 1
        adj.h = self.getHeuristics(adj)
        adj.parent = cell

    # print the path
    def showPath(self, destination):
        pathx = []
        pathy = []
        curr = destination
        while curr.parent != self.start:
            # print('(' + str(curr.x) + ',' + str(curr.y) + ')' + '--', end='')
            pathx.append(curr.x)
            pathy.append(curr.y)
            curr = curr.parent
        # print('(' + str(curr.x) + ',' + str(curr.y) + ')' + '--', end='')
        pathx.append(curr.x)
        pathy.append(curr.y)
        # print('(' + str(self.start.x) + ',' + str(self.start.y) + ')', end='')
        pathx.append(self.start.x)
        pathy.append(self.start.y)
        # print('\n')
        # print('number of node expanded is: ' + str(len(self.closeList)))
        path = list(zip(pathx, pathy))
        return len(self.closeList),path

        # solve the maze
    def solveMaze(self):

        start = time.time()

        # add the start point into the heap
        heapq.heappush(self.openList, (0 + self.N - 2, self.start))

        # the flag to show if the maze has solution
        hasPath = False
        mof = 0
        numOfExpanded = 0
        lop = 0
        moflist=[]
        # Start the loop
        while len(self.openList) != 0:
            if (len(self.openList) > mof):
                mof = len(self.openList)
            # pop the cell which with the min f out
            current = heapq.heappop(self.openList)[1]

            # check if the current cell arrives the destination
            if current == self.destination:
                print('find the path')
                numOfExpanded, path = self.showPath(current)
                lop = len(path)
                hasPath = True
                break

            # add the cell into the close list
            self.closeList.add(current)

            # get the adjacent cells
            adjs = self.getAdj(current)
            for adj in adjs:
                # if visited before, pass
                if adj in self.closeList:
                    continue
                # if not visited before, add into the heap
                if adj not in self.openList:
                    heapq.heappush(self.openList, (current.g + 1 + self.getHeuristics(adj), adj))
                # check if the current path is the shortest path
                elif current.g + 1 > adj.g:
                    continue
                # update(relax) the cell
                self.updateCell(current, adj)



        if (not hasPath):
            print('No Path Found')
            # print(len(self.closeList))

        end = time.time()

        print('Running time is:', end - start, 's')
        numOfExpanded=len(self.closeList)

        return [numOfExpanded, mof,lop]


def main():
    aStar = AStarManhattan(4, 0.2)
    #[numOfExpanded, mof, lop]
    print(aStar.solveMaze())


if __name__ == "__main__":
    main()
