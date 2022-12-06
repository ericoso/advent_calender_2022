with open("day5Input.txt") as f:
    lines = f.readlines()

sLines = []
for line in lines:
    sLine = line.strip("\n")
    sLines.append(sLine)

# MoveList = ["move 1 from 2 to 1", "move 3 from 1 to 3", "move 2 from 2 to 1", "move 1 from 1 to 2"]
# CrateDistribution = [["[Z]", "[N]"], ["[M]", "[C]", "[D]"], ["[P]"]]
MoveList = []
CrateDistribution = []

for x in range(9):
    CrateDistribution.append([])

line: str
for line in sLines:
    if line.startswith("move "):
        MoveList.append(line)
    elif "[" in line:
        for number in range(0, len(line), 4):
            if line[number] == "[":
                CrateDistribution[int(number / 4)].insert(0,line[int(number):int(number) + 3])

CrateDistribution9001 = CrateDistribution

for instruction in MoveList:
    seperation = instruction.split(" ")
    amount = int(seperation[1])
    print(instruction)
    origin = int(seperation[3]) - 1
    destination = int(seperation[5]) - 1

    # for number in range(amount):
    #     CrateDistribution[destination].append(CrateDistribution[origin][-1])
    #     CrateDistribution[origin].pop()

    buffer = []
    print(CrateDistribution9001)
    for number in range(amount):
        print(CrateDistribution9001[origin])
        buffer.append(CrateDistribution9001[origin][-1])
        CrateDistribution9001[origin].pop()

    for index in range(len(buffer)):
        if index == 0:
            CrateDistribution9001[destination].append(buffer[index])
        else:
            CrateDistribution9001[destination].insert(-index,buffer[index])
#
# for crates in CrateDistribution:
#     print(crates[-1])

for crates in CrateDistribution9001:
    print(crates[-1])