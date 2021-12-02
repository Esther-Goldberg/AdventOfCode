infile = open("inputs/dive_input.txt")
input = infile.readlines()

input = [[x.split()[0], int(x.split()[1])] for x in input]

horizontal_pos = 0
depth = 0

for command, value in input:
    if command == "forward":
        horizontal_pos += value
    elif command == "down":
        depth += value
    else:
        depth -= value


print(horizontal_pos * depth)
