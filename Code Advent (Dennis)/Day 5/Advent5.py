input_file = open("advent5.txt", "r")
lines = input_file.readlines()
stack_dict = {}
instructions = []
stacks = []
top_crates = []

# YES, this could have been done in one for loop. I was just lazy to go with try-excepts or whatever, whoops.

# In order to run either part 1 or 2, just comment the entire thing. Again, too lazy to refactor correctly..

for line in lines:
    # Determine the amount of stacks (spoilers: 3 in test, 9 in puzzle input)
    if " 1   2 " in line:
        line = line.replace(" ", "")
        line = line.replace("\n", "")
        for number in line:
            stacks.append(number)

# Create a dictionary of lists for the crate orders per stack
stack_dict = {i: [] for i in stacks}

for line in lines:
    column = 0
    # Determine the starting orientation of all the crates and append to their corresponding list in the dict
    if "[" in line:
        for i in range(0, len(line), 4):
            column = column + 1
            if (line[i] == "[") and (line[i + 2] == "]"):
                # print("Found a crate in column " + str(column) + "!" + " Crate: " + str(line[i + 1]))
                stack_dict[str(column)].append(line[int(i + 1)])

print("Order of crates: " + str(stack_dict))

# ------------------------------------------------ PART 1 --------------------------------------------------------------

# for line in lines:
#     if line.startswith("move"):
#         sentence = line.split(" ")
#         # print(sentence)
#         amount = sentence[1]
#         from_stack = sentence[3]
#         to_stack = sentence[5].replace("\n", "")
#         # print("I want to move " + str(amount) + " crate(s) to stack number " + str(to_stack) + " from stack number " + str(from_stack))
#         for times in range(0, int(amount), 1):
#             crate_to_move = stack_dict[from_stack][0]
#             print("Moving crate "+ str(crate_to_move) + " from stack " + str(from_stack) + " to stack number " + str(to_stack))
#             stack_dict[from_stack].pop(0)
#             stack_dict[to_stack].insert(0,crate_to_move)
#             print("Order of crates: " + str(stack_dict))
#
# for stack in range(1, len(stacks)+1, 1):
#     top_crate = stack_dict[str(stack)][0]
#     top_crates.append(top_crate)
#
#
# print("The top crates with the CrateMover9000 are: " + str("".join(top_crates)))


# ------------------------------------------------ PART 2 --------------------------------------------------------------
moving_crates = []
for line in lines:
    if line.startswith("move"):
        sentence = line.split(" ")
        # print(sentence)
        amount = sentence[1]
        from_stack = sentence[3]
        to_stack = sentence[5].replace("\n", "")
        print("I want to move " + str(amount) + " crate(s) to stack number " + str(to_stack) + " from stack number " + str(from_stack))
        for times in range(0, int(amount), 1):
            crate_to_move = stack_dict[from_stack][0]
            moving_crates.append(crate_to_move)
            stack_dict[from_stack].pop(0)

        print("The crates to move are: " + str(moving_crates))
        stack_dict[to_stack][0:0] = moving_crates
        print("New order of crates: " + str(stack_dict))
        moving_crates = []
            # print("Moving crate "+ str(crate_to_move) + " from stack " + str(from_stack) + " to stack number " + str(to_stack))
            # stack_dict[to_stack].insert(0, crate_to_move)
            # print("Order of crates: " + str(stack_dict))

for stack in range(1, len(stacks)+1, 1):
    top_crate = stack_dict[str(stack)][0]
    top_crates.append(top_crate)


print("The top crates with the CrateMover9001 are: " + str("".join(top_crates)))

