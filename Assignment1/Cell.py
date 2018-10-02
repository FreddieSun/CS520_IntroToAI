class Cell:
    def __init__(self, x, y, isWall):
        self.x = x
        self.y = y
        self.isWall = isWall
        self.g = 0
        self.h = 0
        self.f = 0
        self.parent = None

