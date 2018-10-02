import heapq
import random
from Cell import *


class AStarEuclidean:

    def __init__(self, N, p):
        self.openList = []
        self.closeList = set()
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

        self.start = self.getCell(0, 0)
        self.start.__setattr__('isWall', False)
        self.destination = self.getCell(N - 1, N - 1)
        self.destination.__setattr__('isWall', False)

    # return the cell according to the x and y
    def getCell(self, x, y):
        return self.grid[x * self.N + y]

    def getAdj(self, cell):
        adjs = []
        if cell.x < self.N - 1:
            adjs.append(self.getCell(cell.x + 1, cell.y))
        if cell.x > 0:
            adjs.append(self.getCell(cell.x - 1, cell.y))
        if cell.y < self.N - 1:
            adjs.append(self.getCell(cell.x, cell.y + 1))
        if cell.y > 0:
            adjs.append(self.getCell(cell.x, cell.y - 1))
        return adjs

    def getHeuristics(self, cell):
        return abs(cell.x - self.N) + abs(cell.y - self.N)

    def updateCell(self, cell, adj):
        adj.g = cell.g + 1
        adj.h = self.getHeuristics(adj)
        adj.parent = cell

    def showPath(self, destination):
        curr = destination
        while curr.parent != self.start:
            print('(' + curr.x + ',' + curr.y + ')' + '--')
            curr = curr.parent

    def AStarEuclidean(self):
        heapq.heapify(self.openList)
        heapq.heappush(self.openList, ((0 + self.N - 2, self.start)))

        while len(self.openList) != 0:
            current = heapq.heappop(self.openlist)[1]
            if current == self.destination:
                print('find the path')
                self.showPath(current)
                break

            self.closeList.add(current)

            adjs = self.getAdj(current)
            for adj in adjs:
                if adj in self.closeList:
                    continue

                if adj not in self.openList:
                    heapq.heappush(self.openList, (current.g + 1 + self.getHeuristics(adj), adj))
                elif current.g + 1 > adj.g:
                    continue

                self.updateCell(current, adj)


def main():
    aStar = AStarEuclidean(5, 1)
    aStar.AStarEuclidean()


if __name__ == "__main__":
    main()
