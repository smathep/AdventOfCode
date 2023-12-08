def part1():
    input = read_file()
    input = input.read().splitlines()
    sum = 0
    for idx, line in enumerate(input):
        numberBuilder = ''
        hasDiagonalSymbol = False
        for charIdx, character in enumerate(line):
            if character.isdigit():
                numberBuilder += character
                if charIdx > 0 and idx > 0:
                    if (not input[idx-1][charIdx-1].isdigit()) and input[idx-1][charIdx-1] != ".":
                        hasDiagonalSymbol = True
                if idx > 0:
                    if (not input[idx-1][charIdx].isdigit()) and input[idx-1][charIdx] != ".":
                        hasDiagonalSymbol = True
                if charIdx < len(line) - 1 and idx > 0:
                    if (not input[idx-1][charIdx+1].isdigit()) and input[idx-1][charIdx+1] != ".":
                        hasDiagonalSymbol = True
                if charIdx > 0:
                    if (not line[charIdx-1].isdigit()) and line[charIdx-1] != ".":
                        hasDiagonalSymbol = True
                if charIdx < len(line) - 1:
                    if (not line[charIdx+1].isdigit()) and line[charIdx+1] != ".":
                        hasDiagonalSymbol = True
                if idx < len(input) - 1 and charIdx > 0:
                    if (not input[idx+1][charIdx-1].isdigit()) and input[idx+1][charIdx-1] != ".":
                        hasDiagonalSymbol = True
                if idx < len(input) - 1:
                    if (not input[idx+1][charIdx].isdigit()) and input[idx+1][charIdx] != ".":
                        hasDiagonalSymbol = True
                if idx < len(input) - 1 and charIdx < len(line) - 1:
                    if (not input[idx+1][charIdx+1].isdigit()) and input[idx+1][charIdx+1] != ".":
                        hasDiagonalSymbol = True

                if charIdx == len(line) - 1: #check if last character to add sum
                    if numberBuilder != '':
                        if hasDiagonalSymbol:
                            sum += int(numberBuilder)
                        numberBuilder = ''
                        hasDiagonalSymbol = False
            else:
                if numberBuilder != '':
                    if hasDiagonalSymbol:
                        sum += int(numberBuilder)
                    numberBuilder = ''
                    hasDiagonalSymbol = False
    print(sum)

def part2():
    input = read_file()

def read_file():
    input = open('input.txt', 'r')
    return input

print('Part1:')
part1()

print('Part2:')
part2()