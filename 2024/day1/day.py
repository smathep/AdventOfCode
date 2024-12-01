import sys
sys.path.append('../')
from library import * # type: ignore

use_sample = False

def part1(filename: str = 'input.txt', mode: str = 'r'):
    input = read_file(filename, mode)
    sorted_left, sorted_right = Library.split_input_sorted(input)

    total_distance = 0
    for i in range(len(sorted_left)):
        total_distance += abs(int(sorted_left[i]) - int(sorted_right[i])) 
    return total_distance

def part2(filename: str = 'input.txt', mode: str = 'r'):
    input = read_file(filename, mode)
    left_column, right_column = Library.split_input(input)
    
    similarity_score = 0
    for i in range(len(left_column)):
        similarity_score += int(left_column[i]) * right_column.count(left_column[i])
    return similarity_score

def read_file(filename = 'input.txt', mode = 'r'):
    input = open(filename, mode)
    return input

print(f'Sample: {use_sample}')

print(f'Part1: {part1("sample.txt" if use_sample else "input.txt")}')

print(f'Part2: {part2("sample.txt" if use_sample else "input.txt")}')