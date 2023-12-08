def part1():
    input = read_file()
    lines = input.read().splitlines()
    game_times = lines[0].split()[1:]
    distances = lines[1].split()[1:]
    best_times = []
    sum = 1
    for idx, time in enumerate(game_times):
        time = int(time)
        best_distance = distances[idx]
        # best_button_time = 0
        number_of_possabilities = 0
        print("game time: " + str(time))
        print("best distance: " + str(best_distance))
        for possible_time in range(int(time)):
            print("possible_time: " + str(possible_time) + " distance: " + str(possible_time * (time - possible_time)))
            distance = possible_time * (time - possible_time)
            # print("distance: " + str(distance))
            if distance > int(best_distance):
                print("new best distance: " + str(distance) + " new best time: " + str(possible_time))
                number_of_possabilities += 1
                # best_distance = distance
                # best_button_time = possible_time
            print("")
        best_times.append(number_of_possabilities)

    for time in best_times:
        print(time)
        sum *= time
    print(sum)


def part2():
    input = read_file()
    lines = input.read().splitlines()
    game_times = lines[0].replace(" ", "").split(":")[1]
    # game_times = lines[0].split()[1:]
    distances = lines[1].replace(" ", "").split(":")[1]
    best_times = []
    sum = 1
    for idx, time in enumerate([game_times]):
        time = int(time)
        best_distance = distances
        # best_button_time = 0
        number_of_possabilities = 0
        print("game time: " + str(time))
        print("best distance: " + str(best_distance))
        for possible_time in range(int(time)):
            # print("possible_time: " + str(possible_time) + " distance: " + str(possible_time * (time - possible_time)))
            distance = possible_time * (time - possible_time)
            # print("distance: " + str(distance))
            if distance > int(best_distance):
                # print("new best distance: " + str(distance) + " new best time: " + str(possible_time))
                number_of_possabilities += 1
                # best_distance = distance
                # best_button_time = possible_time
            # print("")
        best_times.append(number_of_possabilities)

    for time in best_times:
        print(time)
        sum *= time
    print(sum)

def read_file():
    input = open('input.txt', 'r')
    return input

print('Part1:')
part1()

print('Part2:')
part2()