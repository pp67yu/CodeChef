# https://www.codechef.com/DEC19B/problems/PLMU
# full passed


def calculate(L):
    count = 0
    give = dict()

    for i in L:
        if i != 1:
            w = i/(i-1)

        if w in give:
            count += give[w]

        if i in give:
            give[i] += 1
        else:
            give[i] = 1

    print(count)


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        seq = list(map(int, input().split()))
        calculate(seq)
