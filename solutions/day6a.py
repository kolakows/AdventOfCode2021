from dataclasses import dataclass

with open('input.txt') as f:
    data = list(map(int, f.read().split(',')))
feeesh = data
fish_colony = []


@dataclass
class Fish:
    counter: int = 8

    def reset(self):
        self.counter = 6


for fish_counter in feeesh:
    fish_colony.append(Fish(fish_counter))
days = 80
for day in range(days):
    new_fish = []
    for fish in fish_colony:
        if fish.counter == 0:
            fish.reset()
            new_fish.append(Fish())
        else:
            fish.counter -= 1
    fish_colony.extend(new_fish)
print(len(fish_colony))

