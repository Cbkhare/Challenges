class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        if len(A)==1:   return [-1]
        stack,i = [0],1
        while i <len(A):
            if stack==[] or A[i]<=A[stack[-1]]:
                stack.append(i)
                i+=1
            else:
                A[stack.pop()]=A[i]
        while len(stack)!=0:
            A[stack.pop()] = -1
        return A
  
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c = list(map(int,input().split(' ')))
        print (S.nextGreater(c))
        

'''
NEXTGREATER

Given an array, find the next greater element G[i] for every element A[i] in the array. The Next greater Element for an element A[i] is the first greater element on the right side of A[i] in array.
More formally,

G[i] for an element A[i] = an element A[j] such that 
    j is minimum possible AND 
    j > i AND
    A[j] > A[i]

Elements for which no greater element exist, consider next greater element as -1.

Example:

Input : A : [4, 5, 2, 10]
Output : [5, 10, 10, -1]

Example 2:

Input : A : [3, 2, 1]
Output : [-1, -1, -1]
'''
