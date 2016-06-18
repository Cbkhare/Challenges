from sys import stdin as Si
from math import ceil as C 

def solution(A):
    X = sum(A[i]*pow(-2,i) for i in range(len(A)))
    X=-X
    Ans = []
    while X not in [0,1,-1]:
        ox = X
        if X*-1==-1: #num is +ve
            X = int(X/-2)
            R = ox-X*-2
        else:
            X = 1*C(X/-2)
            R = ox - X*-2
        Ans.append(R)
    if X==-1:   Ans.append(1);Ans.append(1)
    else:   Ans.append(X)
    return Ans

    
if __name__=='__main__':
    t = int(Si.readline())
    for i in range(t):
        n = list(map(int,Si.readline().split()))
        print (solution(n)) 


'''
Base -2 conversion
1 0 0 1 1 1
-23
23 [1, 1, 0, 1, 0, 1, 1]
1 0 0 1 1
9
-9 [1, 1, 0, 1]
'''
