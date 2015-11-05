class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        s =set(A)
        for i in s:
            c = A.count(i)
            if c==1:
                return i

if __name__=='__main__':

    B =Solution()
    print (B.singleNumber(list(map(int,input().split(' ')))))


'''
SINGLE

Given an array of integers, every element appears twice except for one. Find that single one.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example :

Input : [1 2 2 3 1]
Output : 3


'''
