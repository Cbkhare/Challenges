from sys import stdin as si
from collections import Counter as C
from operator import itemgetter as ig
from functools import reduce 
from sys import maxsize as m

class Solution(object):
    
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            if nums[i]<=0 or nums[i]>n: nums[i]=0

        i= 0
        while i<n:
            #'i' wont inccrease unless i!=nums[i]
            if nums[i]>0:
                index = nums[i]-1
                if nums[index]>=0:
                    nums[i]=nums[index]
                else:
                    nums[i]=0
                nums[index]=-1
            else:
                i+=1

        for i in range(n):
            if nums[i]==0: return i+1
        else:
            return n+1
                
        

        

if __name__ == "__main__":
    for i in range(int(si.readline())):
        A = list(map(int,si.readline().split(' ')))
        S = Solution()
        print (S.firstMissingPositive(A))


'''
First Missing Integer

Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1

Your algorithm should run in O(n) time and use constant space.
'''
