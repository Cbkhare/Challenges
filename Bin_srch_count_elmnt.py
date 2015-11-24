class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):

        found = False
        s,e = 0,len(A)-1,
        while not found:
            m = int((s+e)/2)
            #print (s,e,m)
            if s>e: break
            if A[m]==B:
                found = True
            elif A[m]<B:
                s = m+1
            elif A[m]>B:
                e = m-1
        if found == True:
            l = m-1
            while l >= 0:
                if A[l]!=B:      #B=A[m]
                    break
                l-=1
            n = l+1
            while n<len(A):
                if A[n]!=B:
                    break
                n+=1                
            return (n-1)-l
        else:
            return 0
            

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
return 2.'''
