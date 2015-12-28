class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        #inserting all element in hash
        gp = {i:'DontLev' for i in A}
        c = 0
        for k in gp:
            if gp[k]=='lev':    continue 
            ok = k
            t = 1
            #checking if a prev elemnt exist in gp
            if k-1 in gp:
                while k-1 in gp:
                    gp[k-1] = 'lev'
                    t+=1
                    k-=1
                k=ok
                while k+1 in gp:
                    gp[k+1] = 'lev'
                    t+=1
                    k+=1
            c = max(t,c)
        return c 
                        
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        c = list(map(int,input().split(' ')))
        S = Solution()
        print (S.longestConsecutive(c))
        


'''


Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Example:
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''
