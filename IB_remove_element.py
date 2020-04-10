class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        l = len(A)
        i = 0 
        j = 0
        count = 0
        for j in range(l):
            if A[j] != B:
                A[i]=A[j]
                i+=1
            elif A[j] == B:
                count +=1 
        return l-count
       
       
       '''
       
Remove Element from Array

    Asked in:  
    Amazon

Remove Element

Given an array and a value, remove all the instances of that value in the array.
Also return the number of elements left in the array after the operation.
It does not matter what is left beyond the expected length.

    Example:
    If array A is [4, 1, 1, 2, 1, 3]
    and value elem is 1,
    then new length is 3, and A is now [4, 2, 3] 

Try to do it in less than linear additional space complexity.
'''
