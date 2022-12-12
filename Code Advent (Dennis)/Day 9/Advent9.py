commands = []
part1 = set()
part2 = set()

# ----------------------------------- GENERIC FUNCTIONS -------------------------------------------
input_file = open("Advent9.txt", "r")
lines = input_file.readlines()

for line in lines:
    line = line.replace("\n", "")
    commands.append((line.split(" ")[0], int(line.split(" ")[1])))


def get_direction(dir):
    match dir:
        case "U":
            return [0, 1]
        case "R":
            return [1, 0]
        case "D":
            return [0, -1]
        case "L":
            return [-1, 0]


def move(head_pos, tail_pos):
    #  Determine the distance from T to H
    global distance_to_head
    distance_to_head[0] = head_pos[0] - tail_pos[0]
    distance_to_head[1] = head_pos[1] - tail_pos[1]
    print("Distance from T to H: ", distance_to_head)

    x_distance_to_head = distance_to_head[0]
    y_distance_to_head = distance_to_head[1]

    # When the tail is not touching the head, move the tail towards the head.
    if abs(x_distance_to_head) > 1 or abs(
            y_distance_to_head) > 1:
        print("We need to move!")

        #  This line is nothing more than "for the tail, set its X,Y coords depending on the (direction of the) distance between T and H for that value"
        tail_pos[:] = [coordinate + (1 if distance_to_head >= 1 else -1 if distance_to_head <= -1 else 0) for
                       coordinate, distance_to_head in zip(tail_pos, distance_to_head)]

        print("New T position: ", tail_pos)

    else:
        print("Don't have to move.")


# --------------------------------------------- PART 1 --------------------------------------------
distance_to_head = [0, 0]
head_pos = [0, 0]
tail_pos = [0, 0]

for direction, steps in commands:
    for step in range(steps):
        #  Determine the new position for H
        print("Position of H before moving is: ", head_pos)

        #  Moving H depending on the direction
        head_pos[0] = head_pos[0] + get_direction(direction)[0]
        head_pos[1] = head_pos[1] + get_direction(direction)[1]
        print("Position of H after moving is: ", head_pos)
        print("Position of T is: ", tail_pos)

        #  Moving T depending on the (direction of) the distance to H
        move(head_pos, tail_pos)
        print("T has now visited/is now on", tuple(tail_pos))

        part1.add(tuple(tail_pos))

        print("------------------------------------")

# # -------------------------------- PART 2 --------------------------------------

distance_to_head = [0, 0]
head_pos = [0, 0]
tail_pos = [0, 0]
knots = []

for knot in range(9):
    knots.append([0, 0])
    knot = knot + 1

for direction, steps in commands:
    for step in range(steps):

        #  Determine the new position for H
        print("Position of H before moving is: ", head_pos)

        #  Moving H depending on the direction
        head_pos[0] = head_pos[0] + get_direction(direction)[0]
        head_pos[1] = head_pos[1] + get_direction(direction)[1]
        print("Position of H after moving is: ", head_pos)
        print("Position of T is: ", tail_pos)

        #  Moving T depending on the (direction of) the distance to H
        move(head_pos, tail_pos)
        print("T has now visited/is now on", tuple(tail_pos))

        for knot in range(len(knots)):
            #  When we are at the first knot, just follow the head (in other words, "knots[knot]" is identical to "tail_pos", similar to part 1)
            if knot == 0:
                move(head_pos, knots[knot])

            #  If we arrive here, we are not at the first knot, so we need to follow the knot in front
            else:
                move(knots[knot - 1], knots[knot])

            #  When we arrive at the ninth knot (i.e. the last one)
            if knot == 8:
                part2.add(tuple(knots[knot]))

# ------------------------------- ANSWER -----------------------------------------
print("Amount of tiles the tail visited in part 1: ", len(part1))
print("Amount of tiles the tail visited in part 2: ", len(part2))
