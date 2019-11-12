# https://www.codechef.com/NOV19B/problems/PHCUL
# Partially correct (N, M, K < 101, 50 points)


D = dict()


# function to return the distance between two specific points:
# -> returns distance
def distance(A, B):
    if tuple(A + B) in D:
        return D[tuple(A + B)]

    d = ((A[0] - B[0])**2 + (A[1] - B[1])**2) ** 0.5
    D[tuple(A + B)] = D[tuple(B + A)] = d
    return d


# split a list into a list of x, y co-ordinates
# -> returns list of points(lists). list[lists]
def arr(A):
    res = []
    s = []
    for a in A:
        s.append(a)
        if len(s) == 2:
            res.append(s)
            s = []
    return res


def calculate(X, A, B, E):
    res1 = []
    for a in A:
        for b in B:
            D = distance(X, a) + distance(a, b)
            res1.append(D)

    res2 = []
    for i, b in enumerate(B):
        for e in E:
            L = distance(b, e)
            for j in range(i, len(res1), len(B)):
                res2.append(res1[j] + L)

    return min(res2)


if __name__ == "__main__":
    for _ in range(int(input())):
        # A = B = E = []
        X = list(map(int, input().split()))
        N, M, K = list(map(int, input().split()))
        F = list(map(int, input().split()))
        Y = list(map(int, input().split()))
        Z = list(map(int, input().split()))
        A = arr(F)
        B = arr(Y)
        E = arr(Z)
        print(min(calculate(X, A, B, E), calculate(X, B, A, E)))
