with open('input.txt') as f:
    data = f.readlines()
entries = [reading.split(' | ') for reading in data]

sum = 0
for entry in entries:
    patterns = entry[0].split()
    digit_output = entry[1].split()
    coding = {}
    for p in patterns:
        num = None
        if len(p) == 2:
            num = 1
        if len(p) == 3:
            num = 7
        if len(p) == 4:
            num = 4
        if len(p) == 7:
            num = 8
        if num:
            coding[num] = set(p)
    zero_six_nine = set(frozenset(p) for p in patterns if len(p) == 6)
    two_three_five = set(frozenset(p) for p in patterns if len(p) == 5)
    for p in zero_six_nine:
        if len(p & coding[1]) == 1:
            coding[6] = p
    zero_nine = zero_six_nine - set([coding[6]])
    for p in zero_nine:
        if len(p ^ (coding[7] | coding[4])) == 1:
            coding[9] = p
    coding[0] = next(iter(zero_nine - set([coding[9]])))
    coding[5] = frozenset(coding[8] - (coding[6] ^ coding[9]))
    two_three = two_three_five - set([coding[5]])
    for p in two_three:
        if len(p & coding[1]) == 2:
            coding[3] = p
    coding[2] = next(iter(two_three - set([coding[3]])))

    b_coding = {frozenset(v): str(k) for k, v in coding.items()}
    display = []
    for digit in digit_output:
        d = frozenset(digit)
        display.append(b_coding[d])
    sum += int(''.join(display))
print(sum)