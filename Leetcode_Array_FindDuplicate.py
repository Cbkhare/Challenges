from sys import stdin as si
from math import sqrt; from itertools import count, islice
from sys import maxsize as m

class Solution(object):
    def findDuplicate(self, A):
        
        for i in range(len(A)):
            index = abs(A[i])-1
            if A[index]<0:  return abs(A[i])
            else:
                A[index] *= -1
    
        
if __name__=="__main__":
    n = int(si.readline())
    for i in range(n):
        S = Solution()
        a = list(map(int, si.readline().split()))
        print (S.findDuplicate(a))
        
    
    
'''
 Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:

    You must not modify the array (assume the array is read only).
    You must use only constant, O(1) extra space.
    Your runtime complexity should be less than O(n2).
    There is only one duplicate number in the array, but it could be repeated more than once
'''
