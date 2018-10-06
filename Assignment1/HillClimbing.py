class HillClimbing:
    def __init__(self, initSetsNum, mazeSize, p):
        self.initSetsNum = initSetsNum
        self.initSets = []
        self.mazeSize = mazeSize
        self.maze = []
        self.p = p
        self.finalSets = []

    def hillClimbing(self):
        exitFlag = False
        # 对每一个maze，找到他的最优解， 故循环100次
        for i in range(100):
            while(exitFlag):
                # 对当前的maze，爬山找到最优解
                next = self.randomWalk(self.initSets[i])
                if (self.evaluateMaze(next) > self.evaluateMaze(self.initSets[i])):
                    # 改变后的maze赋给当前的maze，进入下一次迭代
                    self.initSets[i] = next

            self.finalSets[i] = self.initSets[i]

        # 比较finalSets中的所有解，找到全局最优解


    def randomMaze(self):
        print('randomMaze')


    def randomWalk(self, maze):
        print('randomWalk')

    def evaluateMaze(self, maze):
        print('evaluateMaze')
        return 1

if __name__ == '__main__':
    print('main function')
    hillClimbing = HillClimbing(100, 100, 0.2)

