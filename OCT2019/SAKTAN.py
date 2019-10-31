# https://www.codechef.com/OCT19B/problems/SAKTAN
# passed

import numpy as np

# seperate the rows and columns
# op each by % 2


# proc that works only for smaller inputs.
def process(R, C, points):
    arr = np.zeros((R, C), dtype=int)
    for a, b in points:
        arr[a-1, :] += 1
        arr[:, b-1] += 1
    arr %= 2
    print(np.count_nonzero(arr == 1))


# Works for all inputs
def process2(r, c):
    for i in range(len(r)):
        r[i] %= 2
    for j in range(len(c)):
        c[j] %= 2

    # get actual number of uniqe columns and rows:
    rr = sum(r)
    cc = sum(c)

    row = (C - cc) * rr
    col = (R - rr) * cc

    print(row + col)


if __name__ == "__main__":
    for _ in range(int(input())):
        R, C, Q = list(map(int, input().split()))
        r = [0] * R
        c = [0] * C
        i = 0
        while i < Q:
            a, b = list(map(int, input().split()))
            r[a-1] += 1
            c[b-1] += 1
            i += 1
        process2(r, c)


"""
# init for smaller values workable procedure - using numpy
if __name__ == "__main__":
    for _ in range(int(input())):
        R, C, Q = list(map(int, input().split()))
        points = []
        i = 0
        while i < Q:
            points.append(list(map(int, input().split())))
            i += 1
        process(R, C, points)
"""
