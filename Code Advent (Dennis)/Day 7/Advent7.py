input_file = open("advent7.txt", "r")
lines = input_file.readlines()
size_part_1 = 0
size_part_2 = 70000000
current_directory = []
paths = {}


#  ------------------------------ CREATING THE LIST OF DIRS WITH THEIR SIZE------------------------------------------


for line in lines:
    line = line.replace("\n", "")
    #  Find all the lines in which we change directory
    if line.startswith("$ cd"):
        #  Replace the entire line to be just the directory we are moving to (easier to work with)
        dir_line = line.replace("$ cd ", "")
        #  Find the lines in which we go to an existing directory (i.e. with a letter or the main directory)
        if dir_line != "..":
            #  Append the directory letter to the current directory list
            current_directory.append(dir_line)
        else:
            #  If we go up a directory, remove the lastly added directory (i.e. "go up a depth level")
            current_directory.pop()
        #  Create a path to the directory we just found in the if-statement (to determine depth levels later)
        paths.setdefault('/'.join(current_directory).replace("//", "/"), 0)

        #  Find the lines in which we print the current structure of the directory (to ignore to make the catch-all else statement work lol)
    elif line.startswith("$ ls"):
        pass

    #  For every line that is not a command (i.e. a directory/file)
    else:
        #  Find every line in which a file is shown (i.e. with a size)
        if line.split(" ")[0] != "dir":
            #  Add the size of the directory to its corresponding dir in the directory dictionary
            paths['/'.join(current_directory).replace("//", "/")] += int(line.split(" ")[0])


#  ------------------------------------------------ PART 1 --------------------------------------------------------


#  For all directories
for directory in paths:
    #  Nested for loop to find duplicates
    for directory2 in paths:
        #  If the pair is no duplicate and directory 2 is in directory 1
        if directory != directory2 and directory2.startswith(directory):
            #  Add the size of the nested directory to the one of the main directory (i.e. add size of 2 to 1)
            paths[directory] += paths[directory2]
    #  Find all directories that are smaller than 100.000
    if paths[directory] <= 100000:
        size_part_1 += paths[directory]


#  ------------------------------------------------ PART 2 --------------------------------------------------------


#  Determine the required space (i.e. subtract the size of the entire filesystem of the 70.000.000 and subtract that from the 30.000.000 necessary file size)
space_required = 30000000 - (70000000 - paths["/"])

#  For each directory
for directory in paths:
    #  If the directory is larger than the space we require (i.e. removing it would free up enough space)
    if paths[directory] > space_required:
        #  Compare it with the current smallest directory and pass the smallest of the two
        size_part_2 = min(size_part_2, paths[directory])


#  ------------------------------------------------ ANSWERS --------------------------------------------------------


print("The sum of the sizes of all directories with a size smaller than 100.000 is: " + str(size_part_1))
print("The size of the smallest directory that can be deleted to free up enough space is: " + str(size_part_2))
