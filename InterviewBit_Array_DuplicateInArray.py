from sys import stdin as si
from math import sqrt; from itertools import count, islice
from sys import maxsize as m

class Solution(object):
    
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        A= [ i for i in A]
        for i in range(len(A)):
            index = abs(A[i])-1
            if A[index]<0:  return abs(A[i])
            else:
                A[index] *= -1
        else:
            return  -1

        
    
        
if __name__=="__main__":
    n = int(si.readline())
    for i in range(n):
        S = Solution()
        a = list(map(int, si.readline().split()))
        print (S.repeatedNumber(a))
        
    
    
'''
Find Duplicate in Array

Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times.

Sample Input:

[3 4 1 4 1]

Sample Output:

1

If there are multiple possible answers ( like in the sample case above ), output any one.

If there is no duplicate, output -1
'''
