from sys import stdin as si
from math import sqrt; from itertools import count, islice
from sys import maxsize as m

class Solution(object):
    def missingNumber(self, nums):
        S = sum(nums)
        return sum(range(0,len(nums)+1))-S
        
if __name__=="__main__":
    n = int(si.readline())
    for i in range(n):
        S = Solution()
        a = list(map(int, si.readline().split()))
        print (S.missingNumber(a))
        
    
    
'''
 Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''
