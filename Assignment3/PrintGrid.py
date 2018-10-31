import pygame
from Assignment3.Cell import *
from Assignment3.Grid import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (192, 192, 192)
DARKGREY = (41,36,33)
GREEN = (61,145,64)

size = 10
gap = 1

HEIGHT = 10
WIDTH = 20
minP = 0.2



def gridList(grid):
    smallGrid = []
    for i in range(grid.N):
        for j in range(grid.N):
            smallGrid.append(grid.getCell(i, j))

    GridList = []
    for i in range(len(smallGrid)):
        if smallGrid[i].terrain == 1:
            GridList.append(1)
        elif smallGrid[i].terrain == 2:
            GridList.append(2)
        elif smallGrid[i].terrain == 3:
            GridList.append(3)
        elif smallGrid[i].terrain == 4:
            GridList.append(4)
        else:
            GridList.append(smallGrid[i].numOfMines)
    for i in range(len(smallGrid)):
        if smallGrid[i].isTarget == True:
            GridList.append(i)

    return GridList


def drawInitialGrid(gridlist, gridHeight, gridWidth):
    pygame.init()
    width = size * gridWidth + (gridWidth + 1) * gap
    height = size * gridHeight + (gridHeight + 1) * gap
    surface = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Maps")
    exitflag = True
    while exitflag:
        surface.fill(BLACK)
        for i in range(gridHeight):
            for j in range(gridWidth):
                if gridlist[i * gridWidth + j] == 1:
                    pygame.draw.rect(surface, WHITE, [(gap + size) * j + gap, (gap + size) * i + gap, size, size])
                elif gridlist[i * gridWidth + j] == 2:
                    pygame.draw.rect(surface, GREY, [(gap + size) * j + gap, (gap + size) * i + gap, size, size])
                elif gridlist[i * gridWidth + j] == 3:
                    pygame.draw.rect(surface, GREEN, [(gap + size) * j + gap, (gap + size) * i + gap, size, size])
                elif gridlist[i * gridWidth + j] == 4:
                    pygame.draw.rect(surface, DARKGREY, [(gap + size) * j + gap, (gap + size) * i + gap, size, size])
        target=gridlist[len(gridlist)-1]
        targeti = int (target / gridWidth)
        targetj = target - (gridWidth * targeti)
        number = pygame.font.SysFont('宋体', 20)
        numberSurface = number.render('T', True, RED)
        numberRect = numberSurface.get_rect()
        numberRect.center = ((gap + size) * targetj + gap + size / 2, (gap + size) * targeti + gap + size / 2)
        surface.blit(numberSurface, numberRect)

        pygame.display.flip()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exitflag = False

if __name__ == '__main__':
    grid = Grid(50)
    GridList = gridList(grid)
    print("flat ", grid.numofFlat)
    print("hill ", grid.numofHill)
    print("forest ", grid.numofForest)
    print("cave", grid.numofCave)
    drawInitialGrid(GridList,grid.N,grid.N)



