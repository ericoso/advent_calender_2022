with open("day4Input.txt") as f:
    lines = f.readlines()

sLines = []
for line in lines:
    sLine = line.strip("\n")
    sLines.append(sLine)

overlap = 0
overlapPairs = 0
for pair in sLines:
    elf = pair.split(",")
    ElfOne = elf[0].split("-")
    ElfTwo = elf[1].split("-")

    for i in range(len(ElfOne)):
        ElfOne[i] = int(ElfOne[i])

    for i in range(len(ElfTwo)):
        ElfTwo[i] = int(ElfTwo[i])

    if (ElfOne[0] >= ElfTwo[0] and ElfOne[1] <= ElfTwo[1]) or ((ElfOne[0] <= ElfTwo[0] and ElfOne[1] >= ElfTwo[1])):
        overlap +=1

    if (ElfOne[0] >= ElfTwo[0] and ElfOne[0] <= ElfTwo[1]) or ((ElfOne[0] <= ElfTwo[0] and ElfOne[1] >= ElfTwo[0])):
        overlapPairs +=1

print(overlap)
print(overlapPairs)
