# passed(partial) - https://www.codechef.com/NOV19B/problems/SIMGAM
# for max result for chef - chef keeps choosing the max
# of available and Ramsey keeps choosing the min


def clean(rows):
    while [] in rows:
        rows.remove([])
    return rows


def chef(rows):
    # chef choice: - max first number of rows
    if len(rows) == 1:
        return rows[0][0], clean([rows[0][1:]])

    L = list(zip(*rows))[0]
    n = max(L)

    # remove n from correct list.
    row = L.index(n)
    rows[row].pop(0)

    return n, clean(rows)


def rams(rows):
    if len(rows) == 1:
        return rows[0][-1], clean([rows[0][:-1]])

    L = []

    for r in rows:
        L.append(r[-1])

    n = min(L)

    row = L.index(n)
    rows[row].pop()

    return n, clean(rows)


def calc(rows):
    count = 0
    ch = 0
    ra = 0

    while len(rows) > 0:
        if count % 2 == 0:
            n, rows = chef(rows)
            ch += n
        else:
            n, rows = rams(rows)
            ra += n
        count += 1

    return ch


# R = [[5, 2, 3, 4], [1, 6]]
# print(rams(R))
if __name__ == "__main__":
    for _ in range(int(input())):
        rows = []
        for _ in range(int(input())):
            L = list(map(int, input().split()))
            rows.append(L[1:])
        print(calc(rows))
