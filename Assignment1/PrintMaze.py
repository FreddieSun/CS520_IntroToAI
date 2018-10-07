import numpy as np
from PIL import Image


def printMaze(maze):
    n = int(np.sqrt(len(maze)))
    mazeinit = np.zeros([n, n])
    for i in range(n):
        for j in range(n):
            if maze[i * n + j].isWall:
                mazeinit[i][j] = 1
            else:
                mazeinit[i][j] = 0
    mazeDrown = Image.new('RGB', (n, n))
    mazeX = mazeDrown.load()
    for i in range(n):
        for j in range(n):
            if mazeinit[j][i] == 0:
                mazeX[i, j] = (255, 255, 255)
            else:
                mazeX[i, j] = (0, 0, 0)
    mazeDrown.show()