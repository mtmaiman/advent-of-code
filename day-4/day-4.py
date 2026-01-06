import numpy as np

def my_solution(grid, removed = 0, initial = False):
    accessible = 0

    for coordinate, roll in np.ndenumerate(grid):
        if (roll != '@'):
            continue

        neighbors = [
            (coordinate[0] - 1, coordinate[1] - 1), # top left
            (coordinate[0] - 1, coordinate[1]), # top center
            (coordinate[0] - 1, coordinate[1] + 1), # top right
            (coordinate[0], coordinate[1] - 1), # adjacent left
            (coordinate[0], coordinate[1] + 1), # adjcent right
            (coordinate[0] + 1, coordinate[1] - 1), # bottom left
            (coordinate[0] + 1, coordinate[1]), # bottom center
            (coordinate[0] + 1, coordinate[1] + 1) # bottom right
        ]

        occupied = 0

        for neighbor in neighbors:
            if (neighbor[0] < 0 or neighbor[0] >= grid.shape[0] or neighbor[1] < 0 or neighbor[1] >= grid.shape[1]): # check bounds of neighbor
                continue

            if (grid[neighbor[0]][neighbor[1]] == '@'):
                occupied = occupied + 1

        if (occupied < 4):
            grid[coordinate[0]][coordinate[1]] = '.'
            accessible = accessible + 1
        else:
            grid[coordinate[0]][coordinate[1]] = roll

    if (initial):
        print(accessible)

    if (accessible == 0):
        return removed
    else:
        removed += accessible
        return my_solution(grid, removed = removed)


file = 'day-4.input'
input = open(file).read()
grid = np.array([list(row) for row in input.split('\n')])
removed = my_solution(grid, initial = True)
print(removed)