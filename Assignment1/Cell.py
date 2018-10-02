class Cell:
    def __init__(self, x, y, isWall, parent, g, h, f):
        self.x = x
        self.y = y
        self.isWall = isWall
        self.g = g
        self.h = h
        self.f = f
        self.parent=parent

