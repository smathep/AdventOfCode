from operator import countOf

def part1():
    sum = 0
    input = read_file()
    input = input.read().splitlines()
    for line in input:
        line = line.split(":")[1]
        card_points = 0
        winning_numbers, scratchoff_numbers = line.split("|")
        print(line)
        print("winning numbers: ", winning_numbers.split())
        for number in winning_numbers.split():
            num_times = countOf(scratchoff_numbers.split(), number.strip())
            if num_times > 0:
                print(number, num_times)
                if card_points > 0:
                    card_points *= 2 * num_times
                elif num_times == 1:
                    card_points = 1
                else:
                    card_points = 1 * ((num_times-1)*2)
        sum += card_points


    print(sum)

def part2():
    sum = 0
    input = read_file()
    input = input.read().splitlines()
    instances = dict()
    for line in input:
        instances[line] = 1
    for idx, line in enumerate(input):
        line = line.split(":")[1]
        match_count = 0
        winning_numbers, scratchoff_numbers = line.split("|")
        # print(line)
        # print("winning numbers: ", winning_numbers.split())
        for number in winning_numbers.split():
            num_times = countOf(scratchoff_numbers.split(), number.strip())
            match_count += num_times
            # if num_times > 0:
            #     print(number, num_times)
            #     if card_points > 0:
            #         card_points *= 2 * num_times
            #     elif num_times == 1:
            #         card_points = 1
            #     else:
            #         card_points = 1 * ((num_times-1)*2)
        for current_instance_count in range(instances.get(input[idx])):
            for count in range(match_count):
                instances[input[idx+count+1]] += 1
        # sum += card_points
    for key in instances:
        sum += instances[key]
        # print(key, instances[key])
    print(sum)

def read_file():
    input = open('input.txt', 'r')
    return input

print('Part1:')
part1()

print('Part2:')
part2()