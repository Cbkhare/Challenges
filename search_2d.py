class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        s = 0
        e = len(A)-1

        #finding suitable tuple
        
        while s<=e:
            m = int((s+e)/2)
            if A[m][0]==B or A[m][len(A[m])-1]==B:   #best case 
                return 1
            elif A[m][0]<B<A[m][len(A[m])-1]:
                break
            elif A[m][0]>B:     #less than 1 st limit 
                e = m-1
            elif A[m][len(A[m])-1]<B:   #less than last element 
                s = m+1

        #finding the num in that tuple
        s1=0
        e1 = len(A[m])
        while s1<=e1:
            m1 = int((s1+e1)/2)
            if m1>len(A[m])-1: break
            if A[m][m1]==B:
                return 1
            elif A[m][m1]<B:
                s1 = m1+1
            elif A[m][m1]>B:
                e1 = m1-1
        return 0
    
'''         #time complexity lost 
            for tups in A:
            s= 0
            e = len(tups)-1

            while s<=e:
                m = int((s+e)/2)

                if tups[m]==B:
                    return 1
                elif tups[m]>B:
                    e = m-1
                elif tups[m]<B:
                    s = m +1
        return 0 
'''

if __name__=='__main__':

    B =Solution()
    n = int(input())
    for i in range(n):
        sup =[]
        t = int(input())
        for j in range(t):
            c = tuple(map(int,input().split(' ')))
            sup.append(c)
            #c = input()
        sup = tuple(sup)
        b = int(input())
        print (B.searchMatrix(sup,b))

'''
SEARCH2D

Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

        Integers in each row are sorted from left to right.

        The first integer of each row is greater than or equal to the last integer of the previous row.

Example:

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

Given target = 3, return 1 ( 1 corresponds to true )

Return 0 / 1 ( 0 if the element is not present, 1 if the element is present ) for this problem
'''
