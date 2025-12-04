import numpy as np

input = open('day-4-input').read()
grid = np.array([list(row) for row in input.split('\n')])
marked = np.zeros(shape = (grid.shape[0], grid.shape[1]), dtype = str)
accessible = 0

for coordinate, roll in np.ndenumerate(grid):
    if (roll != '@'):
        marked[coordinate[0]][coordinate[1]] = grid[coordinate[0]][coordinate[1]]
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
        marked[coordinate[0]][coordinate[1]] = 'X'
        accessible = accessible + 1
    else:
        marked[coordinate[0]][coordinate[1]] = roll

print(''.join(''.join(row) + '\n' for row in marked).strip())
print(accessible)