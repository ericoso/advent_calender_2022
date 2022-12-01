input_file = open("advent1.txt", "r")
lines = input_file.readlines()

top3 = []
count = 0

for line in lines:
    if line != '\n':
        count = count + int(line)
    else:
        if len(top3) < 3:
            top3.append(count)
            top3.sort(reverse=True)
        else:
            for i in range(len(top3)):
                if count > top3[i]:
                    if i == 0:
                        top3[i+2] = top3[i+1]
                        top3[i+1] = top3[i]
                    elif i == 1:
                        top3[i + 1] = top3[i]
                    top3[i] = count
                    top3.sort(reverse=True)
                    break
        count = 0
print("Total calories of the top 3 elves: " + str(sum(top3)))
