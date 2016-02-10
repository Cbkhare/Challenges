def coinChange2(C,S):
    m = len(C)  #m is length of Coins
    '''
    cm = tuple([0]*m for j in range(S+1))    #cost-matrix
    for i in range(m):  cm[0][i]=1           #cost 1 to assingment '0'
    '''
    for j in range(S+1):
        if j==0:
            cm =([1]*m,)
        else:
            cm+=([0]*m,)
    
    #print (cm)
    for i in range(1,S+1):
        for j in range(m):
            x = cm[i-C[j]][j]   if i-C[j]>=0 else 0
            y = cm[i][j-1]      if j>=1      else 0
            cm[i][j]=x+y
    print (cm)
    return cm[S][m-1]

            
if __name__=='__main__':
    c = tuple(map(int,input().split(' ')))
    s = int(input())
    print (coinChange2(c,s))

'''


You are given a set of coins S. In how many ways can you make sum N assuming you have infinite amount of each coin in the set.

Note : Coins in set S will be unique. Expected space complexity of this problem is O(N).

Example :

Input : 
	S = [1, 2, 3] 
	N = 4

Return : 4

Explanation : The 4 possible ways are
{1, 1, 1, 1}
{1, 1, 2}
{2, 2}
{1, 3}	

Note that the answer can overflow. So, give us the answer % 1000007

'''
