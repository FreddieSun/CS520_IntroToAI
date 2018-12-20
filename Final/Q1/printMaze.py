from PIL import Image


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
        mazeX[i[1], i[0]] = (255, 255, 0)
    for i in mostcells:
        mazeX[i[1], i[0]] = (82, 198, 223)
    mazeDrown.show()