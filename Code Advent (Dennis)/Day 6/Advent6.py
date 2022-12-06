input_file = open("advent6.txt", "r")
input_stream = input_file.readlines()[0]
potential_marker = []
i = 0

for symbol in input_stream:
    i += 1
    potential_marker.append(symbol)
    print("Current marker: " + str(potential_marker))
    if len(potential_marker) == 14:
        marker_no_duplicates = list(dict.fromkeys(potential_marker))
        print("Marker without duplicates (if this is 4, we found it!" + str(marker_no_duplicates))
        if len(marker_no_duplicates) == 14:
            print("Found marker! Position: " + str(i))
            break
        potential_marker.pop(0)
