class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A)==1: return 1
        i =0
        while i< len(A)-1:
            j = i+1
            if A[i]==A[j]:
                A = A[:i]+A[j:]
            else:
                i=j
        return len(A),A

                
        
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c = list(map(int,input().split(' ')))
        print (S.removeDuplicates(c))


'''
REMDUP

Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.

Note that even though we want you to return the new length, make sure to change the original array as well in place

Do not allocate extra space for another array, you must do this in place with constant memory.

    Example:
    Given input array A = [1,1,2],
    Your function should return length = 2, and A is now [1,2]. 


'''
