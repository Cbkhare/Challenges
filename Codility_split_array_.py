from sys import stdin as Si

def solution(X,A):
    for i in range(len(A)):
        if A[i]==X:
            A[i]=1
        else: A[i]=0
    for i in range(1,len(A)):
        if A[:i].count(1)==A[i:].count(0):
            return i
    else:   return 0
    
if __name__=='__main__':
    t = int(Si.readline())
    for i in range(t):
        x = int(Si.readline())
        n = list(map(int,Si.readline().split()))
        print (solution(x,n)) 
'''
split array such that
Number of elements equal to X in first part if equal to number of
elements not equal to X
'''
