class Cell:
    def __init__(self, x, y, isWall):
        self.x = x
        self.y = y
        self.isWall = isWall
        self.g = 0
        self.h = 0
        self.f = 0
        self.parent = None
        self.visited = False

    def __lt__(self, other):
        return self.f < other.f

    def __gt__(self, other):
        return self.f > other.f
