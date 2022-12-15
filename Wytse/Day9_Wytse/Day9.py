# with open("day9Input.txt") as f:
#     lines = f.readlines()
#
# with open("test9.txt") as f:
#     lines = f.readlines()
#
# sLines = []
# for line in lines:
#     sLine = line.strip("\n")
#     sLine = sLine.replace(" ", "")
#     sLines.append(sLine)
#
#
# def coord_update():
#     HeadCoordXY = [0, 0]
#     TailCoordXY = [0, 0]
#     AllTailCoords = []
#
#     match instruction[0]:
#         case "R":
#             for i in range(int(instruction[1:])):
#                 HeadCoordXY[0] += 1
#                 if abs(TailCoordXY[0] - HeadCoordXY[0]) >= 2:
#                     TailCoordXY[0] += 1
#                     if HeadCoordXY[1] - TailCoordXY[1] >= 1:
#                         TailCoordXY[1] += 1
#                     elif HeadCoordXY[1] - TailCoordXY[1] <= -1:
#                         TailCoordXY[1] -= 1
#                 AllTailCoords.append([TailCoordXY[0], TailCoordXY[1]])
#
#         case "U":
#             for i in range(int(instruction[1:])):
#                 HeadCoordXY[1] += 1
#
#                 if abs(TailCoordXY[1] - HeadCoordXY[1]) >= 2:
#                     TailCoordXY[1] += 1
#                     if HeadCoordXY[0] - TailCoordXY[0] >= 1:
#                         TailCoordXY[0] += 1
#                     elif HeadCoordXY[0] - TailCoordXY[0] <= -1:
#                         TailCoordXY[0] -= 1
#                 AllTailCoords.append([TailCoordXY[0], TailCoordXY[1]])
#
#         case "L":
#             for i in range(int(instruction[1:])):
#                 HeadCoordXY[0] -= 1
#
#                 if abs(TailCoordXY[0] - HeadCoordXY[0]) >= 2:
#                     TailCoordXY[0] -= 1
#                     if HeadCoordXY[1] - TailCoordXY[1] >= 1:
#                         TailCoordXY[1] += 1
#                     elif HeadCoordXY[1] - TailCoordXY[1] <= -1:
#                         TailCoordXY[1] -= 1
#                 AllTailCoords.append([TailCoordXY[0], TailCoordXY[1]])
#
#         case "D":
#             for i in range(int(instruction[1:])):
#                 HeadCoordXY[1] -= 1
#
#                 if abs(TailCoordXY[1] - HeadCoordXY[1]) >= 2:
#                     TailCoordXY[1] -= 1
#                     if HeadCoordXY[0] - TailCoordXY[0] >= 1:
#                         TailCoordXY[0] += 1
#                     elif HeadCoordXY[0] - TailCoordXY[0] <= -1:
#                         TailCoordXY[0] -= 1
#                 AllTailCoords.append([TailCoordXY[0], TailCoordXY[1]])
#     print(Allcoords)
#     return AllTailCoords
#
#
# Allcoords = []
# for instruction in sLines:
#     for RopeLength in range(1):
#         Allcoords.append(coord_update())
#
#
# print(Allcoords)
#
#
#
# UniqueCoords = []
#
# for coord in Allcoords:
#     if coord not in UniqueCoords:
#         UniqueCoords.append(coord)
#
# print(len(UniqueCoords))
rope = [0] * 10
seen = [set([x]) for x in rope]
dirs = {'L':+1, 'R':-1, 'D':1j, 'U':-1j}
sign = lambda x: complex((x.real>0) - (x.real<0), (x.imag>0) - (x.imag<0))

for line in open('day9Input.txt'):
    for _ in range(int(line[2:])):
        rope[0] += dirs[line[0]]

        for i in range(1, 10):
            dist = rope[i-1] - rope[i]
            if abs(dist) >= 2:
                rope[i] += sign(dist)
                seen[i].add(rope[i])

print(len(seen[1]), len(seen[9]))