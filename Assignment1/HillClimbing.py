import random
from Cell import *
from DFS_Stack import *
from AStarEuclidean import *
from AStarManhattan import *
from BFS_Queue import *
import copy
from PrintMaze import *


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

    # get the cell from the maze
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

    # evaluate the hardness of maze from noe, mof, and lop
    def evaluateMaze(self, maze, type):
        tempMaze = copy.deepcopy(maze)
        if type == self.A_STAR_EUCLIDEAN:
            aStarEuclidean = AStarEuclidean(0, 0, tempMaze)
            [[noe, mof, lop], path, hasPath] = aStarEuclidean.solveMaze()
        elif type == self.A_STAR_MANHATTON:
            aStarManhattan = AStarManhattan(0, 0, tempMaze)
            [[noe, mof, lop], path, hasPath] = aStarManhattan.solveMaze()
        elif type == self.BFS:
            bfs = BFS_Queue(0, 0, tempMaze)
            [[noe, mof, lop], path, hasPath] = bfs.bfs()
        else:
            dfs = DFS_Stack(0, 0, tempMaze)
            [[noe, mof, lop], path, hasPath] = dfs.dfs()

        return [[noe, mof, lop], path, hasPath]

    # use random walk to change the maze
    def randomWalk(self, maze, step):
        tempMaze = copy.deepcopy(maze)

        Wall = []
        notWall = []

        # seperate cell into two: wall and notWall
        for cell in tempMaze[1:self.mazeSize * self.mazeSize - 1]:
            if cell.isWall is True:
                Wall.append(cell)
            else:
                notWall.append(cell)

        if len(Wall) == 0:
            print('BFS meets the hardest maze. the maze is empty')
            return tempMaze
        if len(notWall) == 0:
            print('the maze is all wall')
            return tempMaze

        # remove/add a wall
        randomNum = random.random()
        if 0 <= randomNum < 0.5:
            for i in range(step):
                # from wall find a wallcell
                wallCell = Wall[random.randint(0, len(Wall) - 1)]
                self.getCell(wallCell.x, wallCell.y, tempMaze).isWall = False
        else:
            for i in range(step):
                # from notwall find a notwallcell
                notWallCell = notWall[random.randint(0, len(notWall) - 1)]
                self.getCell(notWallCell.x, notWallCell.y, tempMaze).isWall = True
        return tempMaze

    def hillClimbing(self, type, criteria):
        criteriaIndex = 0
        if criteria == self.NOE:
            criteriaIndex = 0
        elif criteria == self.MOF:
            criteriaIndex = 1
        else:
            criteriaIndex = 2

        print(self.evaluateMaze(self.initSets[0], type))

        failMazeList = []

        # 对每一个maze，找到他的最优解， 故循环self.InitSetsNum次
        for i in range(self.initSetsNum):
            # random walk十次失败后，结束爬山算法
            consectiveFailNum = 0
            while (True):
                # 对当前的maze，爬山找到最优解
                next = self.randomWalk(self.initSets[i], 5)
                print('\n')
                currentValue = self.evaluateMaze(self.initSets[i], type)
                nextValue = self.evaluateMaze(next, type)

                if currentValue[2] == False:
                    failMazeList.append(i)
                    break

                if currentValue[0][criteriaIndex]  < nextValue[0][criteriaIndex]:
                    # 改变后的maze赋给当前的maze，进入下一次迭代
                    consectiveFailNum = 0
                    print('SUCCESS')
                    self.initSets[i] = next
                else:
                    consectiveFailNum += 1
                    print('FAIL')
                print(consectiveFailNum)
                if consectiveFailNum == 10:
                    if currentValue[2] == False:
                        failMazeList.append(i)
                    break
            self.finalSets.append(self.initSets[i])
            print('第' + str(i) + '结果: ' + str(self.evaluateMaze(self.finalSets[i], type)[0]))

        # 比较finalSets中的所有解，找到全局最优解
        globalMax = 0
        globalMaxIndex = 0


        for i in range(self.initSetsNum):
            if i in failMazeList:
                continue
            print('第' + str(i) +'迷宫的初始数据：', str(self.evaluateMaze(self.initSets[i], type)[0]))
            print('第' + str(i) +'迷宫的最终数据：', str(self.evaluateMaze(self.finalSets[i], type)[0]))
            temp = self.evaluateMaze(self.finalSets[i], type)[0]
            if temp[criteriaIndex] > globalMax:
                globalMax = temp[criteriaIndex]
                globalMaxIndex = i

        print('final result is: ' + str(self.evaluateMaze(self.finalSets[globalMaxIndex], type)[0]))
        path = self.evaluateMaze(self.finalSets[globalMaxIndex], type)[1]

        printPath(self.finalSets[globalMaxIndex], path)


if __name__ == '__main__':
    print('main function')
    hillClimbing = HillClimbing(10, 100, 0.3)
    hillClimbing.hillClimbing(hillClimbing.A_STAR_EUCLIDEAN, hillClimbing.NOE)
