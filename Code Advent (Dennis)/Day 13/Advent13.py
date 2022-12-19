# I mostly stole this from the internet, whoops lol.


def compare(left, right):
    for item_left, item_right in zip(left, right):
        if isinstance(item_left, int) and isinstance(item_right, int):
            if item_left < item_right:
                return 1
            if item_left > item_right:
                return -1
        elif isinstance(item_left, list) and isinstance(item_right, list):
            result = compare(item_left, item_right)
            if result != 0:
                return result
        elif isinstance(item_left, int):  # Left item is an int; right item is a list
            result = compare([item_left], item_right)
            if result != 0:
                return result
        else:  # Left item is a list; right item is an int
            result = compare(item_left, [item_right])
            if result != 0:
                return result

    # if we reached this point, no differences were found.
    if len(left) < len(right):  # Left side is empty first (which is good!)
        return 1
    elif len(left) > len(right):  # Right side is empty first (which is bad..)
        return -1

    return 0


lines = {
    count: (eval(p[0]), eval(p[1]))
    for count, p in enumerate([p.splitlines() for p in open("advent13.txt").read().split("\n\n")], 1)
}


# Part One

print(sum(key for key, value in lines.items() if compare(value[0], value[1]) == 1))

# Part Two

all_packets = [u for v in list(lines.values()) for u in v] + [[[2]], [[6]]]
print((1 + sum(1 for p in all_packets if compare(p, [[2]]) == 1)) * (
        1 + sum(1 for p in all_packets if compare(p, [[6]]) == 1)))
