import random
from Cell import *
from DFS_Stack import *
from AStarEuclidean import *
from AStarManhattan import *
from BFS_Queue import *
import copy

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

    def evaluateMaze(self, maze, type):
        tempMaze = copy.deepcopy(maze)
        if type == self.A_STAR_EUCLIDEAN:
            aStarEuclidean = AStarEuclidean(0, 0, tempMaze)
            lop, noe, mof = aStarEuclidean.solveMaze()
        elif type == self.A_STAR_MANHATTON:
            aStarManhattan = AStarManhattan(0, 0, tempMaze)
            lop, noe, mof = aStarManhattan.solveMaze()
        elif type == self.BFS:
            bfs = BFS_Queue(0, 0, tempMaze)
            lop, noe, mof = bfs.bfs()
        else:
            dfs = DFS_Stack(0, 0, tempMaze)
            lop, noe, mof = dfs.dfs()

        return [lop, noe, mof]

    def randomWalk(self, maze, step):
        Wall = []
        notWall = []
        # seperate cell into two wall and notWall
        for cell in maze[1:len(self.maze) - 1]:
            if cell.isWall is True:
                Wall.append(cell)
            else:
                notWall.append(cell)
        # remove/add a wall
        randomNum = random.randint(0, 1)
        if randomNum == 0:
            for i in range(step):
                # from wall find a wallcell
                wallCell = Wall[random.randint(0, len(Wall) - 1)]
                self.getCell(wallCell.x, wallCell.y, maze).isWall = False
        else:
            for i in range(step):
                # from notwall find a notwallcell
                notWallCell = notWall[random.randint(0, len(notWall) - 1)]
                self.getCell(notWallCell.x, notWallCell.y, maze).isWall = True
        return maze


    def hillClimbing(self):
        print(self.evaluateMaze(self.initSets[0],'BFS'))

        # 对每一个maze，找到他的最优解， 故循环100次
        for i in range(1):
            for j in range(100):
                # 对当前的maze，爬山找到最优解
                next = self.randomWalk(self.initSets[i], 10)
                if self.evaluateMaze(next, 'BFS')[0] > self.evaluateMaze(self.initSets[i], 'BFS')[0]:
                    # 改变后的maze赋给当前的maze，进入下一次迭代
                    print('优化成功')
                    self.initSets[i] = next
                else:
                    print('优化失败')
            self.finalSets.append(self.initSets[i])
        print(self.evaluateMaze(self.finalSets[0], 'BFS'))
        # # 比较finalSets中的所有解，找到全局最优解
        # globalMax = 0
        # globalMaxIndex = 0
        # for i in range(100):
        #     temp = self.evaluateMaze(self.finalSets[i], self.A_STAR_MANHATTON, self.NOE)
        #     if temp > globalMax:
        #         globalMax = temp
        #         globalMaxIndex = i
        #
        # return self.finalSets[globalMaxIndex]


if __name__ == '__main__':
    print('main function')
    hillClimbing = HillClimbing(1, 100, 0.2)
    hillClimbing.hillClimbing()

