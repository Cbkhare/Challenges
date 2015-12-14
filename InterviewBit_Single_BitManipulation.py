class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        a = 0
        for i in range(len(A)):
            a ^= A[i]
        return a 

      
    
if __name__=='__main__':
    B = Solution()
    n = int(input())
    for i in range(n):
        c  = tuple(map(int,input().split(' ')))
        print (B.singleNumber(c))
    

'''
SINGLE

Given an array of integers, every element appears twice except for one. Find that single one.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example :

Input : [1 2 2 3 1]
Output : 3
'''
