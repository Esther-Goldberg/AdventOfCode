infile = open("inputs/sonar_sweep_input.txt")
input = list(map(int, infile.readlines()))

prev_item = input[0]
increases = 0

for item in input:
    if item > prev_item:
        increases += 1
    prev_item = item


print(increases)
