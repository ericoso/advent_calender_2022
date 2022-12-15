with open("Test12.txt") as f:
    lines = f.readlines()

with open("day12input.txt") as f:
    lines = f.readlines()

sLines = []

for line in lines:
    sLine = line.strip("\n")
    sLine = sLine.replace(" ", "")
    sLines.append(sLine)


def compare_neigbours(currentpos=0, directions=[]):
    viableDirs = []
    for dir in directions:

        try:
            # if heightmap[currentpos + dir] >= heightmap[currentpos]:
            # print(heightmap[currentpos + dir])
            #     viableDirs.append(currentpos + dir)
            if  ord(heightmap[currentpos])- ord(heightmap[currentpos + dir]) <= 1:
                viableDirs.append(currentpos + dir)
        except:
            pass
    return viableDirs


def path_algoritm(path={}):
    buffer = {}
    for key in path:
        viable = compare_neigbours(key, neigbours)
        for i in viable:
            if i not in path:
                buffer[i] = path[key]

    for key in buffer:
        path[key] = buffer[key] + heightmap[key]
    print(path)


heightmap = {}
for y, line in enumerate(sLines):
    for x, character in enumerate(line):
        heightmap[complex(x, y)] = character
print(heightmap)

for item in heightmap.items():
    if item[1] == "S":
        indexS = item[0]
    if item[1] == "E":
        indexE = item[0]

heightmap[indexS] = "a"
heightmap[indexE] = "z"

currentPosition = indexE
neigbours = [(1), (-1), (complex(0, 1)), (complex(0, -1))]

path = {indexE: "z"}
print(path)
viable = compare_neigbours(currentPosition, neigbours)
for i in viable:

    if i not in path:
        path[i] = heightmap[currentPosition] + heightmap[i]


while indexS not in path:
    path_algoritm(path)

print(path[indexS])
print(len(path[indexS]) - 1)
low = 500
for value in path.values():
    if value[-1] == "a":
        print(value)
        if len(value) < low:
            low = len(value)
print(low-1)
