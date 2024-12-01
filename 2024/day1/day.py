use_sample = True

def part1(filename: str = 'input.txt', mode: str = 'r'):
    input = read_file()

def part2(filename: str = 'input.txt', mode: str = 'r'):
    input = read_file()

def read_file(filename = 'input.txt', mode = 'r'):
    input = open(filename, mode)
    return input

print(f'Sample: {use_sample}')

print(f'Part1: {part1("sample.txt" if use_sample else "input.txt")}')

print(f'Part2: {part2("sample.txt" if use_sample else "input.txt")}')