import random
import numpy as np


def createMaze(n, p):
    maze = np.zeros([n, n])
    for i in range(n):
        for j in range(n):
            b = random.uniform(0, 1)
            if b <= p:
                maze[i][j] = 1
            else:
                maze[i][j] = 0
    maze[0][0] = 0
    maze[n - 1][n - 1] = 0
    return maze
