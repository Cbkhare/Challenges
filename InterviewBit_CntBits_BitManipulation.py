from itertools import permutations as cr 
class Solution:
    def findDiffBits(self,T):
        x,y = T
        #x = bin(x)[2:]
        #y = bin(y)[2:]
        d = bin(x^y)[2:].count('1')
        #print (x,y,d)
        return d 

    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        '''
        per = cr(A,2)
        s = 0 
        for p in per:
            s += bin(p[0]^p[1])[2:].count('1')
            #s += self.findDiffBits(p)
        return s
        '''
        #without permutations 
        s= 0 
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                s += 2*(bin(A[i]^A[j])[2:].count('1'))
        return s 
      
    
if __name__=='__main__':
    B = Solution()
    n = int(input())
    #c  = tuple(map(int,input().split(' ')))
    for i in range(n):
        c  = tuple(map(int,input().split(' ')))
        #m = int(input())
        print (B.cntBits(c))
    

'''


We define f(X, Y) as number of different corresponding bits in binary representation of X and Y. For example, f(2, 7) = 2, since binary representation of 2 and 7 are 010 and 111, respectively. The first and the third bit differ, so f(2, 7) = 2.

You are given an array of N positive integers, A1, A2 ,…, AN. Find sum of f(Ai, Aj) for all pairs (i, j) such that 1 ≤ i, j ≤ N. Return the answer modulo 109+7.

For example,

A=[1, 3, 5]

We return

f(1, 1) + f(1, 3) + f(1, 5) + 
f(3, 1) + f(3, 3) + f(3, 5) +
f(5, 1) + f(5, 3) + f(5, 5) =

0 + 1 + 1 +
1 + 0 + 2 +
1 + 2 + 0 = 8

'''
