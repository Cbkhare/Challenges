class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        one, two = 0, 0
        for i in range(0, len(A)) :
            one, two = (one ^ A[i]) & ~two , (one & A[i]) | (two & ~A[i])
            #print (one, two)
        return one
      
    
if __name__=='__main__':
    B = Solution()
    n = int(input())
    #c  = tuple(map(int,input().split(' ')))
    for i in range(n):
        c  = tuple(map(int,input().split(' ')))
        #m = int(input())
        print (B.singleNumber(c))
    

'''

SINGLE2

Given an array of integers, every element appears thrice except for one which occurs once.

Find that element which does not appear thrice.

Note: Your algorithm should have a linear runtime complexity.

Could you implement it without using extra memory?

Example :

Input : [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
Output : 4

'''
