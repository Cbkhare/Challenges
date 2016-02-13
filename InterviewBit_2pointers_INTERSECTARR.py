class Solution:
    # @param A : sorted tuple of integers
    # @param B : sorted tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        stack = []
        lastJ=0
        for i in range(len(A)):
            if lastJ<=len(B)-1:
                j = lastJ
            else:
                break
            while B[j]<=A[i]:
                
                if B[j]==A[i]:
                    stack.append(A[i])
                    lastJ= j+1
                    break
                if j==len(B)-1:    break
                j+=1
        return stack

        
if __name__=='__main__':
    B = Solution()
    n = int(input())
    for i in range(n):
        c  = tuple(map(int,input().split(' ')))
        c1 = tuple(map(int,input().split(' ')))
        print (B.intersect(c,c1))
    

'''
INTERSECTARR
Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.

Example :

Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]

Output : [3 3 5]

Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 5]

Output : [3 5]

    NOTE : For the purpose of this problem ( as also conveyed by the sample case ), assume that elements that appear more than once in both arrays should be included multiple times in the final output. 

'''
