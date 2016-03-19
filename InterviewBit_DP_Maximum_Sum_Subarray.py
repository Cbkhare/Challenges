class Solution:

    def maxSum(self,A):
        r = A[0]
        mins = A[0]
        maxs = A[0]
        for a in A[1:]:
            t_mins = mins
            t_maxs = maxs
            maxs = max(max(t_mins+a,t_maxs+a),a)
            mins = min(min(t_mins+a,t_maxs+a),a)
            r = max(r,maxs)
        return r 
        
            
        
if __name__=='__main__':
    S = Solution()
    n = int(input())
    for i in range(n):
        s = tuple(map(int,input().split(' ')))
        print (S.maxSum(s))


'''
Maximum Sum Sub-Array
'''
