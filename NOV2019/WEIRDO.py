# https://www.codechef.com/NOV19B/problems/WEIRDO
# Editorial: https://discuss.codechef.com/t/weirdo-editorial/43717
# full pass in practice
"""
# finding is a recepie belongs to Alice or Bob:
here subsrtring of a string is defined as:
Ex:
substrings of string: aba are aba, ba
substrings of string: baab are baab, aab, ab
vowels = v
consonants = c
hence if we have a pattern as cvc, c can be one of the substrings.
then it belongs to Bob
or if we have a pattern as cc somewhere in the string,
we can have a pattern as cc, or ccv, vcc making it Bobs recepie

for calculating ans, use log values to ensure we dont miss the acuracy
of the very small or very large numbers
"""

import math
import re

wr1 = re.compile(r'[^aeiou][aeiou][^aeiou]')
wr2 = re.compile(r'[^aeiou][^aeiou]')


# function to check if the input recepie is Alice or Bob:
def isAlice(word):
    if wr1.search(word) or wr2.search(word):
        return False
    else:
        return True


def occCount(word, D1, D2):
    # D1 is alph occurance count
    # D2 is alph count
    # met is a set that
    m = set()
    for lett in word:
        if lett in D1:
            D1[lett] += 1
        else:
            D1[lett] = 1

        if lett not in m:
            if lett in D2:
                D2[lett] += 1
            else:
                D2[lett] = 1

        m.add(lett)

    return D1, D2


def calculate(L):
    # Alice
    alice_occ = dict()
    alice_recepie_count = dict()
    # Bob
    bob_occ = dict()
    bob_recepie_count = dict()

    alice = bob = 0

    for word in L:
        if isAlice(word):
            alice += 1
            alice_occ, alice_recepie_count = occCount(
                word, alice_occ, alice_recepie_count)
        else:
            bob += 1
            bob_occ, bob_recepie_count = occCount(
                word, bob_occ, bob_recepie_count)

    A = B = 0

    for occ in alice_recepie_count.keys():
        A += (math.log10(alice_recepie_count[occ]
                         ) - alice*math.log10(alice_occ[occ]))

    for occ in bob_recepie_count.keys():
        B += (math.log10(bob_recepie_count[occ]
                         ) - bob*math.log10(bob_occ[occ]))

    ans = A - B
    return "Infinity" if ans > 7 else math.pow(10, ans)


if __name__ == "__main__":
    for _ in range(int(input())):
        L = []
        for _ in range(int(input())):
            L.append(input())
        print(calculate(L))
