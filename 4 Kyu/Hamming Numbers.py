"""
A Hamming number is a positive integer of the form 2i3j5k, for some non-negative integers i, j, and k.

Write a function that computes the nth smallest Hamming number.

Specifically:

The first smallest Hamming number is 1 = 203050
The second smallest Hamming number is 2 = 213050
The third smallest Hamming number is 3 = 203150
The fourth smallest Hamming number is 4 = 223050
The fifth smallest Hamming number is 5 = 203051
The 20 smallest Hamming numbers are given in the Example test fixture.

https://www.codewars.com/kata/526d84b98f428f14a60008da/train
"""

def hamming(n: int) -> int:
    bases = [2, 3, 5]
    expos = [0, 0, 0]
    hamms = [1]
    next_hamms = [2, 3, 5]
    for _ in range(1, n):
        next_hamm = min(next_hamms)
        hamms.append(next_hamm)
        for i in range(3):
            if next_hamms[i] == next_hamm:
                expos[i] += 1
                next_hamms[i] = bases[i] * hamms[expos[i]]
    return hamms[-1]