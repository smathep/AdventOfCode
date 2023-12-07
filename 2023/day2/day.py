import re

max_green = 13
max_red = 12
max_blue = 14
def part1():
    input = read_file()
    sum = 0
    for line in input:
        game_id = int(re.findall(r'\d+', line)[0])
        sets = line.split(';')
        sets[0] = sets[0][sets[0].find(':')+1:]
        print(sets)
        invalid_set_found = False
        for set in sets:
            if set.find('green') != -1:
                temp = re.findall(r'\d+ green', set)[0]
                green = int(re.search(r'\d+', temp).group())
                print('green: ' + str(green))
                if int(green) > max_green:
                    invalid_set_found = True
            if set.find('red') != -1:
                temp = re.findall(r'\d+ red', set)[0]
                red = int(re.search(r'\d+', temp).group())
                print('red: ' + str(red))
                if int(red) > max_red:
                    invalid_set_found = True
            if set.find('blue') != -1:
                temp = re.findall(r'\d+ blue', set)[0]
                blue = int(re.search(r'\d+', temp).group())
                print('blue: ' + str(blue))
                if int(blue) > max_blue:
                    invalid_set_found = True
            if invalid_set_found:
                break
        if not invalid_set_found:
            sum += game_id
        print(game_id)
    print("sum: " + str(sum))


def part2():
    input = read_file()
    sum = 0
    for line in input:
        game_id = int(re.findall(r'\d+', line)[0])
        sets = line.split(';')
        sets[0] = sets[0][sets[0].find(':')+1:]
        print(sets)
        game_red = 0
        game_blue = 0
        game_green = 0
        for set in sets:
            if set.find('green') != -1:
                temp = re.findall(r'\d+ green', set)[0]
                green = int(re.search(r'\d+', temp).group())
                # print('green: ' + str(green))
                if green > game_green:
                    game_green = green
            if set.find('red') != -1:
                temp = re.findall(r'\d+ red', set)[0]
                red = int(re.search(r'\d+', temp).group())
                # print('red: ' + str(red))
                if red > game_red:
                    game_red = red
            if set.find('blue') != -1:
                temp = re.findall(r'\d+ blue', set)[0]
                blue = int(re.search(r'\d+', temp).group())
                # print('blue: ' + str(blue))
                if blue > game_blue:
                    game_blue = blue
        print("min red: " + str(game_red))
        print("min blue: " + str(game_blue))
        print("min green: " + str(game_green))
        sum += game_red * game_blue * game_green
        print(game_id)
    print("sum: " + str(sum))

def read_file():
    input = open('input.txt', 'r')
    return input

# print('Part1:')
# part1()

print('Part2:')
part2()