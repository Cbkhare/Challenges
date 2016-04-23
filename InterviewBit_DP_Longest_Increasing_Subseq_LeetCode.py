from sys import stdin as Si, maxsize as m
from math import factorial as F
import collections 


class Solution(object):
    def binSearch(self,Elemnt, Seq,N):
        l=len(Seq)
        low,high=0,l-1
        mid = 0
        while low<high:
            mid = int((low+high)/2)

            if N[Seq[mid]]<Elemnt:
                low = mid +1 
            else:
                high = mid 
        return high
            
            
    
    def lengthOfLIS(self, nums):
        if nums==[]:    return 0
        elem = []   #elem_indexes 
        p = [None for _ in nums]      #parent
        
        for i in range(len(nums)):
            if elem==[] or nums[i]>nums[elem[-1]]:
                if len(elem)>0: p[i]=elem[-1]
                elem.append(i)

            else:
                pos = self.binSearch(nums[i],elem,nums)
                elem[pos]=i
                if pos!=0:
                    p[i]=elem[pos-1]

        cp = elem[-1]   #updating current parent 
        lis = []
        while cp is not None:
            lis.append(nums[cp])
            cp=p[cp]
        lis.reverse()
        return lis
          
                


#NOTE This is a O(N*log(N)) solution, O(N^2) solution also exist using 2-D dynamic Pro 
if __name__=='__main__':

    n = list(map(int,Si.readline().split()))
    S = Solution()
    print (S.lengthOfLIS(n))

'''
 Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
'''
    
