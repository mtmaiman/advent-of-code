from itertools import accumulate as acc # for reddit solution

def my_solution(file):
    instructions = [(line[0], int(line[1:].strip())) for line in open(file).readlines()]
    zeros = passes = 0
    start = 50
    on_zero = False

    for instruction in instructions:
        caesar = instruction[1] % 100
        passes += instruction[1] // 100
        direction = -1 if (instruction[0] == 'L') else 1
        start += caesar * direction

        if (start == 0 and caesar > 0):
            passes += 1
        elif (start < 0 or start > 99):
            if (not on_zero):
                passes += 1
                
            start = 100 + start if (start < 0) else start - 100

        if (start == 0):
            zeros += 1
            on_zero = True
        else:
            on_zero = False

    print(zeros)
    print(passes)

def reddit_solution(file):
    a, b = [50], [50]

    for line in open(file):
        dir = {'L': -1, 'R': +1}[line[0]]
        dist = int(line[1:])
        a += [dir * dist]
        b += [dir] * dist

    for x in a, b:
        print(sum(x%100==0 for x in acc(x)))


file = 'day-1.input'
my_solution(file)
print('')
reddit_solution(file)