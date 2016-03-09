from sys import maxsize as m
class Solution:
    def __init__(self):
        self.g = {}

    def adjacent(self,A):
        n = len(A[0])
        B = {} #[0 for i in range(n)]
        for i in range(n+1):
            B[i]=0
        B[n-1]=max(A[0][n-1],A[1][n-1])
        res = B[n-1]
        Max = -m
        for i in range(n-2,-1,-1):
            Max = max(B[i+2],Max)
            B[i]= max(A[0][i],A[1][i])+Max
            res = max(Max,B[i])
        return res

if __name__=='__main__':
    T = int(input())
    for i in range(T):
        S = Solution()
        n,m = map(int,input().split(' '))
        T = []
        for i in range(n):
            T += [list(map(int,input().split(', ')))]
        
        print (S.adjacent(T))
        

        
'''


Given a 2 * N Grid of numbers, choose numbers such that the sum of the numbers
is maximum and no two chosen numbers are adjacent horizontally, vertically or diagonally, and return it.

Example:

Grid:
	1 2 3 4
	2 3 4 5
so we will choose
3 and 5 so sum will be 3 + 5 = 8


Note that you can choose more than 2 numbers
'''
