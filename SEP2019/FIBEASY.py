"""
https://www.codechef.com/problems/FIBEASY

solved (partial)

Fib = 0 1 1 2 3 5 8
"""

from math import log, pow

def form_seq(N):
    # form a array of list of remainders of fibs:
    a, b = 0, 1
    res = [0, 1]

    #if N < 0 or N == 1: 
    #    return 0
    #elif N == 1: 
    #    return 1
    #else: 
    for _ in range(2,N): 
        c = a + b 
        res.append(c%10)
        a = b 
        b = c
    
    return res
    #print("".join(map(str, res))[3:].find('011'))


def find_req(N):
    if N == 0:
        return 0

    n = int(log(N, 2))
    f = int(pow(2, n))

    F = f % 60

    return F


if __name__ == "__main__":
    seq = form_seq(60)
    for _ in range(int(raw_input())):
        N = int(raw_input())
        if N == 0 or N == 1:
            print(N)
        else:
            x = find_req(N)
            if x > 0:
                print(seq[x-1])
            else:
                print("0")


x = find_req(0)
print(x)




