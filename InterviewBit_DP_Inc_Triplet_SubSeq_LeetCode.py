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
            
            
    
    def increasingTriplet(self, nums):
        if nums==[]:    return False 
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

        cp = elem[-1]
        lis = []
        while cp is not None:
            lis.append(nums[cp])
            cp=p[cp]
        #lis.reverse()

        if len(lis)>=3: return True
        else:   return False 
          
                


#NOTE This is a O(N*log(N)) solution, O(N^2) solution also exist using 2-D dynamic Pro 
if __name__=='__main__':

    n = list(map(int,Si.readline().split()))
    S = Solution()
    print (S.increasingTriplet(n))

'''
 Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

    Return true if there exists i, j, k
    such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false. 

Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.
'''
