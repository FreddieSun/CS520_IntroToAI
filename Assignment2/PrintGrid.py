import pygame
from Grid import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY=(192,192,192)
size=20
gap=2

HEIGHT=10
WIDTH=20
minP=0.2

def createGrid(height,width,minP):
    grid = Grid(height,width,minP)
    grid.generateGrid()
    grid.markMineNumber()
    finalGrid=[]
    for i in  range(grid.height):
        for j in range(grid.width):
            finalGrid.append(grid.getCell(i,j))
    return finalGrid

def GridList(grid):
    GridList=[]
    for i in range(len(grid)):
        if grid[i].isMine == True:
            GridList.append(9)
        else:
            GridList.append((grid[i].numOfMines))
    return GridList


def drawInitialGrid(gridlist):
    pygame.init()
    width=size*WIDTH+(WIDTH+1)*gap
    height=size*HEIGHT+(HEIGHT+1)*gap
    surface=pygame.display.set_mode((width,height))
    pygame.display.set_caption("MineSweeper")
    exitflag=True
    while exitflag:
        surface.fill(BLACK)
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if gridlist[i*WIDTH+j] == 0:
                    pygame.draw.rect(surface,GREY,[(gap+size)*j+gap,(gap+size)*i+gap,size,size])
                elif gridlist[i*WIDTH+j] == 9:
                    pygame.draw.rect(surface, RED, [(gap + size) * j + gap, (gap + size) * i + gap, size, size])
                else:
                    pygame.draw.rect(surface, WHITE, [(gap + size) * j + gap, (gap + size) * i + gap, size, size])
                    number = pygame.font.SysFont('宋体', 20)
                    numberSurface = number.render(str(gridlist[i*WIDTH+j]), True, BLACK)
                    numberRect = numberSurface.get_rect()
                    numberRect.center = ((gap + size) * j + gap + size/2, (gap + size) * i + gap + size/2)
                    surface.blit(numberSurface, numberRect)
        pygame.display.flip()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exitflag = False

if __name__ == '__main__':
    grid=createGrid(HEIGHT,WIDTH,minP)
    print(grid)
    print(GridList(grid))
    drawInitialGrid(GridList(grid))





