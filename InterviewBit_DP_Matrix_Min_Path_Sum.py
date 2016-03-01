class Solution(object):

    def minPathSum(self,M):
        n = len(M)
        for i in range(n-1,-1,-1):
            l = len(M[i])
            if i==n-1:
                for j in range(l-2,-1,-1):
                    M[i][j]=M[i][j+1]+M[i][j]
            else:
                for j in range(l-1,-1,-1):      #for j in range(0,i+1):
                    if j==l-1:
                        M[i][j] = M[i+1][j] + M[i][j]
                    else:
                        M[i][j] = min(M[i+1][j],M[i][j+1]) + M[i][j]
        #print(M)
        return M[0][0]


if __name__=='__main__':

    S = Solution()
    Tri = []
    for x in range(int(input('Matrix length:- '))):
        Tri+= [list(map(int,input().split(' ')))]
    print  (S.minPathSum(Tri))
    
        
