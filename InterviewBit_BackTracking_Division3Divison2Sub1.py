from sys import stdin as si
from collections import Counter as C
from operator import itemgetter as ig
from functools import reduce 
from sys import maxsize as m

class Solution:
    # @param A : Integer
    # @return an integer
    def m(self,N):
        print (N)
        if N in [1,2,3]:
            return 1
        else:
            th,tw=False,False
            s3,s2 = 1,1
            if (N-1)%3==0:
                #print ('in N-1 3')
                s3 += self.m(N-1)
                th = True
            elif N%3==0:
                #print ('in N 3')
                s3 += self.m(int(N/3))
                th = True
            if (N-1)%2==0:
                #print ('in N-1 2')
                s2 += self.m(N-1)
                tw=True
            elif N%2==0:
                #print ('in N 2')
                s2 += self.m(int(N/2))
                tw = True
            if th and tw:
                return min(s3,s2)
            elif not tw:
                return s3
            elif not th:
                return s2

if __name__ == "__main__":
    for i in range(int(si.readline())):
        n = int(input())
        S = Solution()
        print (S.m(n))


'''
Given an Integer N:

There are three possible operations
1) Divide by Three
2) Divide by Two
3) Sub by 1

1st and 2nd step can only be performed only when an Int is completely
divisible by 3/2.

Find the minimum number of steps to take to reduce the N to one.
'''
