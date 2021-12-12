with open('input.txt') as f:
    data = f.read()
edges = [line.split('-') for line in data.split('\n')]

paths = []
visited = []

def dfs(v, path):
    path.append(v)
    adj = [e for e in edges if v in e]
    nbs = [e[0] if e[1] == v else e[1] for e in adj]
    for nb in nbs:
        if nb not in path or nb.isupper():
            if nb == 'end':
                paths.append(path)
            else:
                dfs(nb, path)
                path.pop()

dfs('start', [])
print(len(paths))