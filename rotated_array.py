class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        l = len(A)
        s,e,m = 0, l-1, 0
        
        while s<=e:
            if A[s]<= A[e]: return A[s]
            m = int(s + int((e-s)/2))
            nex = (m+1)%l
            prev = (m+l-1)%l
            #print (A[prev],A[m],A[nex])
            if   A[prev]>= A[m]<=A[nex]:      #like 8-2-3
                return A[m]
            elif A[m]<=A[e]:
                e = m-1
            elif A[m]>= A[s]:
                s = m+1
        return -1
                

if __name__=='__main__':

    B =Solution()
    n = int(input())
    for i in range(n):
        a = tuple(map(int,input().split(' ')))
        print (B.findMin(a))
        
'''
ROTATEDARRAY

Suppose a sorted array A is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array will not contain duplicates.

        NOTE 1: Also think about the case when there are duplicates. Does your current solution work? How does the time complexity change?*

PROBLEM APPROACH:

Note: If you know the number of times the array is rotated, then this problem becomes trivial. If the number of rotation is x, then minimum element is A[x].
Lets look at how we can calculate the number of times the array is rotated.
'''
