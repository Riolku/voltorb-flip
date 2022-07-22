from collections import defaultdict


def group2(x):
    return [x[i * 2 : (i + 1) * 2] for i in range((len(x) + 1) // 2)]


row_restrictions = group2(list(map(int, input().split())))
col_restrictions = group2(list(map(int, input().split())))

grid = [[-1] * 5 for _ in range(5)]

possible_grids = []


def fill_recursive(r, c):
    global possible_grids
    if r == 4 and not all(
        restriction == [0, 0] for restriction in col_restrictions[:c]
    ):
        return

    if not all(restriction == [0, 0] for restriction in row_restrictions[:r]):
        return

    if r == 5:
        if all(restriction == [0, 0] for restriction in col_restrictions):
            possible_grids.append([r[:] for r in grid])

        return

    if grid[r][c] != -1:
        fill_recursive(*next_pos(r, c))
        return

    if row_restrictions[r][1] != 0 and col_restrictions[c][1] != 0:
        do_next(0, r, c)

    for i in range(1, 4):
        if row_restrictions[r][0] >= i and col_restrictions[c][0] >= i:
            do_next(i, r, c)


def do_next(v, r, c):
    grid[r][c] = v
    if v == 0:
        row_restrictions[r][1] -= 1
        col_restrictions[c][1] -= 1
        fill_recursive(*next_pos(r, c))
        row_restrictions[r][1] += 1
        col_restrictions[c][1] += 1
    else:
        row_restrictions[r][0] -= v
        col_restrictions[c][0] -= v
        fill_recursive(*next_pos(r, c))
        row_restrictions[r][0] += v
        col_restrictions[c][0] += v
    grid[r][c] = -1


def perma_sub(v, r, c):
    grid[r][c] = v
    if v == 0:
        row_restrictions[r][1] -= 1
        col_restrictions[c][1] -= 1
    else:
        row_restrictions[r][0] -= v
        col_restrictions[c][0] -= v


def next_pos(r, c):
    if c == 4:
        return (r + 1, 0)
    return (r, c + 1)


def main():
    while True:
        global possible_grids
        possible_grids = []
        fill_recursive(0, 0)

        counts = [[defaultdict(int) for _ in range(5)] for _ in range(5)]

        for g in possible_grids:
            for r in range(5):
                for c in range(5):
                    if grid[r][c] != -1 and grid[r][c] != g[r][c]:
                        print(*g)
                        assert False
            else:
                for r in range(5):
                    for c in range(5):
                        counts[r][c][g[r][c]] += 1

        def getscore(v):
            r, c = v
            return 1 - (counts[r][c][0] / sum(counts[r][c].values())), 1 - (
                (counts[r][c][0] + counts[r][c][1]) / sum(counts[r][c].values())
            )

        def inc(v):
            return (v[0] + 1, v[1] + 1)

        bestmove = max(
            ((r, c) for r in range(5) for c in range(5) if grid[r][c] == -1),
            key=getscore,
        )

        score = getscore(bestmove)

        print(inc(bestmove), round(score[0], 2), round(score[1], 2))

        value = int(input())

        perma_sub(value, *bestmove)


main()
