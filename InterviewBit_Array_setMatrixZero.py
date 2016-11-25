from sys import stdin as si

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        cols = []
        for x in range(len(A)):
            col = False
            for y in range(len(A[x])):
                if A[x][y]==0:
                    cols.append(y)
                    col = True
            if col:
                A[x] = [ 0 for h in range(len(A[x]))]
            
        for x in range(len(A)):
            for y in range(len(A[x])):
                if y in cols:
                    A[x][y]=0
        return A


if __name__ == "__main__":
    for i in range(int(si.readline())):
        x,y = map(int,si.readline().split())
        A = list(map(int,si.readline().split()))
        #A = [A[j] for j in range(0,len(A),y)
        B = []
        for j in range(x):
            t= []
            for k in range(y):
                t.append(A.pop(0))
            B.append(t)
        S = Solution()
        print (S.setZeroes(B))


'''
Set Matrix Zeros

Given an m x n matrix of 0s and 1s, if an element is 0, set its entire row and column to 0.

Do it in place.

Example

Given array A as

1 0 1
1 1 1 
1 1 1

On returning, the array A should be :

0 0 0
1 0 1
1 0 1

Note that this will be evaluated on the extra memory used. Try to minimize the space and time complexity.

'''
