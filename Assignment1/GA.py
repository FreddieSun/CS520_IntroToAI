import random


class GATool(object):
    def __init__(self):
        self.initSetsNum = initSetsNum
        self.initSets = []
        self.maze_size = maze_size
        self.end_maze = []
        self.visited = []
        self.path = []


    def produceInitSet(self):
        for i in range(self.initSetsNum):
            init_maze = []
            for j in range(self.maze_size):
                init_maze[j] = random.randint(0, 1)
            self.initSets.append(init_maze[i])

    def select(self,mazeCodes):

        return mazeCodes

    def cross(self,mazeCodes):
        crossPoint = random.randint()
        for index in range(len(mazeCodes),2):
            mazeCodes[index] cross with mazeCodes[index+1] in crossPoint
        return mazeCodes


    def variation(self,mazeCodes):
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
                if mazeCode == self.end_maze:
                    exitFlag == True
                if self.visited == [1,1,1,1,1,1,1,1]:
                    exitFlag == True

            selectCodes = self.select(initCodes)
            crossCodes = self.cross(selectCodes)
            variationCodes = self.variation(crossCodes)
            initCodes = variationCodes

            loopCount += 1
            if loopCount == 1000:
                exitFlag == True

        print("times:", loopCount)
        self.getPath()

    def getPath(self):



