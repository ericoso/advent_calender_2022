import numpy as np

completlist =[]
for f in open("day8Input.txt"):
    completlist.append(list(f.strip()))


grid = np.array(completlist, int)

part1 = np.zeros_like(grid, int)
part2 = np.ones_like(grid, int)


for _ in range(4):
    for x, y in np.ndindex(grid.shape):
        lower = [t < grid[x, y] for t in grid[x, y + 1:]]
        part1[x, y] |= all(lower)
        part2[x, y] *= next((i + 1 for i, t in enumerate(lower) if ~t), len(lower))

    grid, part1, part2 = map(np.rot90, [grid, part1, part2])


print(part1.sum(), part2.max())

#
#
#
#
# with open("day8Input.txt") as f:
#     lines = f.readlines()
#
# lines = ["30373", "25512", "65332", "33549", "35390"]
#
# visibleTrees = 0
# Visible = []
#
# columns = []
# for index in range(len(lines)):
#     boffer = ""
#     for line in lines:
#         boffer += line[index]
#
#     columns.append(boffer)
#
#
# rowcount = 0
# for row in lines:
#
#     if rowcount != 0 and rowcount != len(lines) - 1:
#         columncount = 0
#         print(row)
#         for three in row:
#             if columncount != 0 and columncount != len(columns) - 1:
#                 print(row[:columncount-1])
#                 leftBuffer = "-1"
#                 for rowComparisonLeft in row[:columncount - 1]:
#                     if rowComparisonLeft > leftBuffer:
#                         leftBuffer = rowComparisonLeft
#
#                 if row[columncount] > leftBuffer:
#                     visibleTrees += 1
#
#
#
#
#
#             else:
#                 visibleTrees += 2
#
#             columncount += 1
#
#
#     else:
#         visibleTrees += len(row)
#
#     rowcount += 1
#
# print("visible = " + str(visibleTrees))

