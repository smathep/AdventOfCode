def part1():
    input = open('input.txt', 'r')
    overlappingPairs = 0
    for line in input:
        # print(line)
        elf1, elf2 = line.split(',')
        elf1 = elf1.split('-')
        elf2 = elf2.split('-')

        # yes, i know this is an ugly solution, but i had small edge cases that were eluding me so i just wanted to get the star
        if int(elf1[0]) > int(elf2[0]):
            if int(elf1[1]) <= int(elf2[1]):
                overlappingPairs += 1
                # print(f"Overlapping pair1: {line}")
        if int(elf2[0]) > int(elf1[0]):
            if int(elf2[1]) <= int(elf1[1]):
                overlappingPairs += 1
                # print(f"Overlapping pair2: {line}")
        if int(elf1[0]) == int(elf2[0]):
            if int(elf1[1]) <= int(elf2[1]):
                overlappingPairs += 1
                # print(f"Overlapping pair3: {line}")
            if int(elf2[1]) < int(elf1[1]):
                overlappingPairs += 1
                # print(f"Overlapping pair4: {line}")

            
    print(f"Overlapping pairs: {overlappingPairs}")
    return

def part2():
    input = open('input.txt', 'r')
    overlappingPairs = 0
    for line in input:
        print(line)
        elf1, elf2 = line.split(',')
        elf1 = elf1.split('-')
        elf2 = elf2.split('-')
        if int(elf2[0]) <= int(elf1[0]) <= int(elf2[1]):
            overlappingPairs += 1
        elif int(elf1[0]) <= int(elf2[0]) <= int(elf1[1]):
            overlappingPairs += 1

    print(f"Overlapping pairs: {overlappingPairs}")
    # return
    return

print('Part1:')
part1()

print('Part2:')
part2()