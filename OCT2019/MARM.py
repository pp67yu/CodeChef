"""
https://www.codechef.com/OCT19B/problems/MARM

PASSED
---------
Cases:
the result seem to be having a  pattern, 
the first A N, second A N and third A N values seem to be repeating itself.
"""



def mod_seq(N, K, A):
    Q = K // N
    R = K % N
    # Create zip order for Q:
    # Q_order = zip(range(N), range(N)[::-1])
    # R_order = zip(range(R), range(N)[::-1][:R])

    
    if Q == 0:
        if R > 0:
            R_range = zip(range(R), range(N)[::-1][:R])
            i = 0
            for (a, b) in R_range:
                A[i] = A[a] ^ A[b]
                i += 1
        return A
    else:
        # now for the new Q - we find the pattern:
        P = Q % 3
        if P == 1:
            Q = 1
        elif P == 2:
            Q = 2
        else:
            Q = 3
        
        # for each Q rotate xor A:
        Q_order = zip(range(N), range(N)[::-1])
            
        for k, (a, b) in enumerate(list(Q_order) * Q):
            A[k%N] = A[a] ^ A[b]
        
        # for R > 0
        if R > 0:
            R_range = zip(range(R), range(N)[::-1][:R])
            j = 0
            for (a, b) in R_range:
                A[j] = A[a] ^ A[b]
                j += 1
    
        return A


if __name__ == "__main__":
    for i in range(int(input())):
        N, K = list(map(int, raw_input().split()))
        A = list(map(int, raw_input().split()))
        a = mod_seq(N, K, A)
        print(" ".join(list(map(str, a))))


