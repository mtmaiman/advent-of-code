import re
import math
import sys

def my_solution(file):
    grid = [re.sub(' +', ' ', line).strip().split(' ') for line in open(file, 'r').read().split('\n')]
    running_total = 0

    for column_index in range(0, len(grid[0])):
        column = [row[column_index] for row in grid]
        operation = column[-1]
        column_total = 0

        if (operation == '+'):
            column_total = sum([int(value) for value in column[0:-1]])
        else:
            column_total = math.prod([int(value) for value in column[0:-1]])

        running_total += column_total

    print(f'part 1: {running_total}')
    
    print(f'part 2: {running_total}')

def reddit_solution(file):
    return

file = 'day-6.demo'
sys.set_int_max_str_digits(1000000)
my_solution(file)
print('')
reddit_solution(file)