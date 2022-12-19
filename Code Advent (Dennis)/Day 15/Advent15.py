input_file = open("Advent15.txt").read()
input_file = input_file.strip()
sensors = set()
beacons = set()

for input in input_file.split("\n"):
    row = input.split()
    sensor_x, sensor_y = int(row[2][2:-1]), int(row[3][2:-1])
    beacon_x, beacon_y = int(row[8][2:-1]), int(row[9][2:])
    distance_to_closest_beacon = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    sensors.add((sensor_x, sensor_y, distance_to_closest_beacon))
    beacons.add((beacon_x, beacon_y))


# Check for an x,y coordinate whether it is possible that there is a beacon there based on all others sensors
def possible_beacon(x, y):
    for sensor_x, sensor_y, distance_to_closest_beacon in sensors:
        if abs(x - sensor_x) + abs(y - sensor_y) <= distance_to_closest_beacon and (x, y) not in beacons:
            return False
    return True


def part_1():
    i = 1
    percent = 25
    counter = 0
    y = 2000000
    min_x = min(x - d for x, _, d in sensors)
    max_x = max(x + d for x, _, d in sensors)
    for x in range(min_x, max_x):
        if x % 1800794 == 0:
            print(25 * i, "% done!")
            i += 1
        if not possible_beacon(x, y) and (x, y) not in beacons:
            counter += 1
    return counter


def part_2():
    for sensor_x, sensor_y, distance_to_closest_beacon in sensors:
        for delta_x in range(distance_to_closest_beacon + 2):
            delta_y = (distance_to_closest_beacon + 1) - delta_x
            for x_direction, y_direction in [(1, 1), (-1, -1), (-1, 1), (1, -1)]:
                x, y = sensor_x + (delta_x * x_direction), sensor_y + (delta_y * y_direction)
                if not (0 <= x <= 4000000 and 0 <= y <= 4000000):
                    continue
                if possible_beacon(x, y):
                    return (x * 4000000) + y


print("Number of spots where a beacon cannot be placed:", part_1())
print("Tuning frequency of the distress signal:", part_2())
