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
        s1= tuple(s[i]-s[i-1] for i in range(1,len(s)))
        print (S.maxSum(s1))

'''
Maximum difference between 2 element in an Array

100 180 260 310 40 535 695
655

1 2 3 4 5
4

step 1:- Make an list with difference of adjacent element in the iven list.
step 2:- Maximize the Sum of the List obtained from step 1.
         Apply DP in step 2.
'''
