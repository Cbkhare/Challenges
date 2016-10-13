from sys import stdin as si
from math import sqrt; from itertools import count, islice
from sys import maxsize as m

class Solution(object):
    
    def gcd(self, A,B ):
        if A==0 or B==0:    return max(A,B)
        test =1
        while test>0:
            test= A%B
            A=B
            B=test
        return A 
        
    
        
if __name__=="__main__":
    n = int(si.readline())
    for i in range(n):
        S = Solution()
        a,b = map(int,si.readline().split())
        print (S.gcd(a,b))
        
    
    
'''
Greatest Common Divisor

Given 2 non negative integers m and n, find gcd(m, n)

GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.
Both m and n fit in a 32 bit signed integer.

Example

m : 6
n : 9

GCD(m, n) : 3 


'''
