with open('input.txt') as f:
    data = f.read()
positions = list(map(int, data.split(',')))
cost = []
for i in range(max(positions) + 1):
    def single_cost(x):
        n = abs(x - i)
        return (n * (n+1))/2
    c = list(map(lambda x: single_cost(x), positions))
    cost.append(sum(c))
best_pos = min(range(len(cost)), key=cost.__getitem__)
print(cost[best_pos])
