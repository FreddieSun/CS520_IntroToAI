import pandas as pd
from PIL import Image

'''
transfer the data in the txt file into array
'''


def read_file_data(data):
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


'''
get the number of surrounded cells of your current position
'''


def get_surrounded_block_cell_number(x, y, maze):
    number = 0
    if x == 0 or y == 0 or x == 42 or y == 56:
        return 0
    if maze[x][y] == 1:
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
find the cells with 5 blocks around
'''


def get_cells(maze, observation):
    cells = []
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if get_surrounded_block_cell_number(x, y, maze) == observation:
                cells.append([x, y])
    return cells


'''
move the cells 
actions =['U','D','L','R']
'''


def move_cells(maze, cells, action):
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


'''
update cells array
'''


def update_cells(maze, cells, action, obervation):
    nextcells = move_cells(maze, cells, action)
    returncell = []
    for cell in nextcells:
        if get_surrounded_block_cell_number(cell[0], cell[1], maze) == obervation:
            returncell.append(cell)
    return returncell


'''
use dict to find the cells with highest probabilities
'''


def find_highest_probability(cells):
    info = dict()
    for i in range(len(cells)):
        (x, y) = cells[i]
        key = (x, y)
        if key not in info:
            info[key] = 1
        else:
            info[key] = info.get(key) + 1

    maxValue = 0
    for key, value in info.items():
        if value >= maxValue:
            maxValue = value

    result = []
    result1 = []
    for key, value in info.items():
        if value == maxValue:
            result.append(key)
        else:
            result1.append(key)
    return [result, result1, maxValue]


def draw_maze(maze, cells, most_cells):
    mazeDrown = Image.new('RGB', (len(maze[0]), len(maze)))
    mazeX = mazeDrown.load()
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 0:
                mazeX[j, i] = (255, 255, 255)
            else:
                mazeX[j, i] = (0, 0, 0)
    for i in cells:
        mazeX[i[1], i[0]] = (0, 153, 51)
    for i in most_cells:
        mazeX[i[1], i[0]] = (204, 0, 153)
    mazeDrown.show()


if __name__ == '__main__':
    file_data = pd.read_table("Maze.txt", header=None)
    Maze = read_file_data(file_data)
    observations_sequence = [5, 5, 5]
    actions_sequence = ['L', 'L']
    Cells = get_cells(Maze, observations_sequence[0])
    print(Cells)
    print(len(Cells))
    n = 0
    while n < len(actions_sequence):
        Cells = update_cells(Maze, Cells, actions_sequence[n], observations_sequence[n + 1])
        n += 1
    print(Cells)
    print(len(Cells))
    mostCells = find_highest_probability(Cells)
    print(mostCells[0])
    print(mostCells[2])

    # count the number of white cells in the maze
    # count = 0
    # for i in range(len(Maze)):
    #     for j in range(len(Maze[0])):
    #         if Maze[i][j] == 0:
    #             count += 1
    # print(count)

    draw_maze(Maze, Cells, mostCells[0])
