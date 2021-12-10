with open('input.txt') as f:
    data = f.readlines()


opening = ['(', '{', '<', '[']
closing = [')', '}', '>', ']']
scoring = {')': 1, ']': 2, '}': 3, '>': 4}

s = []
incomplete = []
for l in data:
    stack = []
    for c in l.strip():
        if c in opening:
            stack.append(c)
        else:
            p = stack.pop()
            if c != closing[opening.index(p)]:
                break
    else:
        sc = 0
        while stack:
            p = closing[opening.index(stack.pop())]
            sc = 5 * sc + scoring[p]
        s.append(sc)
s.sort()
print(s[len(s) // 2])
