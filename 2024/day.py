import sys
sys.path.append('../')
from library import * # type: ignore
use_sample = True

def part1(filename: str = 'input.txt', mode: str = 'r'):
    input = Library.read_file(filename, mode)

def part2(filename: str = 'input.txt', mode: str = 'r'):
    input = Library.read_file(filename, mode)

print(f'Sample: {use_sample}')

print(f'Part1: {part1("sample.txt" if use_sample else "input.txt")}')

print(f'Part2: {part2("sample.txt" if use_sample else "input.txt")}')