class ProbSearch:

    def __init__(self):
        print('init method')

    def probSearch(self):
        print('probSearch method')

    def findTarget(self, cell):
        print('findTarget method')

    def updateProb(self, i, j, grid):
        searchedCell = grid.getCell(i,j)
        Pj = searchedCell.Pr1
        Tj = 1-searchedCell.Pf
        grid.getCell(i, j).Pr1 = Pj * Tj
        for ii in grid.N:
            for jj in grid.N:
                OtherCell = grid.getCell(ii,jj)
                if i == ii and j == jj:
                    continue
                else:
                    Pi = OtherCell.Pr1
                    grid.getCell(ii, jj).Pr1 = Pi * (1 + Pj * (1-Tj) / (1-Pj))
        return grid
        print('updateProb method')

    def searchCell(self):

        print('searchCell method')


if __name__ == '__main__':
    print('main method')
