# Trying a diff approach - but timing out for larger inputs, specifically
# for N > 80000
# https://www.codechef.com/NOV19B/problems/LSTBTF

import math


# function to check if a number is a perfect square
def perf_square(x):
    root = math.sqrt(x)
    return x == int(root + 0.5) ** 2


def root_check2(m, n):
    ans = 0
    M = str(m)
    j = n - 1
    while M[j] != "1":
        ans += int(M[j]) ** 2
        j -= 1
        if j == -1:
            break

    # check j
    if j >= 0:
        ans += (j+1)

    if perf_square(ans):
        return True
    else:
        return False


# function to check requirement
def root_check(m):
    ans = 0

    for j in str(m):
        ans += int(j) ** 2

    if perf_square(ans):
        return True
    else:
        return False


def calculate(start, end, n):
    #print(start, end)
    for i in range(start, end):
        if root_check2(i, n):
            return i

    if end != int("9"*n):
        ref = str(end)
        j = len(ref) - 1

        while ref[j] == "0":
            j -= 1

        start = int("1" * j + ref[j] * (n-j))

        if ref[j] != "9":
            end = int("1" * j + str(int(ref[j]) + 1) +
                      "0" * (n - j - 1))
        else:
            end = start + 1
        print(start, end, n)
        return calculate(start, end, n)


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        st = int("1" * n)
        en = st + 9
        print(calculate(st, en, n))
