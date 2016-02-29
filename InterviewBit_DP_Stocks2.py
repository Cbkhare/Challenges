class Solution:
        
    def maxProfit(self,P):
        if len(P)==0: return 0
        mn = P[0]
        mx = P[0]
        profit,res = 0,0
        for i in range(1,len(P)):
            mn = min(P[i],mn)
            mx = max(P[i],mx)
            res = max(res,P[i]-mn)  
            if P[i]<mx:
                mn = P[i]
                mx = P[i]
                profit += res
                res = 0
        profit +=res
        return (profit)
            
        
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        s = tuple(map(int,input().split(' ')))
        print (S.maxProfit(s))


'''

4 3 4 5 6 8 1 0
5

4 3 4 5 6 8 1 2 3
7

1 2 3 4 2 3 4 5 6
7

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example :

Input : [1 2 3]
Return : 2


'''
