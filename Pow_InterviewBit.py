class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if x==0:    return 0
        if x==1 or n==0:    return 1
        a,y = 1,x%d
        if y<0: y+=d
        while n>0:
            if n & 1: a=(a*y)%d
            y *=y
            y %=d
            if y<0: y+=d
            n>>=1
        return a 

             
if __name__=='__main__':
    B = Solution()
    t = int(input())
    for i in range(t):
        num,po,div = list(map(int,input().split(' ')))
        print (pow(num,po,div))
    

'''
POW

Implement pow(x, n) % d.

In other words, given x, n and d,

find (xn % d)

Note that remainders on division cannot be negative.
In other words, make sure the answer you return is non negative.

Input : x = 2, n = 3, d = 3
Output : 2

2^3 % 3 = 8 % 3 = 2.

'''
