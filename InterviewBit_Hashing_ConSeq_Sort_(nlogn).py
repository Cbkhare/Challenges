class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        A.sort()
        gp =1
        i = 0
        mgp = 0
        while i<len(A)-1:
            if A[i+1]-A[i]==1:
                gp+=1
            else:
                gp = 1
            if gp>mgp:  mgp=gp
            i+=1
        return mgp
        
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        c = list(map(int,input().split(' ')))
        S = Solution()
        print (S.longestConsecutive(c))
        


'''


Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Example:
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''
