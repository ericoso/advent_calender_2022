with open("input.txt") as f:
    lines = f.readlines()

elves = 0
CaloriesPerElf = [0]
TopElves = 3

for line in lines:

    if line == '\n':
        elves += 1
        CaloriesPerElf.append(0)

    sLine = line.strip("\n")
    if sLine != '':
        CaloriesPerElf[elves] += int(sLine)
TopElf = max(CaloriesPerElf)
print(TopElf)

total = 0
for x in range(TopElves):
    TopElf = max(CaloriesPerElf)
    total += TopElf
    pos = CaloriesPerElf.index(TopElf)
    CaloriesPerElf.pop(pos)

print(total)
