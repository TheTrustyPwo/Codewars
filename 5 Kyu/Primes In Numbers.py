"""
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"

https://www.codewars.com/kata/54d512e62a5e54c96200019e
"""

def primeFactors(n: int) -> str:
    i, j, p = 2, 0, []
    while n > 1:
        while n % i == 0:
            n /= i
            j += 1
        if j > 0:
            p.append([i,j])
        i += 1
        j = 0
    return ''.join('(%d' %q[0] + ('**%d' %q[1]) * (q[1] > 1) + ')' for q in p)