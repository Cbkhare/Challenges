class Solution:
    def maxProduct(self, A):
        ans,minPro,maxPro = A[0],A[0],A[0]
        for a in A[1:]:
            tempMaxPro = maxPro
            tempMinPro = minPro
            maxPro = max(max(tempMaxPro*a,tempMinPro*a), a)
            minPro = min(min(tempMaxPro*a,tempMinPro*a), a)
            ans = max(ans,maxPro)
        return ans
            
if __name__=='__main__':
    S = Solution()
    n = int(input())
    for j in range(n):
        s = tuple(map(int,input().split(' ')))
        print (S.maxProduct(s))

'''
MAXPROD

Find the contiguous subarray within an array (containing at least one number) which has the largest product.
Return an integer corresponding to the maximum product possible.

Example :

Input : [2, 3, -2, 4]
Return : 6 

Possible with [2, 3]


'''
