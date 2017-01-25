from sys import stdin as si

class Solution(object):
    """object for MRO refrencing"""

    def __init__(self):
        pass


    def maxSubArray(self, A):
        if A==[]:   return 0

        #kadane's algorithm
        tSum=fSum = A[0] #tempSum, finalSum 
        for n in A[1:]:
            tSum = max(n, tSum+n)
            fSum = max(tSum,fSum)
        return fSum


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        A = tuple(map(int,si.readline().split(',')))
        S = Solution()
        print (S.maxSubArray(A))

    
'''
Max Sum Contiguous Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example:

Given the array [-2,1,-3,4,-1,2,1,-5,4],

the contiguous subarray [4,-1,2,1] has the largest sum = 6.

For this problem, return the maximum sum.


'''
