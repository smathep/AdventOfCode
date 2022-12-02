def part1():
    input = open('input.txt', 'r')
    score = 0
    for line in input:
        opponent_move, my_move = line.split()
        # print(f"Opponent move: {opponent_move}", f"My move: {my_move}")
        if my_move == 'X':
            score += 1
            # print("X")
        elif my_move == "Y":
            score += 2
            # print("Y")
        elif my_move == "Z":
            score += 3
            # print("Z")

        if opponent_move == 'A':
            if my_move == 'X':
                score += 3
            if my_move == 'Y':
                score += 6
        elif opponent_move == 'B':
            if my_move == 'Y':
                score += 3
            if my_move == 'Z':
                score += 6
        elif opponent_move == 'C':
            if my_move == 'X':
                score += 6
            if my_move == 'Z':
                score += 3
        print(score)
    print(f"Score: {score}")
    return

def part2():
    input = open('input.txt', 'r')
    score = 0
    for line in input:
        opponent_move, round_end = line.split()
        # print(f"Opponent move: {opponent_move}", f"My move: {round_end}")
        # if opponent_move == 'X':
            # score += 1
            # print("X")
        if round_end == "Y":
            score += 3
            if opponent_move == 'A':
                score += 1
            if opponent_move == 'B':
                score += 2
            if opponent_move == 'C':
                score += 3
            # print("Y")
        elif round_end == "Z":
            score += 6
            if opponent_move == 'A':
                score += 2
            if opponent_move == 'B':
                score += 3
            if opponent_move == 'C':
                score += 1
        elif round_end == "X":
            if opponent_move == 'A':
                score += 3
            if opponent_move == 'B':
                score += 1
            if opponent_move == 'C':
                score += 2

    print(f"Score: {score}")
    return

print('Part1:')
part1()

print('Part2:')
part2()