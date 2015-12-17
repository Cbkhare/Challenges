class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        gp = {}   #a kind of hashing 
        s=0
        Af = []
        Sum = 0
        for i in range(len(A)):
            Sum+=A[i]
            if Sum==0:
                Af=A[:i+1]
            elif Sum in gp:
                s=gp[Sum][0]
                ts = A[s+1:i+1]
                if len(ts)>len(Af):
                    Af = ts
                gp[Sum]+=[i]
            else:
                gp[Sum]=[i]
        return Af       

        
            
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c = list(map(int,input().split(' ')))
        print (S.lszero(c))

'''

Find the largest continuous sequence in a array which sums to zero.

Example:


Input:  {1 ,2 ,-2 ,4 ,-4}
Output: {2 ,-2 ,4 ,-4}

    NOTE : If there are multiple correct answers, return the sequence which occurs first in the array. 

'''
