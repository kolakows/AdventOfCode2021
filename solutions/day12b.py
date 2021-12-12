with open('input.txt') as f:
    data = f.read()
edges = [line.split('-') for line in data.split('\n')]

paths = []
visited = []

def dfs(v, path, dup):
    path.append(v)
    adj = [e for e in edges if v in e]
    nbs = [e[0] if e[1] == v else e[1] for e in adj]
    for nb in nbs:
        if nb not in path or nb.isupper():
            if nb == 'end':
                paths.append(path.copy())
            else:
                dfs(nb, path, dup)
                path.pop()
        if not dup and nb.islower() and nb in path and nb not in ['start', 'end']:
            dfs(nb, path, True)
            path.pop()


dfs('start', [], False)
print(len(paths))