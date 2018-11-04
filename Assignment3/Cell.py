'''
flat   : terrain = 1
hill   : terrain = 2
forest : terrain = 3
cave   : terrain = 4
'''


class Cell:

    def __init__(self, terrain, Pf):
        self.terrain = terrain
        self.isTarget = False
        self.Pf = Pf
        self.Pr1 = 1 / 2500
        self.Pr2 = self.Pr1 * self.Pf
