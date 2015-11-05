from collections import deque 
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        stack = deque([deque([1])])
        a = A-1 
        for i in range(a):
            bit = stack[0][0]
            l = len(stack)+2
            for j in range(l):
                if j==0:
                    stack.appendleft(deque([bit+1]*l))
                elif j==l-1:
                    stack.append(deque([bit+1]*l))
                else:
                    stack[j].appendleft(bit+1)
                    stack[j].append(bit+1)
        s = len(stack)
        for r in range(s):           #converting list to deque
            stack.append(list(stack.popleft()))
        return list(stack)
s        
if __name__ == '__main__':

    B = Solution()
    n = int(input())      
    for b in (B.prettyPrint(n)):
        print (b)

'''


Print concentric rectangular pattern in a 2d matrix.
Let us show you some examples to clarify what we mean.

Example 1:

Input: A = 4.
Output:

4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 

Example 2:

Input: A = 3.
Output:

3 3 3 3 3 
3 2 2 2 3 
3 2 1 2 3 
3 2 2 2 3 
3 3 3 3 3 

The outermost rectangle is formed by A, then the next outermost is formed by A-1 and so on.

You will be given A as an argument to the function you need to implement, and you need to return a 2D array.
'''
