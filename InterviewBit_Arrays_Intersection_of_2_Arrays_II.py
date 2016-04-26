from sys import stdin as Si, maxsize as m
from math import factorial as F
import collections 

class Solution(object):
        
    def intersect(self, nums1, nums2):

        ans = []
        nums1 = collections.Counter(nums1)
        #print(nums1)
        for x in nums2:
            if x in nums1:
                ans.append(x)
                nums1[x] -= 1
                if nums1[x] == 0:
                    del nums1[x]
        return ans

        
if __name__=='__main__':

    n = list(map(int,Si.readline().split()))
    k = list(map(int,Si.readline().split()))
    S = Solution()
    print (S.intersect(n, k))
    

'''
 Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:

    Each element in the result should appear as many times as it shows in both arrays.
    The result can be in any order.

Follow up:

    What if the given array is already sorted? How would you optimize your algorithm?
    What if nums1's size is small compared to num2's size? Which algorithm is better?
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


'''
