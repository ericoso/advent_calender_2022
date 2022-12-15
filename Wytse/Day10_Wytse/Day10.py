with open("Test10.txt") as f:
    lines = f.readlines()

sLines = []
for line in lines:
    sLine = line.strip("\n")
    sLine = sLine.replace(" ", "")
    sLines.append(sLine)


def signal_strength(tick):


    if tick / 20 == 1:
        # print(registerX * tick)
        return registerX * tick

    elif (tick - 20) % 40 == 0:
        # print(registerX * tick)
        return registerX * tick
    else:
        return 0


signal = 0
cycle = 0
registerX = 1
crtpicture=[]
crtrow = ""
for instruction in sLines:
    if instruction == "noop":
        if cycle == registerX or cycle - registerX == -1 or cycle - registerX == 1:
            crtrow += "#"
        else:
            crtrow += "."
        # signal += signal_strength(cycle)
        if cycle / 40 == 1:
            crtpicture.append(crtrow)
            crtrow = ""
            cycle = 0
        cycle += 1
        # signal += signal_strength(cycle)


    if instruction[:4] == "addx":
        if cycle == registerX or cycle - registerX == -1 or cycle - registerX == 1:
            crtrow += "#"
        else:
            crtrow += "."
        # signal += signal_strength(cycle)
        if cycle / 40 == 1:
            crtpicture.append(crtrow)
            crtrow = ""
            cycle = 0
        cycle += 1
        if cycle == registerX or cycle - registerX == -1 or cycle - registerX == 1:
            crtrow += "#"
        else:
            crtrow += "."
        # signal += signal_strength(cycle)
        if cycle / 40 == 1:
            crtpicture.append(crtrow)
            crtrow = ""
            cycle = 0

        cycle += 1

        # signal += signal_strength(cycle)
        registerX += int(instruction[4:])


    if len(crtrow) == 39:
        print(crtrow)
print(crtpicture)
for pic in crtpicture:
    print(pic)

