input_file = open("Advent4.txt", "r")
lines = input_file.readlines()
pairs = 0
overlap = 0

for line in lines:
    ranges = line.split(",")
    print(ranges)
    first_range = ranges[0].split("-")
    second_range = ranges[1].split("-")
    first_range_begin = int(first_range[0])
    first_range_end = int(first_range[1])
    second_range_begin = int(second_range[0])
    second_range_end = int(second_range[1].replace("\n", ""))
    print(first_range_begin, first_range_end, second_range_begin, second_range_end)

    if (first_range_begin >= second_range_begin) & (first_range_end <= second_range_end):
        print("Found one! First range in second range!")
        pairs = pairs + 1
    elif (second_range_begin >= first_range_begin) & (second_range_end <= first_range_end):
        print("Found one! Second range in first range!")
        pairs = pairs + 1
    else:
        print("Not in each others ranges!")

    if ((first_range_begin or first_range_end) >= second_range_begin) and ((first_range_begin or first_range_end) <= second_range_end):
        overlap = overlap + 1
        print("Found one! First range overlaps with second!")
    elif ((second_range_begin or second_range_end) >= first_range_begin) and ((second_range_begin or second_range_end) <= first_range_end):
        overlap = overlap + 1
        print("Found one! Second range overlaps with first!")
    else:
        print("No overlaps!")

print("Number of pairs is: " + str(pairs))
print("Number of overlaps is: " + str(overlap))
