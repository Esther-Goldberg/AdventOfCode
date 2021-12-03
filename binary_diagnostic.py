infile = open("inputs/binary_diagnostic.txt")
input = infile.readlines()
input = [item.strip() for item in input]


number_of_zeros = [0]*len(input[0])
number_of_ones = [0]*len(input[0])

for item in input:
    for index, char in enumerate(item):
        if char == '0':
            number_of_zeros[index] += 1
        else:
            number_of_ones[index] += 1

gamma_rate = []
epsilon_rate = []

for i in range(len(input[0])):
    if number_of_zeros[i] > number_of_ones[i]:
        gamma_rate.append('0')
        epsilon_rate.append('1')
    else:
        gamma_rate.append('1')
        epsilon_rate.append('0')

print(int(''.join(gamma_rate), 2) * int(''.join(epsilon_rate), 2))
