# https://www.codechef.com/DEC19B/problems/WATSCORE
# full passed


def calculate(D):
    ans = 0
    for i in range(1, 9):
        if i in D:
            ans += D[i]
    return ans


if __name__ == "__main__":
    for _ in range(int(input())):
        scores = dict()
        for _ in range(int(input())):
            p, score = list(map(int, input().split()))
            if p in scores:
                scores[p] = max(scores[p], score)
            else:
                scores[p] = score
        print(calculate(scores))
