from __future__ import print_function
import numpy as np
from mazeCreator import createMaze
import sys

from Cell import *
import random
import time
from collections import deque

class BFS_Stack:

    def __init__(self, N, P):
        self.maze=[]
        self.N = N
        self.P = P

        # generate the maze
        for i in range(N):
            for j in range(N):
                b = random.uniform(0, 1)
                if b <= P:
                    self.maze.append(Cell(i, j, True))
                else:
                    self.maze.append(Cell(i, j, False))
        # set the start point and the destination point
        self.start = self.getCell(0, 0)
        self.start.__setattr__('isWall', False)
        self.destination = self.getCell(N - 1, N - 1)
        self.destination.__setattr__('isWall', False)

        # print the maze
        for i in range(N):
            for j in range(N):
                print(1 if self.maze[i * self.N + j].isWall else 0, end=''),
                print(' ', end='')
                if j % N == N - 1:
                    print('')



    def bfs(self):
        queue = deque()
        queue.append(self.getCell(0,0))
        hasPath = False
        start = time.time()
        while len(queue) != 0:
            current = queue.popleft()
            if current == self.destination:
                print('find the path')
                self.showPath(self.destination)
                hasPath = True
                break
            if not current.visited:
                current.visited = True
                for adj in self.getAdj(current):
                    if adj.visited:
                        continue
                    queue.append(adj)
                    adj.parent = current
        end = time.time()

        print('duration is: ', str(end - start), 's')
        if not hasPath:
            print('No Path')


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


    # return the cell according to the x and y
    def getCell(self, x, y):
        return self.maze[x * self.N + y]

    # print the path
    def showPath(self, destination):
        curr = destination
        while curr.parent != self.start:
            print('(' + str(curr.x) + ',' + str(curr.y) + ')' + '--', end='')
            curr = curr.parent
        print('(' + str(curr.x) + ',' + str(curr.y) + ')' + '--', end='')
        print('(' + str(self.start.x) + ',' + str(self.start.y) + ')', end='')
        print('\n')


def main():
    # Generate the maze with size len(maze)*len(maze) and p
    bfs = BFS_Stack(9,0.4)
    bfs.bfs()



if __name__ == "__main__":
    main()