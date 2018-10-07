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

    def printMaze(self,maze):
        n=self.mazeSize
        mazeinit = np.zeros([n, n])
        for i in range(n):
            for j in range(n):
                if maze[i * n + j].isWall:
                    mazeinit[i][j]=1
                else:
                    mazeinit[i][j]=0
        mazeDrown = Image.new('RGB', (n, n))
        mazeX = mazeDrown.load()
        for i in range(n):
            for j in range(n):
                if mazeinit[j][i] == 0:
                    mazeX[i, j] = (255, 255, 255)
                else:
                    mazeX[i, j] = (0, 0, 0)
        mazeDrown.show()

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
        tempMaze = copy.deepcopy(maze)

        Wall = []
        notWall = []
        if len(Wall) == 0:
            print('BFS meets the hardest maze. the maze is empty')
            return tempMaze
        if len(notWall) == 0:
            print('the maze is all wall')
            return tempMaze

        # seperate cell into two wall and notWall
        for cell in tempMaze[1:self.mazeSize * self.mazeSize - 1]:
            if cell.isWall is True:
                Wall.append(cell)
            else:
                notWall.append(cell)
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


    def hillClimbing(self, type):
        print(self.evaluateMaze(self.initSets[0], type))


        # 对每一个maze，找到他的最优解， 故循环100次
        for i in range(self.initSetsNum):
            consectiveFailNum = 0
            while(True):

                # 对当前的maze，爬山找到最优解
                next = self.randomWalk(self.initSets[i], 5)
                print('\n')
                if self.evaluateMaze(self.initSets[i], type)[0] < self.evaluateMaze(next, type)[0]:
                    # 改变后的maze赋给当前的maze，进入下一次迭代
                    consectiveFailNum = 0
                    print('SUCCESS')
                    self.initSets[i] = next
                else:
                    consectiveFailNum += 1
                    print('FAIL')
                print(consectiveFailNum)
                if consectiveFailNum == 10:
                    break

        self.finalSets.append(self.initSets[i])
        print('第' + str(i) + '结果: ' + str(self.evaluateMaze(self.finalSets[0]), type))

        # 比较finalSets中的所有解，找到全局最优解
        globalMax = 0
        globalMaxIndex = 0
        for i in range(1):
            temp = self.evaluateMaze(self.finalSets[i], self.BFS)
            if temp > globalMax:
                globalMax = temp
                globalMaxIndex = i

        print('final result is: ' + str(self.evaluateMaze(self.finalSets[globalMaxIndex], self.BFS)))


if __name__ == '__main__':
    print('main function')
    hillClimbing = HillClimbing(3, 100, 0.2)
    hillClimbing.hillClimbing(hillClimbing.DFS)


