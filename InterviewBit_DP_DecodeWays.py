class Solution:
    def __init__(self):
        self.g = {}
        
    def check(self,i):
        if int(i) in range(1,27):   return True
        else:   False
        
    def numDecodings(self,A):
        if A in self.g:  return self.g[A]
        res = 0
        if len(A)==0 or len(A)==A.count('0')or  A[0]=='0':   res = 0
        else:   #return self.bazinga(A)
            if A=='':    res=0
            elif len(A)==1 and self.check(A): res= 1
            elif len(A)==2:
                if self.check(A):
                    if A[1]=='0':   res= 1
                    else:   res = 2
                
                else:   
                    if A[0] in ['1','2'] or '0' not in A:   res= 1
                    else:   res = 0
            else:
                x,y=0,0
                if self.check(A[0]):    x = self.numDecodings(A[1:])
                if self.check(A[:2]):   y = self.numDecodings(A[2:])
                res= x+y
        self.g[A]=res
        return res   
            
        
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        s = input()
        print (S.numDecodings(s))


'''
012--->0
01---->0
00---->0
99---->1
90---->0



A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given an encoded message containing digits, determine the total number of ways to decode it.

Example :

Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''

