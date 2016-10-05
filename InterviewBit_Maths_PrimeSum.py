from sys import stdin as si
from math import sqrt; from itertools import count, islice


class Solution(object):
        
    def primesum(self, A):
        for i in range(2,A-1):
            if self.isPrime(i) and self.isPrime(A-i):
                return [i,A-i]

    def is_prime(self, n):
        if n < 2:
            return False

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False

        return True
        
if __name__=="__main__":
    n = int(si.readline())
    for i in range(n):
        S = Solution()
        a = int(si.readline())
        print (S.primesum(a))
        
    
    
'''
Prime Sum

Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

NOTE A solution will always exist. read Goldbach’s conjecture

Example:


Input : 4
Output: 2 + 2 = 4

If there are more than one solutions possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b,
and [c,d] is another solution with c <= d, then

[a, b] < [c, d] 

If a < c OR a==c AND b < d. 


'''
