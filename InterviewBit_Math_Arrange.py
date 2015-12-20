from math import floor 
class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        for i in range(len(A)):
            A[i] = A[i] + (A[A[i]]%len(A))*len(A)
        for j in range(len(A)):
            A[j] = A[j]/len(A)



if __name__=='__main__':
    B = Solution()
    n = int(input())
    #c  = tuple(map(int,input().split(' ')))
    for i in range(n):
        c  = list(map(int,input().split(' ')))
        #m = int(input())
        #c = input()
        print (B.arrange(c))
    

'''
ARRANGE

Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

Example:

Input : [1, 0]
Return : [0, 1]

    Lets say N = size of the array. Then, following holds true :
    * All elements in the array are in the range [0, N-1]
    * N * N does not overflow for a signed integer 

'''
