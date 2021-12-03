from collections import Counter


def read_bits(lines):
    return [line.strip() for line in lines]


def find_most_common_bit_at_index(bit_readings, index, tie_breaker='1'):
    bits_at_index = [bit[index] for bit in bit_readings]
    counts = Counter(bits_at_index)
    if counts['0'] == counts['1']:
        return tie_breaker
    else:
        return counts.most_common(1)[0][0]


data_path = '../input/day3.txt'
with open(data_path) as f:
    lines = f.readlines()

# Part 1
list_of_bits = read_bits(lines)
gamma_rate_bits = []
for i in range(len(list_of_bits[0])):
    gamma_rate_bits.append(find_most_common_bit_at_index(list_of_bits, i))
gamma_rate = int(''.join(gamma_rate_bits), 2)
# flipping bit values in binary representation
epsilon_rate = (pow(2, len(gamma_rate_bits)) - 1) - gamma_rate
print(f'3-1: {gamma_rate * epsilon_rate}')

# Part 2


def flip_bit(bit):
    if bit == '0':
        return '1'
    else:
        return '0'


def read_rating(bit_readings, type):
    for i in range(len(bit_readings)):
        common_bit = find_most_common_bit_at_index(bit_readings, i)
        if type == 'co':
            common_bit = flip_bit(common_bit)
        bit_readings = [bits for bits in bit_readings if bits[i] == common_bit]
        if len(bit_readings) == 1:
            return int(bit_readings[0], 2)


bit_readings = read_bits(lines)
oxygen_rating = read_rating(bit_readings, type='oxygen')
co_rating = read_rating(bit_readings, type='co')
print(f'3-2: {oxygen_rating * co_rating}')
