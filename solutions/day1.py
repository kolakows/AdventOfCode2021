from utils.data import read_data

data_path = '../input/day1.txt'
sea_depths = read_data(data_path, int)


def depth_increase_count(depths):
    return sum(next_depth - depth > 0 for depth, next_depth in zip(depths, depths[1:]))


def sliding_window_sums(depths, window_size):
    return [sum(depths[i:i+window_size]) for i in range(len(depths) - window_size + 1)]


# part 1
print(depth_increase_count(sea_depths))

# part 2
sliding_depths = sliding_window_sums(sea_depths, 3)
print(depth_increase_count(sliding_depths))
