import pandas as pd
import numpy as np
from PIL import Image

def maze_generator(data):
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


def num_of_blocks_around(x, y, maze):
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


def get_blocks_cell(maze, observation):
    cells = []
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if num_of_blocks_around(x, y, maze) == observation:
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
        if num_of_blocks_around(cell[0], cell[1], maze) == obervation:
            returncell.append(cell)
    return returncell


def find_highest_prob(cells):
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

def printMaze(maze, cells, mostcells):
    mazeDrown = Image.new('RGB', (len(maze[0]), len(maze)))
    mazeX = mazeDrown.load()
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 0:
                mazeX[j, i] = (255, 255, 255)
            else:
                mazeX[j, i] = (0, 0, 0)
    for i in cells:
        mazeX[i[1], i[0]] = (0, 255, 0)
    for i in mostcells:
        mazeX[i[1], i[0]] = (255, 0, 0)
    mazeDrown.show()


if __name__ == '__main__':
    data = pd.read_table("Maze.txt", header=None)
    maze = maze_generator(data)
    observations = [5, 5, 5,3]
    actions = ['L', 'L','D']
    cells = get_blocks_cell(maze, observations[0])
    n = 0
    while n < len(actions):
        cells = update(maze, cells, actions[n], observations[n + 1])
        n += 1
    print(cells)
    mostcells = find_highest_prob(cells)
    print(mostcells)
    printMaze(maze, cells, mostcells)
