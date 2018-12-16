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
'''
find the cell with 5 blocks around
'''
def get_5blocks_cell(maze):
    cell = []
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if getblocksaround(x, y, maze) ==5:
                cell.append([x,y])
    return cell
'''
move the cells 
actions =['U','D','L','R']
'''
def move(maze,cells, actions):
    for action in actions:
        if action == 'U':
            for cell in cells:
                if maze[cell[0]-1][cell[1]] == 0:
                    cell[0]-=1
        elif action == 'D':
            for cell in cells:
                if maze[cell[0]+1][cell[1]] == 0:
                    cell[0]+=1
        elif action == 'L':
            for cell in cells:
                if maze[cell[0]][cell[1]-1] == 0:
                    cell[1]-=1
        elif action == 'R':
            for cell in cells:
                if maze[cell[0]][cell[1]+1] == 0:
                    cell[1]+=1
    return cells

if __name__ == '__main__':
    data = pd.read_table("Maze.txt", header=None)
    maze = generateMaze(data)
