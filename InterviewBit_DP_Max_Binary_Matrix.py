from sys import maxsize as m
class Solution:

    def bazinga(self,A):
        m,n = len(A),len(A[0])
        Max = 0
        for i in range(1,m):
            for j in range(n):
                if A[i][j]==1:
                    A[i][j] = min(A[i-1][j-1],A[i-1][j],A[i][j-1])+1
                    Max= max(A[i][j],Max)
        return (Max**2)
                    


if __name__=='__main__':

    S = Solution()
    T = int(input())
    for i in range(T):
        m,n =  map(int,input().split(' '))
        A = []
        for i in range(m):
            A.append(list(map(int,input().split(' '))))
        print (S.bazinga(A))
        
            
'''
Find maximum area a binary matrix with '1' possible

'''
        
        
    
        
