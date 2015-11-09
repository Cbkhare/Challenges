class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        s = 0
        e = len(A)-1
        found = False 
        #first occurence
        x1 = 0
        while s<=e:
            m = int((s+e)/2)
            if A[m]==B:
                found = True   #proof that atleast the element exist 
                x1 = m
                e = m-1
            elif A[m]>B:     #less than 1 st limit 
                e = m-1
            elif A[m]<B:   #less than last element 
                s = m+1

        x2 = 0
        s = 0
        e = len(A)-1
        while s<=e:
            m = int((s+e)/2)
            if A[m]==B:
                x2 = m
                s = m+1
            elif A[m]>B:     #less than 1 st limit 
                e = m-1
            elif A[m]<B:   #less than last element 
                s = m+1
        if found:
            return [x1,x2]
        else: return [-1,-1]

if __name__=='__main__':

    B =Solution()
    n = int(input())
    c = list(map(int,input().split(' ')))
    for i in range(n):
        b = int(input())
        print (B.searchRange(c,b))

'''
iven a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm’s runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example:

Given [5, 7, 7, 8, 8, 10]

and target value 8,

return [3, 4].
'''
