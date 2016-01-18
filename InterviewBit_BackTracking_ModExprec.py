class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def Mod(self, A, B, C):
        if A==0:
            return 0
        if B==0:
            return 1
        elif A%2==0:
            y = self.Mod(A,int(B/2),C)
            return (y*y)%C
        else:
            return ((A%C)*self.Mod(A,B-1,C)%C)

        
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c,c1,c2 = list(map(int,input().split(' ')))
        print (S.Mod(c,c1,c2))


'''


Implement pow(A, B) % C.

In other words, given A, B and C,
find (AB)%C.

Input : A = 2, B = 3, C = 3
Return : 2 
2^3 % 3 = 8 % 3 = 2

'''
