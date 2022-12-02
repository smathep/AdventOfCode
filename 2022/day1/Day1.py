def part1():
    input = open('input.txt', 'r')
    calories = 0
    max_calories = 0

    for line in input:
        if line == '\n':
            if calories > max_calories:
                max_calories = calories
            calories = 0
        else:
            calories += int(line)
    print(max_calories)

def part2():
    input = open('input.txt', 'r')
    calories = 0
    max_calories = 0

    calorie_list = []
    for line in input:
        if line == '\n':
            if calories > max_calories:
                calorie_list += [calories]
            calories = 0
        else:
            calories += int(line)
    calorie_list += [calories]
    sorted_calorie_list = sorted(calorie_list)
    print(sorted_calorie_list)
    print(sorted_calorie_list[-1]+sorted_calorie_list[-2]+sorted_calorie_list[-3])

# part1()
part2()