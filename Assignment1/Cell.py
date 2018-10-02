class Cell:
    def __init__(self, x, y, isWall, g, h, f,parent):
        self.x = x
        self.y = y
        self.isWall = isWall
        self.g = g
        self.h = h
        self.f = f
        self.parent=parent

