infile = open("inputs/dive_input.txt")
input = infile.readlines()

input = [[x.split()[0], int(x.split()[1])] for x in input]

horizontal_pos = 0
depth = 0
aim = 0

for command, value in input:
    if command == "down":
        aim += value
    elif command == "up":
        aim -= value
    else:
        horizontal_pos += value
        depth += value * aim


print(horizontal_pos * depth)
