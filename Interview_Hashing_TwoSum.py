class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        gp = {}
        for i in range(len(A)):
            if A[i] in gp:
                return [gp[A[i]],i]     #for non-zero based list [gp[A[i]]+1,i+1]
            else:
                if B-A[i] not in gp:    gp[B-A[i]]=i        #to return lowest
        return None
          
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c= list(map(int,input().split(' ')))
        c1 = int(input())
        print (S.twoSum(c,c1))


      


'''
2SUM

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2. Please note that your returned answers (both index1 and index2 ) are not zero-based.
Put both these numbers in order in an array and return the array from your function ( Looking at the function signature will make things clearer ). Note that, if no pair exists, return empty list.

If multiple solutions exist, output the one where index2 is minimum. If there are multiple solutions with the minimum index2, choose the one with minimum index1 out of them.

Input: [2, 7, 11, 15], target=9
Output: index1 = 1, index2 = 2

'''
