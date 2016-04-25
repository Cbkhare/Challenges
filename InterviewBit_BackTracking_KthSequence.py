from sys import stdin as Si, maxsize as m
from math import factorial as F

class Solution(object):

    def getP(self,N,K):
        #Base condition
        if len(N) == 0: return ''
        if K<=0 and N!=[]:  return ''.join(map(str,sorted(N)[::-1]))
        
        N,l = sorted(N),len(N)
        f = F(l-1)
        
        #getting first digit

        if K%f==0:
            pos = (K//f)-1
            Num = str(N.pop(pos)) + self.getP(N,K-(pos+1)*F(l-1))
        else:
            pos = K//f
            Num = str(N.pop(pos)) + self.getP(N,K-pos*F(l-1))

        return Num

    def getPermutation(self, n, k):
        return self.getP([i for i in range(1,n+1)],k)
       
if __name__=='__main__':

    n,k = map(int,Si.readline().split())
    S = Solution()
    print (S.getPermutation(n, k))

'''
Kth Permutation Sequence

The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3 ) :

1. "123"
2. "132"
3. "213"
4. "231"
5. "312"
6. "321"

Given n and k, return the kth permutation sequence.

For example, given n = 3, k = 4, ans = "231"

    Good questions to ask the interviewer :

        What if n is greater than 10. How should multiple digit numbers be represented in string?
        > In this case, just concatenate the number to the answer.
        > so if n = 11, k = 1, ans = "1234567891011"

        Whats the maximum value of n and k?
        > In this case, k will be a positive integer thats less than INT_MAX.
        > n is reasonable enough to make sure the answer does not bloat up a lot.


'''
    
