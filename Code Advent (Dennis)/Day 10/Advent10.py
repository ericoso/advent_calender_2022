register = 1
cycle = 0
signal_strength_per_cycle = {}
part1 = 0
crt_board = []

#  Create the empty CRT board
for i in range(240):
    crt_board.append(".")

input_file = open("Advent10.txt", "r")
lines = input_file.readlines()


#  Function for drawing the # symbol when needed
def draw(register, cycles, crt_board):
    current_position = (cycles - 1) % 40  # Modulo 40 to account for the different rows
    if current_position in {register - 1, register, register + 1}:
        crt_board[cycles] = "#"


for line in lines:
    line.rstrip()
    line = line.split()
    command = line[0]
    match command:
        case "noop":
            cycle += 1
            signal_strength_per_cycle[cycle] = register * cycle
            draw(register, cycle, crt_board)

        case "addx":
            cycle += 1
            signal_strength_per_cycle[cycle] = register * cycle
            draw(register, cycle, crt_board)

            #  Since addx takes two cycles, do two cycles of functions
            cycle += 1
            signal_strength_per_cycle[cycle] = register * cycle
            draw(register, cycle, crt_board)
            register += int(line[1])

for i in range(20, 260, 40):
    part1 = part1 + signal_strength_per_cycle.get(i, 0)

print("Signal strength in part 1:", part1)

print("--------------------------------------------")

for i in range(0, 240, 40):
    print("".join(crt_board[i: i + 40]))

print("--------------------------------------------")
