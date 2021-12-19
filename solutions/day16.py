from functools import reduce
import numpy as np

with open('input.txt') as f:
    data = f.read()
bdata = bin(int(data, 16))[2:].zfill(len(data) * 4)
bits = bdata


def sum_(x):
    if type(x) == int:
        return x
    else:
        return np.sum(x)


def reduce_op(op, args):
    return reduce(lambda x, y: op(x, y), args)

operation = {
    0: sum_,
    1: lambda x: reduce_op(lambda a, b: a * b, x),
    2: lambda x: min(x) if len(x) > 1 else x,
    3: lambda x: max(x) if len(x) > 1 else x,
    5: lambda x: 1 if x[0] > x[1] else 0,
    6: lambda x: 1 if x[0] < x[1] else 0,
    7: lambda x: 1 if x[0] == x[1] else 0
}


def parse_packet(bits, offset):
    version = bits[offset:offset+3]
    version = int(''.join(version), 2)
    offset += 3
    packet_type = bits[offset:offset+3]
    packet_type = int(''.join(packet_type), 2)
    offset += 3
    if packet_type == 4:
        number = []
        while bits[offset] == '1':
            offset += 1
            number += bits[offset:offset+4]
            offset += 4
        offset += 1
        number += bits[offset:offset+4]
        offset += 4
        value = int(''.join(number), 2)
    else:
        length_type = bits[offset]
        offset += 1
        if length_type == '0':
            subpacket_length = int(''.join(bits[offset:offset+15]), 2)
            offset += 15
            subbits = bits[offset:offset+subpacket_length]
            offset += subpacket_length
            off = 0
            vals = []
            while off < len(subbits):
                v, off, val = parse_packet(subbits, off)
                version += v
                vals.append(val)
            value = operation[packet_type](vals)
        else:
            subpacket_count = int(''.join(bits[offset:offset+11]), 2)
            offset += 11
            vals = []
            for i in range(subpacket_count):
                v, off, val = parse_packet(bits, offset)
                version += v
                offset = off
                vals.append(val)
            value = operation[packet_type](vals)
    # skip unused bits to match hex notation of packets
    # to_skip = (4 - offset % 4) % 4
    # offset += to_skip
    return version, offset, value

print(parse_packet(bits, 0))

