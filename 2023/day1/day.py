import re

# numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"] 
numbers = {
    # "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}

def part1():
    input = open('input.txt', 'r')
    sum = 0
    for line in input:
        print(line)
        temp = re.findall(r'(\d)', line)
        number = int(temp[0]+temp[-1])
        print(number)
        sum+=number
    print(sum)
    


def part2():
    input = open('input.txt', 'r').readlines()
    sum = 0
    for line in input:
        print(line[0:-1])
        for index in line:
            firstNumIndex = 99999999
            firstKey = None
            for key, value in numbers.items():

                if(key in line):
                    if(line.index(key) < firstNumIndex):
                        firstNumIndex = line.index(key)
                        firstKey = key
            if firstKey != None:
                line = line.replace(firstKey[0:-1], str(numbers[firstKey])) #0:-1 to not destroy possible consecutive digits
        print("new line: ", line[0:-1])
        temp = re.findall(r'[1-9]', line)
        print("digits: ", temp)
        number = int(temp[0]+temp[-1])
        print(number)
        sum+=number
        print("sum: ", sum)
        print('\n')
    print(sum)
    return

print('Part1:')
# part1()

print('Part2:')
part2()