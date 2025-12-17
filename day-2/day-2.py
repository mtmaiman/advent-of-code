def my_solution(file):
    ranges = [tuple(map(int, range.split('-'))) for range in open(file).read().split(',')]
    part1 = part2 = 0
    invalid_ids = []

    for id_range in ranges:
        for id in range(id_range[0], id_range[1] + 1):
            id = str(id)

            if (id[0:len(id) // 2] == id[len(id) // 2:len(id)]):
                part1 += int(id)
            
            for comparator_slice_end in range(1, len(id) // 2 + 1):
                comparator_slice = id[0:comparator_slice_end]

                for comparable_slice_start in range(comparator_slice_end, len(id), len(comparator_slice)):
                    if (comparator_slice != id[comparable_slice_start:comparable_slice_start + len(comparator_slice)]):
                        break
                else:
                    if (id in invalid_ids):
                        break
                    else:
                        invalid_ids.append(id)
                        part2 += int(id)

    print(part1)
    print(part2)

def reddit_solution(file):
    return


file = 'day-2.input'
my_solution(file)
print('')
reddit_solution(file)