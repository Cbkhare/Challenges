class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A)==0: return 0
        i = 1
        count = 1
        d = A[0]
        for j in range(1,len(A)):
            if A[j]!=d:
                A[i]=A[j]
                d = A[j]
                i+=1
                count+=1 
        return count
      
'''

    Asked in:  
    United Healthgroup
    Amazon
    Google
    Microsoft
    Expedia

Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.

Note that even though we want you to return the new length, make sure to change the original array as well in place

Do not allocate extra space for another array, you must do this in place with constant memory.

    Example:
    Given input array A = [1,1,2],
    Your function should return length = 2, and A is now [1,2]. 

'''
