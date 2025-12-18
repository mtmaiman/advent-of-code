from itertools import combinations

def my_solution(file):
    banks = [list(map(int, list(line.strip()))) for line in open(file).readlines()]
    total_max_2 = 0
    total_max_12 = 0

    for bank in banks:
        bank_max = 0
        
        for pair in combinations(bank, 2):
            bank_max = max(bank_max, int(''.join(str(battery) for battery in pair)))

        total_max_2 += bank_max

        '''
        # Hits memory limits
        for pair in combinations(bank, 12):
            bank_max = max(bank_max, int(''.join(str(battery) for battery in pair)))

        # Attempted one-liner but loses positional optimization
        total_max_12 += int(''.join([str(battery[0]) for battery in sorted(list(reversed(sorted([(value, index) for index, value in enumerate(bank)])))[0:12], key = lambda _: _[1])]))
        '''

        freespace = len(bank) - 12
        max_battery_builder = []

        for battery in bank:
            while (freespace and max_battery_builder and max_battery_builder[-1] < battery):
                max_battery_builder.pop()
                freespace -= 1
            
            max_battery_builder.append(battery)

        total_max_12 += int(''.join(str(battery) for battery in max_battery_builder[0:12]))
    
    print(total_max_2)
    print(total_max_12)

def reddit_solution(file):
    return


file = 'day-3.input'
my_solution(file)
print('')
reddit_solution(file)