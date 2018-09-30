import random as rd
import sys
from PIL import Image

sys.setrecursionlimit(150000)

Size = 101
def create_maze():
    # Size of maze
    weight = Size
    height = Size

    # Initialize the visited matrix and maze matrix
    visited = [[0] * weight for _ in range(height)]
    maze = [[1] * weight for _ in range(height)]

    # Create a constant random list to make sure every time the maze is the same.
    randomNum = rd.Random();
    randomNum.seed(1)
    randomList = [randomNum.randint(0, 9) for i in range(Size*Size)]

    # Depth first search to create the maze
    def dfs(x, y, counter, randomList):

        # Mark this point as visited
        visited[y][x] = 1

        if (y >= 1 and y < height - 1 and x >= 1 and x < weight - 1):
            # direction list
            d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        else:
            if (y == 0):
                if (x == 0):
                    d = [(x + 1, y), (x, y + 1)]
                if (x == weight - 1):
                    d = [(x - 1, y), (x, y + 1)]
                if (x > 0 and x < weight - 1):
                    d = [(x, y + 1), (x - 1, y), (x + 1, y)]
            if (y == height - 1):
                if (x == 0):
                    d = [(x + 1, y), (x, y - 1)]
                if (x == weight - 1):
                    d = [(x - 1, y), (x, y - 1)]
                if (x > 0 and x < weight - 1):
                    d = [(x, y - 1), (x - 1, y), (x + 1, y)]
            if (y != 0 and y != height - 1):
                if (x == 0):
                    d = [(x + 1, y), (x, y + 1), (x, y - 1)]
                if (x == weight - 1):
                    d = [(x - 1, y), (x, y + 1), (x, y - 1)]

        rd.shuffle(d)

        for (xx, yy) in d:
            if visited[yy][xx]:
                continue
            if (randomList[counter] >= 0 and randomList[counter] <= 2):
                maze[yy][xx] = 0
            counter += 1
            dfs(xx, yy, counter, randomList)
        return tuple(maze)

    Counter = 0
    rd.seed(1)
    maze = dfs(rd.randrange(weight), rd.randrange(height), Counter, randomList)
    return maze

def draw_path(Maze, start, goal, path):
    imgx = Size
    imgy = Size
    image = Image.new("RGB", (imgx, imgy))
    pixels = image.load()

    for ky in range(Size):
        for kx in range(Size):
            if Maze[kx][ky] == 0:
                m = 0
            else:
                m = 255

            pixels[ky, kx] = (m, m, m)
    pixels[start[1], start[0]] = (255, 0, 0)
    pixels[goal[1], goal[0]] = (0, 0, 255)

    for index in range(1, len(path) - 1):
        pixels[int(path[index][1]), int(path[index][0])] = (0, 255, 0)

    A = image.resize((1024, 1024))
    A.save('Maze_path.jpg')


def draw_maze(Maze, start, goal):
    imgx = Size
    imgy = Size
    image = Image.new("RGB", (imgx, imgy))
    pixels = image.load()

    for ky in range(Size):
        for kx in range(Size):
            if Maze[kx][ky] == 0:
                m = 0
            else:
                m = 255

            pixels[ky, kx] = (m, m, m)
    pixels[start[1], start[0]] = (255, 0, 0)
    pixels[goal[1], goal[0]] = (0, 0, 255)

    A = image.resize((1024, 1024))
    A.save('Maze.jpg')

def show_maze():
    image = Image.open('Maze.jpg')
    image.show()

def show_path():
    image = Image.open('Maze_path.jpg')
    image.show()