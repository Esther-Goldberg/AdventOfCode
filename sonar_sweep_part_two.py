infile = open("inputs/sonar_sweep_input.txt")
input = list(map(int, infile.readlines()))

first_two_lists = zip(input[:len(input) - 2], input[1:len(input) - 1])
summed_first_two_lists = [x + y for (x, y) in first_two_lists]

all_three_lists = zip(summed_first_two_lists, input[2:])
summed_all_lists = [x + y for (x, y) in all_three_lists]


prev_item = summed_all_lists[0]
increases = 0

for item in summed_all_lists:
    if item > prev_item:
        increases += 1
    prev_item = item


print(increases)
