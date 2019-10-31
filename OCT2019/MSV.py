# https://www.codechef.com/OCT19B/problems/MSV
# Passed - Partial solve


def process(A):
    if len(A) == 1:
        return 0

    R = [0] * len(A)
    for i, a in enumerate(A):
        if i > 0:
            count = 0
            for num in A[:i]:
                if num % a == 0:
                    count += 1
            R[i] = count

    return max(R)


def get_divisors(n):
    L = set()
    for i in range(1, int((n**0.5) + 1)):
        if n % i == 0:
            L.add(i)
            L.add(n//i)
    return list(L)


def process2(A):
    D = [0]*len(A)
    ans = 0
    D = dict()
    for num in A:
        if num in D:
            ans = max(ans, D[num])

        for k in get_divisors(num):
            if k in D:
                D[k] += 1
            else:
                D[k] = 1
    return ans


if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        A = list(map(int, input().split()))
        x = process2(A)
        print(x)
