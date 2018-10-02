from mazeCreator import createMaze
from queue import PriorityQueue as PQueue
import random
from Cell import *

class AStarEuclidean:

    def __init__(self, N, p):
        self.open = []
        self.closed = []
        self.grid = []
        self.N = N
        self.p = p
        pq = PQueue(self.open)

        # generate the maze
        for i in range(N):
            for j in range(N):
                b = random.uniform(0, 1)
                if b <= p:
                    self.grid.append(Cell(i, j, True))
                else:
                    self.grid.append(Cell(i, j, False))

        # self.start =
        # self.destination =

    def AStarEuclidean(x, y, maze):


        if len(pq) != 0:
            print('123')


    def heuristics(x, y, maze):
        N = len(maze)
        return abs(pow(N - 1 - x, 2) + pow(N - 1 - y), 2)


def main():
    print('main function')
    aStar = AStarEuclidean(5,0.3)



if __name__ == "__main__":
    main()
