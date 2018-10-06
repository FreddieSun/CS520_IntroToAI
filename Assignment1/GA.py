import random
import Cell

class GATool(object, initSetsNum, maze_size, p):
    def __init__(self):
        self.initSetsNum = initSetsNum
        self.initSets = []
        self.maze_size = maze_size
        self.maze = []
        self.p = p

    def produceInitSet(self):
        for i in range(self.initSetsNum):
            maze = []
            for j in range(self.maze_size):
                randomNum = random.randint(0, 1)

                if randomNum == 1:
                    maze.append(Cell(i,j,randomNum))

            self.initSets.append(init_maze[i])

    def variation(self, mazeCodes):
        for mazeCode in mazeCodes :
            variationPoint = random.randint()
            variationValue = random.randint(0,1)
            mazeCode[variationPoint] = variationValue
        return mazeCodes

    def fitness(self,mazeCode):
        # most length
        fitScore1 = len(mazeCode)
        fitScore2 = number of expands nodes
        fitScore3 = len(Fringe)
        return fitScore

    def process(self):
        self.produceInitSet()
        loopCount = 0
        exitFlag = False
        initCodes = self.initSets

        while(not exitFlag):
            for mazeCode in self.initSets:
                # find other terminal condition
                self.getPath()
                self.fitness()
                if end :
                    exitFlag == True

            variationCodes = self.variation(initCodes)
            initCodes = variationCodes

            loopCount += 1
            if loopCount == 1000:
                exitFlag == True

        print("times:", loopCount)

    def getPath(self):



