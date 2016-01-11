class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def swap (self,B,x,y):
        temp = B[x]
        B[x]=B[y]
        B[y]=temp
        return B
    def permuteMe(self,A,c):
        if c ==len(A)-1:
            print (A)
            if A not in self.S:  self.S.append(A[:])
        else:
            for j in range(c,len(A)):
                A = self.swap(A,c,j)
                self.permuteMe(A,c+1)
                A = self.swap(A,c,j)
                
    def permute(self, A):
        self.S = []
        c = 0
        self.permuteMe(A,c)
        return self.S 
        
        
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        c = list(map(int,input().split(' ')))
        S = Solution()
        print (S.permute(c))
        


'''


Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example :
[1,1,2] have the following unique permutations:

[1,1,2]
[1,2,1]
[2,1,1]

    NOTE : No 2 entries in the permutation sequence should be the same. 

    Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS.

    Example : next_permutations in C++ / itertools.permutations in python.
    If you do, we will disqualify your submission retroactively and give you penalty points. 

'''
