with open("day6Input.txt") as f:
    lines = f.readlines()

sLines = lines[0]

# sLines = "bvwbjplbgvbhsrlpgdmjqwftvncz"

buffer = []
count = 0
for letter in sLines:
    if letter in buffer:
        lol = buffer.index(letter)
        for i in range(lol+1):
            buffer.pop(0)

    buffer.append(letter)
    print(buffer)
    count += 1
    print(count)
    # if len(buffer) == 4:
    #     print(count)
    #     break

    if len(buffer) == 14:
        print(count)
        break
