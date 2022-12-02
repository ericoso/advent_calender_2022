with open("advent2.txt", "r") as input_file:
    lines = input_file.readlines()

score = 0

# A and X are rock (1)
# B and Y are paper (2)
# C and Z are scissors (3)

for line in lines:
    turn = line.split(" ")
    opponent = turn[0]
    myself = turn[1].strip()
    if opponent == 'A':
        if myself == 'X':
            score += 4
        elif myself == "Y":
            score += 8
        elif myself == "Z":
            score += 3
    elif opponent == "B":
        if myself == "X":
            score += 1
        elif myself == "Y":
            score += 5
        elif myself == "Z":
            score += 9
    elif opponent == "C":
        if myself == "X":
            score += 7
        elif myself == "Y":
            score += 2
        elif myself == "Z":
            score += 6

print("The score before the second column has been explained: " + str(score))
score = 0


for line in lines:
    turn = line.split(" ")
    opponent = turn[0]
    myself = turn[1].strip()
    if opponent == 'A':  # Opponent plays Rock
        if myself == 'X':  # I should lose, thus play Scissors
            score += 3
        elif myself == "Y":  # We should draw, thus play Rock
            score += 4
        elif myself == "Z":  # I should win, thus play Paper
            score += 8
    elif opponent == "B":  # Opponent plays Paper
        if myself == "X":  # I should lose, thus play Rock
            score += 1
        elif myself == "Y":  # We should draw, thus play Paper
            score += 5
        elif myself == "Z":  # I should win, thus play Scissors
            score += 9
    elif opponent == "C":  # Opponent plays Scissors
        if myself == "X":  # I should lose, thus play Paper
            score += 2
        elif myself == "Y":  # We should draw, thus play Scissors
            score += 6
        elif myself == "Z":  # I should win, thus play Rock
            score += 7

print("The score after the second column has been explained: " + str(score))


