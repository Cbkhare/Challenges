class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A)==1: return 1
        i =0
        count = 1
        tar = 0
        while i< len(A)-1:
            j = i+1
            if count==2 and A[i]==A[j]:
                #A = A[:i]+A[j:]
                del A[i]
            elif A[i]==A[j] and count<2:
                count+=1
                tar+=1
                i+=1
            elif A[i]!=A[j]:
                count = 1
                tar+=1
                i+=1
        return tar+1,len(A),A
             
            
if __name__=='__main__':
    n = int(input())
    for i in range(n):\
        S = Solution()
        c = list(map(int,input().split(', ')))
        print (S.removeDuplicates(c))


'''
REMDUP2

Remove Duplicates from Sorted Array

Given a sorted array, remove the duplicates in place such that each element appear atmost twice and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

Note that even though we want you to return the new length, make sure to change the original array as well in place

For example,
Given input array A = [1,1,1,2],

Your function should return length = 3, and A is now [1,1,2].


'''
