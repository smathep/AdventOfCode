def part1():
    input = open('input.txt', 'r')
    priority = 0
    for line in input:
        compartmentOne = line[0:int(len(line)/2)]
        compartmentTwo = line[int(len(line)/2):len(line)-1]
        common = set(compartmentOne)&set(compartmentTwo)
        for c in common:
            if 'a' <= c <= 'z':
                priority += ord(c)-ord('a')+1
            elif 'A' <= c <= 'Z':
                priority += ord(c)-ord('A')+27
    print(f"Priority: {priority}")


def part2():
    input = open('input.txt', 'r').readlines()
    priority = 0
    # print(input[i:i+3] for i in range(0, len(input), 3))
    for i in range(0, len(input), 3):
        print(input[i:i+3])
        common = set(input[i][0:len(input[i])-1])&set(input[i+1][0:len(input[i+1])-1])&set(input[i+2][0:len(input[i+2])-1])
        for c in common:
            if 'a' <= c <= 'z':
                priority += ord(c)-ord('a')+1
                print(ord(c)-ord('a')+1)
            elif 'A' <= c <= 'Z':
                priority += ord(c)-ord('A')+27
                print(ord(c)-ord('A')+1)
    print(f"Priority: {priority}")
    return

# print('Part1:')
# part1()

print('Part2:')
part2()