class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        i = 0
        j = i
        while i<len(A)-1:
            j=i+1
            if A[i]==B:
                A =A[:i]+A[j:]
            else:
                i+=1
        return len(A),A
               
            
            
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c = list(map(int,input().split(' ')))
        c1 = int(input())
        print (S.removeElement(c,c1))


'''
REMELM

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
