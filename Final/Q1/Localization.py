import pandas as pd
def generateMaze(data):
    maze=[]
    for i in range(43):
        temp = []
        for j in data.loc[i]:
            temp2 = j
            for j2 in temp2:
                if j2 == 'G':
                    temp.append(0)
                else:
                    temp.append(int(j2))
        maze.append(temp)
    return maze

def getblocksaround(x,y,maze):
    number = 0
    if x == 0 or y == 0 or x == 42 or y == 56:
        return 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0:
                continue
            temp = maze[x + i][y + j]
            if temp == 1:
                number += 1
    return number

if __name__ == '__main__':
    data = pd.read_table("Maze.txt",header=None)
    maze = generateMaze(data)

