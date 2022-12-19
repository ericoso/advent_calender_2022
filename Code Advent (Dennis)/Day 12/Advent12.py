data = []
# First create a list of lists depicting the elevation fields and determine where the start/end is. (also replace their "values" with a and z respectively)
with open("advent12.txt") as file:
    for row, line in enumerate(file):
        data.append([])
        for row2, char in enumerate(line.strip()):
            data[row].append(char)
            if char == "S":
                start_pos = (row, row2)
                data[start_pos[0]][start_pos[1]] = "a"
            elif char == "E":
                end_pos = (row, row2)
                data[end_pos[0]][end_pos[1]] = "z"


def bfs(data, start, end, part2):
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    rows = len(data)
    columns = len(data[0])

    visited = []

    queue = [start]

    v = [[0 for i in range(columns)] for _ in range(rows)]

    while len(queue) > 0:
        p = queue[0]
        queue.pop(0)

        if part2 and data[p[0]][p[1]] == "a":
            return v[p[0]][p[1]]
        elif not part2 and p == end:
            return v[end[0]][end[1]]

        for i in range(4):
            a = p[0] + dirs[i][0]
            b = p[1] + dirs[i][1]

            if (0 <= a < rows and 0 <= b < columns and (
                    ord(data[a][b]) >= ord((data[p[0]][p[1]])) or ord(data[a][b]) + 1 == ord((data[p[0]][p[1]]))) and (
                    a, b) not in visited):
                queue.append((a, b))
                visited.append((a, b))
                v[a][b] = v[p[0]][p[1]] + 1

    return None


print("Part 1:", bfs(data, end_pos, start_pos, False))
print("Part 2:", bfs(data, end_pos, start_pos, True))
