from sys import stdin as si
from collections import Counter as C
from operator import itemgetter as ig
from functools import reduce 
from sys import maxsize as m

class Solution(object):
    def majorityElement(self, A):
        m,c=0,1 
        for i in range(1,len(A)):
            if A[m]==A[i]:
                c+=1
            else:   c-=1
            if c==0:
                m=i
                c=1
        return A[m]

if __name__ == "__main__":
    for i in range(int(si.readline())):
        A = sys.readline().split()
        S = Solution()
        print (S.majorityElement(A))
        

'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''
