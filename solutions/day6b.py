import functools

with open('input.txt') as f:
    data = list(map(int, f.read().split(',')))
feeesh = data


@functools.lru_cache(maxsize=None)
def fish_numbers(n):
    if n < 1:
        return 1
    return fish_numbers(n - 7) + fish_numbers(n-9)


days = 256
total_fish = 0
for fish_counter in feeesh:
    total_fish += fish_numbers(days - fish_counter)
print(total_fish)
