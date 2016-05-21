from sys import stdin as Si, maxsize as m
from math import factorial as F,log as lg 
import collections
from operator import itemgetter as ig 

        
class Solution:
    def max3p(self,A):
        if len(A)==3:   return A[0]*A[1]*A[2]
        A = sorted(A)
        mx,mx2 = A[0],A[1]
        mi,mi2 = A[0],A[1]
        p3 = -m
        for a in A[1:]:
            #print(mx,mx2,mi,mi2,p2)
            p3 =  max(mx*mx2*a,mi*mi2*a,p2)
            mx,mx2 = sorted([a,mx,mx2],reverse=True)[:2]
            mi,mi2 = sorted([a,mi,mi2])[:2]
            
        return p3
        
if __name__=='__main__':
    S=Solution()
    for i in range(int(Si.readline())):
        a = list(map(int,Si.readline().split()))
        print (S.max3p(a))

'''
Highest Product

Given an array of integers, return the highest product possible by multiplying 3 numbers from the array

Input:

array of integers e.g {1, 2, 3}

    NOTE: Solution will fit in a 32-bit signed integer 

Example:

[0, -1, 3, 100, 70, 50]

=> 70*50*100 = 350000


'''
