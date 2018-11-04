'''
flat   : terrain = 1
hill   : terrain = 2
forest : terrain = 3
cave   : terrain = 4
'''
class Cell:

    def __init__(self, terrain):
        self.terrain = terrain
        self.isTarget = False
        self.Pf = None
        self.Pr1 = None
        self.Pr2 = self.Pr1 * self.Pf







