with open('input.txt') as f:
    data = f.readlines()
entries = [reading.split(' | ') for reading in data]
c = 0
for entry in entries:
    digit_output = entry[1].split()
    for d in digit_output:
        if len(d) in [2, 3, 4, 7]:
            c += 1
print(c)