import pandas as pd


def generateMaze(data):
    maze = []
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


def getBlocksAround(x, y, maze):
    number = 0
    if x == 0 or y == 0 or x == 42 or y == 56:
        return 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            temp = maze[x + i][y + j]
            if temp == 1:
                number += 1
    return number


'''
find the cell with 5 blocks around
'''


def get_blocks_cell(maze, observation):
    cells = []
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if getBlocksAround(x, y, maze) == observation:
                cells.append([x, y])
    return cells


'''
move the cells 
actions =['U','D','L','R']
'''


def move(maze, cells, action):
    if action == 'U':
        for cell in cells:
            if maze[cell[0] - 1][cell[1]] == 0:
                cell[0] -= 1
    elif action == 'D':
        for cell in cells:
            if maze[cell[0] + 1][cell[1]] == 0:
                cell[0] += 1
    elif action == 'L':
        for cell in cells:
            if maze[cell[0]][cell[1] - 1] == 0:
                cell[1] -= 1
    elif action == 'R':
        for cell in cells:
            if maze[cell[0]][cell[1] + 1] == 0:
                cell[1] += 1
    return cells


def update(maze, cells, action, obervation):
    nextcells = move(maze, cells, action)
    returncell = []
    for cell in nextcells:
        if getBlocksAround(cell[0], cell[1], maze) == obervation:
            returncell.append(cell)
    return returncell


def findMostProbability1(cells):
    info = {}
    info = dict()
    for i in range(len(cells)):
        (ii, jj) = cells[i]
        key = (ii, jj)
        if info.__contains__(key):
            info[key] = info.get(key) + 1
        else:
            info[key] = 1

    max_key = cells[0]
    max_value = 0
    for key, value in info.items():
        if value > max_value:
            max_key = key
            max_value = value

    result = []
    for key, value in info.items():
        if value == max_value:
            result.append(key)

    return result


if __name__ == '__main__':
    data = pd.read_table("Maze.txt", header=None)
    maze = generateMaze(data)
    observations = [5, 5, 5]
    actions = ['L', 'L']
    cells = get_blocks_cell(maze, observations[0])
    n = 0
    while n < len(actions):
        cells = update(maze, cells, actions[n], observations[n + 1])
        n += 1
    print(findMostProbability(cells))
