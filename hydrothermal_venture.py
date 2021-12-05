infile = open("inputs/hydrothermal_venture_input.txt")

ocean_floor = [[0]*1000 for x in range(1000)]

lines = infile.readlines()
lines = [x.split('->') for x in lines]

lines = [[x.strip().split(",") for x in line] for line in lines]

lines = [[[int(x) for x in pair] for pair in line] for line in lines]

for line in lines:
    xrange = range(line[0][0], line[1][0], 1 if line[0]
                   [0] < line[1][0] else -1)
    yrange = range(line[0][1], line[1][1], 1 if line[0]
                   [1] < line[1][1] else -1)

    if line[0][1] == line[1][1]:
        for x in xrange:
            ocean_floor[x][line[0][1]] += 1
        ocean_floor[line[1][0]][line[0][1]] += 1
    elif line[0][0] == line[1][0]:
        for y in yrange:
            ocean_floor[line[0][0]][y] += 1
        ocean_floor[line[0][0]][line[1][1]] += 1
    else:       # only for part two
        for (x, y) in zip(xrange, yrange):
            ocean_floor[x][y] += 1
        ocean_floor[line[1][0]][line[1][1]] += 1

total = 0

for row in ocean_floor:
    for column in row:
        if column >= 2:
            total += 1

print(total)
