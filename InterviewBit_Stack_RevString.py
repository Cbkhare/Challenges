class Solution:
    # @param A : string
    # @return a strings
    def reverseString(self, A):
        stack = ''      #using string reduces memory
        for i in range(len(A)):
            stack+=A[i]
        A = ''
        for i in range(len(stack)-1,-1,-1):
            A+=stack[i]
        return A

    
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c = input()
        print (S.reverseString(c))


'''


Given a string S, reverse the string using stack.

Example :

Input : "abc"
Return "cba"

PROBLEM APPROACH :

Complete solution in hints.
'''
