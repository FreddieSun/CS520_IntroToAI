import pandas as pd
from printMaze import *


def maze_generator():
    data = pd.read_table("Maze.txt", header=None)
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


def move(maze, cells, action):
    for cell in cells:
        if action == 'U':
            if maze[cell[0] - 1][cell[1]] == 0:
                cell[0] -= 1
        elif action == 'D':
            if maze[cell[0] - 1][cell[1]] == 0:
                cell[0] -= 1
        elif action == 'L':
            if maze[cell[0]][cell[1] - 1] == 0:
                cell[1] -= 1
        elif action == 'R':
            if maze[cell[0]][cell[1] + 1] == 0:
                cell[1] += 1
    return cells


def num_of_blocks_around(x, y, maze):
    result = 0
    # if the current cell is obstacle, ignore it.
    if maze[x][y] == 1:
        return result

    # the border doesn't has 8 neighbors.
    if x == 0 or y == 0 or x == 42 or y == 56:
        return 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            if maze[x + i][y + j] == 1:
                result += 1
    return result


def get_blocks_cell(maze, observation):
    cells_meet_requirement = []
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if num_of_blocks_around(x, y, maze) == observation:
                cells_meet_requirement.append([x, y])
    return cells_meet_requirement


def update_current_cell_list(maze, cells, action, obervation):
    next_cells = move(maze, cells, action)
    return_cell = []
    for cell in next_cells:
        if num_of_blocks_around(cell[0], cell[1], maze) == obervation:
            return_cell.append(cell)
    return return_cell


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

    for key, value in info.items():
        # info[key] = info.get(key)/len(cells)
        print("key: ", key, "value: ", info.get(key) / len(cells))
    return result


if __name__ == '__main__':
    # Here is the observation and actions for this program
    observations = [5, 5, 5, 3]
    actions = ['L', 'L', 'U']

    # load the data from the txt file and load it into a list
    maze = maze_generator()

    first_observation = observations[0]

    cells = get_blocks_cell(maze, first_observation)

    for i in range(len(actions)):
        cells = update_current_cell_list(maze, cells, actions[i], observations[i + 1])


    print("The possible cells are:")
    print(cells)
    print("The number of solutions is: ", len(cells))
    high_prob_cells = find_highest_prob(cells)
    print("The most possible cells are: ")
    print(high_prob_cells)
    print("The number of most possible solutions is: ", len(high_prob_cells))
    printMaze(maze, cells, high_prob_cells)
