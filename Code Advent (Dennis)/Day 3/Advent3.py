input_file = open("Advent3.txt", "r")
lines = input_file.readlines()
prio = 0
priority = 0
elf = 1
group = False

# -------------------------------- PART 1 ------------------------------------

for line in lines:
    line = line.replace("\n", "")
    halfway = int(len(line)/2)
    first_half = "".join(set(line[:halfway]))
    second_half = "".join(set(line[halfway:]))
    for item in first_half:
        if item in second_half:
            if item.islower():
                prio += (ord(item) - 96)
            else:
                prio += (ord(item) - 64 + 26)

print("Priority of the first part: " + str(prio))

# ----------------------------------- PART 2 ----------------------------------------

for line in lines:
    line = line.replace("\n", "")
    if elf == 1:
        elf1 = line
        elf = 2
    elif elf == 2:
        elf2 = line
        elf = 3
    elif elf == 3:
        elf3 = line
        elf = 1
        group = True
    if group:
        for letter in elf1:
            if letter in elf2:
                if letter in elf3:
                    if letter.islower():
                            priority += (ord(letter) - 96)
                    else:
                            priority += (ord(letter) - 64 + 26)
                    elf1 = ""
                    elf2 = ""
                    elf3 = ""
                    break
print("Priority of the second part: " + str(priority))



