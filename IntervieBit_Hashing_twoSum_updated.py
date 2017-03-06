from sys import stdin as si
from collections import Counter as C
from operator import itemgetter as ig 

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        ind = [] 
        g= {}
        for i in range(len(A)):
            if B-A[i] not in g: g[B-A[i]]=i

        for i in range(len(A)):
            if A[i] in g and i!=g[A[i]]:
                check = sorted([i,g[A[i]]])
                if check==ind:  continue
                else:
                    if ind==[]:
                        ind = check
                    else:
                        if check[1]<ind[1]:
                            ind = check
                        elif check[1]==ind[1] and check[0]<ind[0]:
                            ind = check
                
        if ind!=[]: return [ind[0]+1,ind[1]+1]
        return []
                
                    


if __name__ == "__main__":
    for i in range(int(si.readline())):
        A = list(map(int,si.readline().split(' ')))
        n = int(input())
        S = Solution()
        print (S.twoSum(A,n))


'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2. Please note that your returned answers (both index1 and index2 ) are not zero-based.
Put both these numbers in order in an array and return the array from your function ( Looking at the function signature will make things clearer ). Note that, if no pair exists, return empty list.

If multiple solutions exist, output the one where index2 is minimum. If there are multiple solutions with the minimum index2, choose the one with minimum index1 out of them.

Input: [2, 7, 11, 15], target=9
Output: index1 = 1, index2 = 2
'''
