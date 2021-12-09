ans = 0

with open("input.txt", "r") as f:
    for present in f:
        dims = [int(i) for i in present.strip().split("x")]
        dims.sort()
        ans += 3 * dims[0] * dims[1]
        ans += 2 * dims[1] * dims[2]
        ans += 2 * dims[0] * dims[2]

print("Part 1: {}".format(ans))
