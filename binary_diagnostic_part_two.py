infile = open("inputs/binary_diagnostic.txt")
input = infile.readlines()
input = [item.strip() for item in input]


def most_common(zeros_and_ones):
    if zeros_and_ones[0] == zeros_and_ones[1]:
        return 1
    elif zeros_and_ones[0] > zeros_and_ones[1]:
        return 0
    else:
        return 1


oxygen_gen_rating = input
co2_scrubber_rating = input

final_oxygen = 0
final_co2 = 0

for i in range(len(input[0])):
    zeros_and_ones = [0]*2

    for item in oxygen_gen_rating:
        if item[i] == '0':
            zeros_and_ones[0] += 1
        else:
            zeros_and_ones[1] += 1

    oxygen_gen_rating = [
        x for x in oxygen_gen_rating if int(x[i]) == most_common(zeros_and_ones)]

    if len(oxygen_gen_rating) == 1:
        final_oxygen = int(''.join(oxygen_gen_rating[0]), 2)
        break

for i in range(len(input[0])):
    zeros_and_ones = [0]*2

    for item in co2_scrubber_rating:
        if item[i] == '0':
            zeros_and_ones[0] += 1
        else:
            zeros_and_ones[1] += 1

    co2_scrubber_rating = [
        x for x in co2_scrubber_rating if not (int(x[i]) == most_common(zeros_and_ones))]

    if len(co2_scrubber_rating) == 1:
        final_co2 = int(''.join(co2_scrubber_rating[0]), 2)
        break


print(final_oxygen * final_co2)
