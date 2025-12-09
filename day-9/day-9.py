def my_solution(file):
    red_tiles = [tuple(map(int, line.strip().split(','))) for line in open(file)]
    max_area = 0

    for outer_coordinate in red_tiles[0:len(red_tiles) // 2]:
        for inner_coordinate in list(reversed(red_tiles))[0:len(red_tiles) // 2]:
            area = (abs(inner_coordinate[0] - outer_coordinate[0]) + 1) * (abs(inner_coordinate[1] - outer_coordinate[1]) + 1)
            max_area = area if (area > max_area) else max_area

    print(f'part 1: {max_area}')

    max_area = 0

    for outer_coordinate in red_tiles[0:len(red_tiles) // 2]:
        for inner_coordinate in list(reversed(red_tiles))[0:len(red_tiles) // 2]:
            for x, y in (
                (x, y)
                for x in range(min(outer_coordinate[0], inner_coordinate[0]), max(outer_coordinate[0], inner_coordinate[0]) + 1)
                for y in range(min(outer_coordinate[1], inner_coordinate[1]), max(outer_coordinate[1], inner_coordinate[1]) + 1)
            ):
                for tile in red_tiles:
                    if (tile == outer_coordinate or tile == inner_coordinate):
                        continue

                    if (tile[0] <= x and tile[1] <= y):
                        area += 1

            max_area = area if (area > max_area) else max_area

    print(f'part 2: {max_area}')


def reddit_solution(file):
    return

file = 'day-9.input'
my_solution(file)
print('')
reddit_solution(file)