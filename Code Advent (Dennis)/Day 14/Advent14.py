data = open("advent14.txt").read()
data = data.strip()
sand_origin = (500, 0)
sand_count = 0
part_1 = 0
part_2 = 0


def create_rock_map(data):
    for line in data.split("\n"):
        points = [tuple(map(int, p.split(","))) for p in line.split(" -> ")]
        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i + 1]
            rocks_x = range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1)
            rocks_y = range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1)
            rocks.update({(x, y) for x in rocks_x for y in rocks_y})

    return rocks


rocks = set()
rocks = create_rock_map(data)
max_y = max((y for _, y in rocks))  # For part 2

x, y = sand_origin
while True:
    if (x, y) in rocks:  # Start at 500, 0 point when a new sand grain falls
        (x, y) = sand_origin
    if y > max_y and part_1 == 0:  # When a grain of sand falls in the abyss
        part_1 = sand_count  # Set the answer to part 1 to the current count
    if (x, y + 1) not in rocks and y < max_y + 1:  # Try to fall straight down
        y += 1
    elif (x - 1, y + 1) not in rocks and y < max_y + 1:  # Try to go diagonally down-left
        x += -1
        y += 1
    elif (x + 1, y + 1) not in rocks and y < max_y + 1:  # Try to go diagonally down-right
        x += 1
        y += 1
    else:  # We cannot fall any further
        sand_count += 1
        rocks.add((x, y))  # Interpret the new sand grain as a rock
    if (x, y) == sand_origin:  # filled
        part_2 = sand_count
        break

print("The number of sand grains that have fallen before the first sand grain falls into the abyss is", part_1)
print("The number of sand grains that have fallen before the sand origin becomes blocked is", part_2)
