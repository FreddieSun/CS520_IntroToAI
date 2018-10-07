import numpy as np
from Cell import *
import random
import time
from PIL import Image


class DFS_Stack:

    def __init__(self, N, P, maze=None):
        self.maze = []

        # generate the maze
        # array=np.loadtxt("mazearray.txt", delimiter=',')
        if maze == None:
            self.N = N
            self.P = P
            for i in range(N):
                for j in range(N):
                    b = random.uniform(0, 1)
                    # b=array[i+j-2]
                    if b <= P:
                        # if b==1:
                        self.maze.append(Cell(i, j, True))
                    else:
                        self.maze.append(Cell(i, j, False))
            # set the start point and the destination point
            self.start = self.getCell(0, 0)
            self.start.__setattr__('isWall', False)
            self.destination = self.getCell(N - 1, N - 1)
            self.destination.__setattr__('isWall', False)

            # # print the maze
            # for i in range(N):
            #     for j in range(N):
            #         print(1 if self.maze[i * self.N + j].isWall else 0, end = ''),
            #         print(' ', end = '')
            #         if j % N == N - 1:
            #             print('')
        else:
            self.maze = maze
            self.N = len(maze)
            self.P = 0

    def printMaze(self):
        n = self.N
        maze = np.zeros([n, n])
        for i in range(n):
            for j in range(n):
                if self.maze[i * self.N + j].isWall:
                    maze[i][j] = 1
                else:
                    maze[i][j] = 0
        mazeDrown = Image.new('RGB', (n, n))
        mazeX = mazeDrown.load()
        for i in range(n):
            for j in range(n):
                if maze[j][i] == 0:
                    mazeX[i, j] = (255, 255, 255)
                else:
                    mazeX[i, j] = (0, 0, 0)
        path = self.showPath(self.destination)
        print(path)
        mazeDrown.show()
        for i in path:
            mazeX[i] = (134, 205, 133)
        mazeDrown.show()

    def dfs(self):
        stack = []
        stack.append(self.getCell(0, 0))
        hasPath = False
        start = time.time()
        numOfExpanded = 0
        mof = 0
        lop = 0
        while len(stack) != 0:
            if (len(stack) > mof):
                mof = len(stack)
            current = stack.pop()
            numOfExpanded += 1
            if current == self.destination:
                print('find the path')
                path = self.showPath(self.destination)
                lop = len(path)
                self.printMaze()
                hasPath = True
                break
            if not current.visited:
                current.visited = True
                for adj in self.getAdj(current):
                    if adj.visited:
                        continue
                    stack.append(adj)
                    adj.parent = current
        end = time.time()

        print('duration is: ', str(end - start), 's')
        if not hasPath:
            print('No Path')
        print('number of node expanded is: ', numOfExpanded)
        return [numOfExpanded,mof,lop]


    # return the adjacent cell of the input cell
    def getAdj(self, cell):
        adjs = []
        if cell.x > 0 and not self.getCell(cell.x - 1, cell.y).isWall:
            adjs.append(self.getCell(cell.x - 1, cell.y))
        if cell.y > 0 and not self.getCell(cell.x, cell.y - 1).isWall:
            adjs.append(self.getCell(cell.x, cell.y - 1))
        if cell.x < self.N - 1 and not self.getCell(cell.x + 1, cell.y).isWall:
            adjs.append(self.getCell(cell.x + 1, cell.y))
        if cell.y < self.N - 1 and not self.getCell(cell.x, cell.y + 1).isWall:
            adjs.append(self.getCell(cell.x, cell.y + 1))
        return adjs


    # return the cell according to the x and y
    def getCell(self, x, y):
        return self.maze[x * self.N + y]

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
        path = list(zip(pathy, pathx))
        return path


def main():
    # Generate the maze with size len(maze)*len(maze) and p
    dfs = DFS_Stack(99,0.2)
    print(dfs.dfs())



if __name__ == "__main__":
    main()
