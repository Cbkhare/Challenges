from fractions import gcd
class Solution:
    # @param A : integer
    # @return a list of integers
    def gcd(self, A, B):
        x= [A,B]
        x.sort()
        g = 1
        for i in xrange(1,x[0]+1):
            if A%i==0:
                if B%i==0:
                    g *=i
                else:
                    continue
        return g       
        #return gcd(A,B)

B = Solution()
m = int(raw_input())
n = int(raw_input())
print B.gcd(m,n)



'''
Given 2 non negative integers m and n, find gcd(m, n)

GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.
Both m and n fit in a 32 bit signed integer.

Example

m : 6
n : 9

GCD(m, n) : 3 
'''
