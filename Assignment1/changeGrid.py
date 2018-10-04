import random
def change_grid(self):
    # initialize father
    for cell in self.cells:
        cell.father = None

    # seperate cell into two obstacle and path
    for cell in self.cells[1:len(self.cells) - 1]:
        if cell.reachable is True:
            self.reachable_cells.append(cell)
        else:
            self.unreachable_cells.append(cell)

    # from obstacle find a cell
    obstacle_cell = self.unreachable_cells[random.randint(0, len(self.unreachable_cells) - 1)]

    # from non onstacle find a cell
    nonobstacle_cell = self.reachable_cells[random.randint(0, len(self.reachable_cells) - 1)]

    # remove a obstacle
    # self.get_cell(obstacle_cell.x, obstacle_cell.y).reachable = True

    # add a obstacle
    self.get_cell(nonobstacle_cell.x, nonobstacle_cell.y).reachable = False