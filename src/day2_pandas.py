
import pandas as pd

data_path = '../input/day2.txt'
df = pd.read_csv(data_path, sep=' ', header=None, names=['direction', 'units'])
df['units'] = df['units'].astype(int)

# part 1

totals = df.groupby('direction').sum()
depth = totals['units']['down'] - totals['units']['up']
position = totals['units']['forward']
print(f'2-1 {position * depth} using pandas')

# part 2
# hmmm, no
