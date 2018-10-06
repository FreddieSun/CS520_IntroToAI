import heapq
import random
import numpy as np
from Cell import *
import time
from PIL import Image
from scipy.spatial import distance


class AStarEuclidean:

    def __init__(self, N, p):
        self.openList = []
        self.closeList = set()
        self.grid = []
        self.N = N
        self.p = p
        heapq.heapify(self.openList)

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

        # print the maze
        for i in range(N):
            for j in range(N):
                print(1 if self.grid[i * self.N + j].isWall else 0, end = ''),
                print(' ', end = '')
                if j % N == N - 1:
                    print('')

    # return the cell according to the x and y
    def getCell(self, x, y):
        return self.grid[x * self.N + y]

    def printMaze(self):
        n = self.N
        maze = np.zeros([n, n])
        for i in range(n):
            for j in range(n):
                if self.grid[i * self.N + j].isWall:
                    maze[i][j] = 1
                else:
                    maze[i][j] = 0
        mazeDrown = Image.new('RGB', (n, n))
        mazeX = mazeDrown.load()
        for i in range(n):
            for j in range(n):
                if maze[i][j] == 0:
                    mazeX[i, j] = (255, 255, 255)
                else:
                    mazeX[i, j] = (0, 0, 0)
        path = self.showPath(self.destination)
        print(n)

        for i in path:
            mazeX[i] = (134, 205, 133)
        mazeDrown.show()


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
        return round(distance.euclidean((cell.x, cell. y), (self.N - 1, self.N - 1)))

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
            print('(' + str(curr.x) + ',' + str(curr.y) + ')' + '--', end='')
            pathx.append(curr.x)
            pathy.append(curr.y)
            curr = curr.parent
        print('(' + str(curr.x) + ',' + str(curr.y) + ')' + '--', end='')
        pathx.append(curr.x)
        pathy.append(curr.y)
        print('(' + str(self.start.x) + ',' + str(self.start.y) + ')', end='')
        pathx.append(self.start.x)
        pathy.append(self.start.y)
        print('\n')
        path = list(zip(pathx, pathy))
        return path


    # solve the maze
    def solveMaze(self):
        start = time.time()

        # add the start point into the heap
        heapq.heappush(self.openList, (0 + self.N - 2, self.start))

        # the flag to show if the maze has solution
        hasPath = False
        # Start the loop
        while len(self.openList) != 0:
            # pop the cell which with the min f out
            current = heapq.heappop(self.openList)[1]

            # check if the current cell arrives the destination
            if current == self.destination:
                print('find the path')
                self.showPath(current)
                self.printMaze()
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

        end = time.time()

        print('Running time is:', end - start, 's')

def main():
    aStar = AStarEuclidean(100, 0.2)
    aStar.solveMaze()

if __name__ == "__main__":
    main()
