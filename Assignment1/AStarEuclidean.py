from mazeCreator import createMaze


def main():
    # Generate the maze with size N*N and p
    maze = createMaze(5, 0.1)
    print(maze)


if __name__ == "__main__":
    main()
