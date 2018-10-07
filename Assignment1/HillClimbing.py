import random
from Cell import *
from DFS_Stack import *
from AStarEuclidean import *
from AStarManhattan import *
from BFS_Queue import *


class HillClimbing:


    def __init__(self, initSetsNum, mazeSize, p):
        self.initSetsNum = initSetsNum
        self.initSets = []
        self.mazeSize = mazeSize
        self.maze = []
        self.p = p
        self.finalSets = []
        self.randomMaze(initSetsNum)
        self.A_STAR_MANHATTON = "A_STAR_MANHATTON"
        self.A_STAR_EUCLIDEAN = "A_STAR_EUCLIDEAN"
        self.DFS = "DFS"
        self.BFS = "BFS"
        self.LOP = "LOP"
        self.NOE = "NOE"
        self.MOF = "MOF"

    def hillClimbing(self):
        exitFlag = False
        # 对每一个maze，找到他的最优解， 故循环100次
        for i in range(100):
            while (exitFlag):
                # 对当前的maze，爬山找到最优解
                next = self.randomWalk(self.initSets[i])
                if (self.evaluateMaze(next) > self.evaluateMaze(self.initSets[i])):
                    # 改变后的maze赋给当前的maze，进入下一次迭代
                    self.initSets[i] = next

            self.finalSets[i] = self.initSets[i]

        # 比较finalSets中的所有解，找到全局最优解
        globalMax = 0
        globalMaxIndex = 0
        for i in range(100):
            temp = self.evaluateMaze(self.finalSets[i], self.A_STAR_MANHATTON, self.NOE)
            if temp > globalMax:
                globalMax = temp
                globalMaxIndex = i

        return self.finalSets[globalMaxIndex]


    def getCell(self, x, y, maze):
        return maze[x * self.mazeSize + y]

    # generate a random maze
    def generateMaze(self, mazeSize, p):
        tempMaze = []
        for i in range(mazeSize):
            for j in range(mazeSize):
                b = random.uniform(0, 1)
                if b <= p:
                    tempMaze.append(Cell(i, j, True))
                else:
                    tempMaze.append(Cell(i, j, False))
        tempMaze[0].isWall = False
        tempMaze[mazeSize * mazeSize - 1].isWall = False
        return tempMaze

    # generate a number of initSetsNum mazes and store them in the InitSets list.
    def randomMaze(self, initSetsNum):
        mazeSize = self.mazeSize
        p = self.p
        for i in range(initSetsNum):
            self.initSets.append(self.generateMaze(mazeSize, p))
        return self.initSets

    def randomWalk(self, maze):
        print('randomWalk')

    def evaluateMaze(self, maze, type, criteria):
        lop = 0
        noe = 0
        mof = 0
        if type == self.A_STAR_EUCLIDEAN:
            aStarEuclidean = AStarEuclidean(0, 0, maze)
            lop, noe, mof = aStarEuclidean.solveMaze()
        elif type == self.A_STAR_MANHATTON:
            aStarManhattan = AStarManhattan(0, 0, maze)
            lop, noe, mof = aStarManhattan.solveMaze()
        elif type == self.BFS:
            bfs = BFS_Queue(0, 0, maze)
            lop, noe, mof = bfs.bfs()
        else:
            dfs = DFS_Stack(0, 0, maze)
            lop, noe, mof = dfs.dfs()

        return [lop, noe, mof]


if __name__ == '__main__':
    print('main function')
    hillClimbing = HillClimbing(100, 100, 0.2)
    result = hillClimbing.evaluateMaze(hillClimbing.initSets[0], hillClimbing.BFS, hillClimbing.NOE)
    print(result)

