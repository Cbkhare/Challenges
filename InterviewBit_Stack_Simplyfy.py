class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self,A):
        res = []
        N = len(A)
        start = 0
        if A == '' :
            return "/"
        while start < N :
            while start < N and A[start] == '/' :
                start += 1
            if start == N :
                break
            end = start
            while end < N and A[end] != "/" :
                end += 1
            temp = A[start : end]
            if temp == ".." :
                if res != [] :
                    res.pop()
            elif temp == '.' :
                pass
            else :
                res.append("/" + temp)
            start = end
        if len(res) == 0 :
            return "/"
        return "".join(res)
            
        
        
    
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c = input()
        print (S.simplifyPath(c))


'''
SIMPLIFYPATH

Given an absolute path for a file (Unix-style), simplify it.

Examples:

path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Note that absolute path always begin with ‘/’ ( root directory )
Path will not have whitespace characters.

'''
