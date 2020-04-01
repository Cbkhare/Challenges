class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        if l==0:
            return ""
        mx=s[0]
        for i in range(l):
            m = self.expand(s,l,i,i)
            n = self.expand(s,l,i,i+1)
            mx = max(m,n,mx,key=lambda x: len(x))
        return mx
        
    def expand(self,s,l,i,j):
        while (i>=0 and j<l and s[i]==s[j]):
            i-=1
            j+=1
        return s[i+1:j]
