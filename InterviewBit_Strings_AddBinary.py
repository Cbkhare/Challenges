class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        return bin(int(A,2)+int(B,2))[2:]

        
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c1 = input()
        c2 = input()
        print (S.addBinary(c1,c2))
        

'''
ADDBINARY

Given two binary strings, return their sum (also a binary string).

Example:

a = "100"

b = "11"

Return a + b = “111”.
'''
