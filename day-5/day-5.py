def my_solution(file):
    ids, ingredients = [], []
    ranges, ints = open(file).read().split('\n\n')

    for line in ranges.splitlines():
        start, end = map(int, line.split('-'))
        ids.append((start, end))

    for line in ints.splitlines():
        ingredients.append(int(line))

    fresh = []

    for ingredient in ingredients:
        if (any(ingredient in range(id_range[0], id_range[1] + 1) for id_range in ids)):
            fresh.append(ingredient)

    print(f'part 1: {len(fresh)}')

    total_fresh = 0
    pointer = 0

    for start, end in sorted(ids):
        if (start <= pointer):
            start = pointer + 1

        if (start <= end):
            total_fresh = total_fresh + end - start + 1
            pointer = end

    print(f'part 2: {total_fresh}')

def reddit_solution(file):
    fresh, ingredients = open(file).read().split('\n\n')
    fresh = [[*map(int, id_range.split('-'))] for id_range in fresh.split('\n')]
    ingredients = [*map(int, ingredients.splitlines())]

    print(f'part 1: {sum(any(a <= i <= b for a, b in fresh) for i in ingredients)}')

    ans = curr = 0

    for start, end in sorted(fresh):
        start = max(start, curr + 1)
        ans += max(0, end - start + 1)
        curr = max(curr, end)

    print(f'part 2: {ans}')

file = 'day-5.input'
my_solution(file)
print('')
reddit_solution(file)