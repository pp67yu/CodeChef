"""
passed - https://www.codechef.com/NOV19B/problems/HRDSEQ

Idea:
1. seperate l and prev
2. check if l in prev
    i. if l not in prev: append(0) to seq ->
       update the index for 0 --> update(p, 0, i)
   ii. if l in prev: find the diff of last two occurances,
       add to pattern and update p again
"""


def update(p, value, pos):
    if value not in p:
        p[value] = [pos]
    else:
        p[value].append(pos)
        # if we are saving more than 2 index remove the oldest:
        if len(p[value]) > 2:
            p[value] = p[value][1:]
    return p


def calc(n):
    if n == 1:
        return n

    # init
    # dict to hold position of last occurance:
    p = dict()
    s = [0]
    p[0] = [0]

    for i in range(1, n):
        L = s[-1]
        prev = s[:i - 1]
        if L not in prev:
            s.append(0)
            p = update(p, 0, i)
        else:
            # p = update(p, l, i-1)
            # print(p)
            v = abs(p[L][0] - p[L][1])
            s.append(v)
            p = update(p, v, i)

    return s.count(s[-1])


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        print(calc(n))
