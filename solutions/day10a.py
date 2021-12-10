with open('input.txt') as f:
    data = f.readlines()


opening = ['(', '{', '<', '[']
closing = [')', '}', '>', ']']
scoring = {')': 3, ']': 57, '}': 1197, '>': 25137}

s = 0
for l in data:
    stack = []
    for c in l.strip():
        if c in opening:
            stack.append(c)
        else:
            p = stack.pop()
            if c != closing[opening.index(p)]:
                s += scoring[c]
                break
print(s)
