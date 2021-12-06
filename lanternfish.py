infile = open("inputs/lanternfish_input.txt")

fish = infile.readline().split(",")
fish = [int(x) for x in fish]

fish_by_age = [0]*9

for item in fish:
    fish_by_age[item] += 1

for day in range(256):
    new_fish = fish_by_age.pop(0)
    fish_by_age.append(new_fish)
    fish_by_age[6] += new_fish

print(sum(fish_by_age))
