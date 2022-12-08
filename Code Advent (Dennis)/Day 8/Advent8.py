input_file = open("Advent8.txt", "r")
lines = input_file.readlines()

forest = []
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def main():
    i = 0
    j = 0
    max_x = 0
    max_y = 0
    visible_from_outside = 0
    max_score = 0

    #  First create a list of lists depicting the entire forest
    for line in lines:
        line = line.replace("\n", "")
        forest.append([])
        for tree in line:
            forest[i].append(tree)
            j = j + 1
        i = i + 1
    height, width = len(forest), len(forest[0])

    #  For every tree in every row (height) and column (width), determine whether it is visible AND it's scenic score
    for y in range(0, height):
        for x in range(0, width):
            #  N.B. I first had the entire code of "determine_whether_visible" in here, but it was a complete mess.
            #  Then I remembered that functions exist lol
            score, visible = determine_whether_visible(forest, x, y)

            # Determine whether this tree has the highest scenic score and save its score and its coordinates (row and column)
            if score > max_score:
                max_score = score
                max_x = x
                max_y = y

            # Determine whether this tree is visible from any of the sides
            if visible:
                visible_from_outside += 1

    return visible_from_outside, max_score, max_x, max_y


#  Note to self: this function determines both the visibility from the outside as well as the scenic score PER TREE.
def determine_whether_visible(forest, x, y):
    tree_height = forest[y][x]
    height = len(forest)
    width = len(forest[0])
    coordinates = (x, y)
    visible_from_outside = False  # Innocent until proven guilty lol
    scenic_score = 1

    #  Do the same loop four times for every direction
    #  N.B. I first had four different loops, this is way more compact and efficient (yes I stole this from internet)
    for x_direction, y_direction in directions:
        x, y = coordinates
        visible = 0

        #  While we are not at the edge yet
        while 0 < x < width - 1 and 0 < y < height - 1:

            #  Add a visibility score to determine the scenic score for this tree in this direction, since we can see this tree
            visible += 1

            #  When we find a tree that is either as large or larger, stop going in this direction
            if forest[y + y_direction][x + x_direction] >= tree_height:
                break  # Note to self: this break breaks the while loop of line 62, thus also not changing "visible_from_outside" to True in the if-statement of line 76

            #  Go to the next step in the direction (i.e. next tree in the row/column)
            x += x_direction
            y += y_direction

        #  Hooray! We did not find any trees that are as large or larger (i.e. we reached the edge).
        if x <= 0 or x >= width - 1 or y <= 0 or y >= height - 1:
            visible_from_outside = True

        #  Multiply the scenic score of this tree with the scenic score of the above direction
        scenic_score *= visible

    return scenic_score, visible_from_outside


part1, part2, x_max, y_max = main()
print("The amount of trees visible from the outside is " + str(part1))
print("The highest possible scenic score is " + str(part2) + " which is found at the tree in the " + str(
    y_max) + "th row and the " + str(x_max) + "th column")
