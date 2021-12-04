from itertools import chain


with open('input.txt', 'r') as f:
    data = f.read()
data = data.split('\n\n')

whole_seq = data[0].split(',')

bbs = []
for board in data[1:]:
    rows, cols = [], []
    for line in board.splitlines():
        rows.append(set(line.split()))
    for line in zip(*rows):
        cols.append(set(line))
    bbs.append((rows, cols))


def is_win(board, s):
    rows, cols = board
    for line in chain(rows, cols):
        if line.issubset(s):
            return True
    return False


def check_win_last(boards, s, index):
    s.add(whole_seq[index])

    if len(boards) == 1 and is_win(boards[0], s):
        rows, _ = boards[0]
        all_nums = set(chain.from_iterable(rows))
        unmarked = all_nums - s
        return sum(list(map(int, unmarked))) * int(whole_seq[index])

    not_winning = []
    for board in boards:
        if is_win(board, s):
            pass
        else:
            not_winning.append(board)
    return check_win_last(not_winning, s, index+1)


print(check_win_last(bbs, set(), 0))
