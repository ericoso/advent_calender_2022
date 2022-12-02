with open("day2input.txt") as f:
    lines = f.readlines()

ScoreRock = 1
ScorePaper = 2
ScoreScissors = 3
ScoreWin = 6
ScoreDraw = 3
ScoreLose = 0

# rock -> scissors -> paper -> rock
# A = X = rock
# B = Y  = paper
# C = Z = scissors

TotalScore = 0
for line in lines:
    sLine = line.strip("\n")
    score = 0
    if sLine[0] == "A":
        if sLine[-1] == "X":
            score += ScoreDraw
            score += ScoreRock
        elif sLine[-1] == "Y":
            score += ScoreWin
            score += ScorePaper
        elif sLine[-1] == "Z":
            score += ScoreLose
            score += ScoreScissors
        else:
            print("error")

    if sLine[0] == "B":
        if sLine[-1] == "X":
            score += ScoreLose
            score += ScoreRock
        elif sLine[-1] == "Y":
            score += ScoreDraw
            score += ScorePaper
        elif sLine[-1] == "Z":
            score += ScoreWin
            score += ScoreScissors
        else:
            print("error")

    if sLine[0] == "C":
        if sLine[-1] == "X":
            score += ScoreWin
            score += ScoreRock
        elif sLine[-1] == "Y":
            score += ScoreLose
            score += ScorePaper
        elif sLine[-1] == "Z":
            score += ScoreDraw
            score += ScoreScissors
        else:
            print("error")

    TotalScore += score

print(TotalScore)
# rock -> scissors -> paper -> rock
# A = rock
# B = paper
# C = scissors
SmartScore = 0
for line in lines:
    sLine = line.strip("\n")

    score = 0
    if sLine[-1] == "X":
        score += ScoreLose
        if sLine[0] == "A":
            score += ScoreScissors
        elif sLine[0] == "B":
            score += ScoreRock
        elif sLine[0] == "C":
            score += ScorePaper
        else:
            print("error")

    elif sLine[-1] == "Y":
        score += ScoreDraw
        if sLine[0] == "A":
            score += ScoreRock
        elif sLine[0] == "B":
            score += ScorePaper
        elif sLine[0] == "C":
            score += ScoreScissors
        else:
            print("error")

    elif sLine[-1] == "Z":
        score += ScoreWin
        if sLine[0] == "A":
            score += ScorePaper
        elif sLine[0] == "B":
            score += ScoreScissors
        elif sLine[0] == "C":
            score += ScoreRock
        else:
            print("error")
    else:
        print("error")
    SmartScore += score

print(SmartScore)