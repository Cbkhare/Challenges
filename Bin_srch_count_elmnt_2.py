class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):

        found = False
        s,e,m = 0,len(A)-1,0

        #Binary search to find first occurence
        while s<=e:
            m = int((s+e)/2)
            #print (s,e,m)
            
            if A[m]==B:
                e = m-1    #diff
            elif A[m]<B:
                s = m+1
            elif A[m]>B:
                e = m-1
        s,e,n = 0,len(A)-1,0
        #Binary search to find last occurence
        while s<=e:
            n = int((s+e)/2)
            #print (s,e,n)
            
            if A[n]==B:
                s = n+1
            elif A[n]<B:
                s = n+1
            elif A[n]>B:
                e = n-1
        return n-m        
            

if __name__=='__main__':

    B =Solution()
    n = int(input())
    for i in range(n):
        a = list(map(int,input().split(' ')))
        b = int(input())
        print (B.findCount(a,b))
        
'''
COUNTELEMENTS

Given a sorted array of integers, find the number of occurrences of a given target value.
Your algorithm’s runtime complexity must be in the order of O(log n).
If the target is not found in the array, return 0

**Example : **
Given [5, 7, 7, 8, 8, 10] and target value 8,
return 2
'''
