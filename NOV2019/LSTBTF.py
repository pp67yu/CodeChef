# Passed (partial: for N <= 100)
# https://www.codechef.com/NOV19B/problems/LSTBTF

import math


# function to check if a number is a perfect square
def perf_square(x):
    root = math.sqrt(x)
    return x == int(root + 0.5) ** 2


# function to check requirement
def root_check(m):
    ans = 0

    for j in str(m):
        ans += int(j) ** 2

    if perf_square(ans):
        return True
    else:
        return False


def calculate(n):
    if n == 1:
        return n

    start = int("1" * n)
    end = int("9" * n)

    for i in range(start, end+1):
        if "0" not in str(i) and root_check(i):
            return i

    return -1


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        print(calculate(n))
