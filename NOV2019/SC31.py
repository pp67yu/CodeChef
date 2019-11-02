# passed full - https://www.codechef.com/NOV19B/problems/SC31


def calc(A):
    s = ""
    for a, b in zip(*A):
        s += str(int(a) ^ int(b))
    return s


if __name__ == "__main__":
    for _ in range(int(input())):
        A = []
        for _ in range(int(input())):
            A.append(input())
            if len(A) == 2:
                A = [calc(A)]
        print(A[0].count("1"))
