class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        stack = []      #Real Stack
        Graph = {
        ']':'[',
        '}':'{',
        ')':'('
        }

        for e in A:
            if e in ['[','{','(']:
                stack.append(e)
            else:
                if stack==[] or Graph[e]!=stack[-1]:
                    return 0
                else:
                    stack.pop(len(stack)-1)     #pop last 
        if len(stack) ==0:
            return 1
        else:
            return 0
              
if __name__=='__main__':
    B = Solution()
    n = int(input())
    for i in range(n):
        c = input()
        #c = list(map(int,input().split(' ')))
        print (B.isValid(c))
'''
PARENTHESIS

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''
