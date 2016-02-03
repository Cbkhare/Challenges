class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        if A>=5:
            return self.trailingZeroes(int(A/5))+int(A/5)
        else:
            return 0
'''
FACTORIAL

Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Example :

n = 5
n! = 120 
Number of trailing zeros = 1
So, return 1

'''
