class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        braces = 0
        for c in A :
            if c == '(' :
                braces += 1
            elif c in "*/+-" :
                braces -= 1
            if braces < 0 :
                braces = 0
        if braces == 0 :
            return 0
        else :
            return 1
        
    
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c = input()
        print (S.braces(c))


'''
BRACES

Write a program to validate if the input string has redundant braces?
Return 0/1
0 -> NO 1 -> YES

Input will be always a valid expression

and operators allowed are only + , * , - , /

Example:

((a+b)) has redundant braces so answer will be 1
(a + (a + b)) doesn't have have any redundant braces so answer will be 0

'''
