with open("day3input.txt") as f:
    lines = f.readlines()

sLines = []
for line in lines:
    sLine = line.strip("\n")
    sLines.append(sLine)


matches = []
for sLine in sLines:
    HalveRucksack = int(len(sLine) / 2)
    FirstCompartment = sLine[:HalveRucksack]
    SecondCompartment = sLine[HalveRucksack:]

    for letter in FirstCompartment:
        if letter in SecondCompartment:
            match = letter
    matches.append(match)


sum = 0
for i in matches:
    if i.islower():
        sum += ord(i) - 96 #the ord function get the unicode of a character which for lower case is 96 higher than desired e.g. ord("a") = 97
    elif i.isupper():
        sum += ord(i) - 64 + 26 #the ord for upper case is 64 higher e.g. ord("A") = 65 and we define "A" at 27 so add 26 back

print(sum)

BadgeCount = []
test = ["vJrwpWtwJgWrhcsFMMfFFhFp","jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL","PmmdzqPrVvPwwTWBwg","wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn","ttgJtRGJQctTZtZT","CrZsJsPPZsGzwwsLwLmpwMDw"]
for index in range(0,len(sLines),3):

    for letter in sLines[index]:
        count = 0
        for i in range(3):
            if letter in sLines[index+i]:
                print(letter)
                count += 1
        if count == 3:
            BadgeCount.append(letter)
            break


sum = 0
for i in BadgeCount:
    if i.islower():
        sum += ord(i) - 96 #the ord function get the unicode of a character which for lower case is 96 higher than desired e.g. ord("a") = 97
    elif i.isupper():
        sum += ord(i) - 64 + 26 #the ord for upper case is 64 higher e.g. ord("A") = 65 and we define "A" at 27 so add 26 back

print(sum)


print(BadgeCount)

