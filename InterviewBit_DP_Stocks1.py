class Solution:

    def maxProfit(self, A):
        n = len(A)
        r = 0
        if n>1: 
            mn = A[0]
            for i in range(1,n):
                mn = min(A[i],mn)
                r = max(r,A[i]-mn)
        return r
            
        
if __name__=='__main__':

    S = Solution()
    n = int(input())
    for i in range(n):
        s = tuple(map(int,input().split(' ')))
        print (S.maxProfit(s))
    
'''
5
5 4 1 2 6
5
1 2 4
3
4 2 1
0

STOCKS1

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example :

Input : [1 2]
Return :  1


'''
