from sys import stdin as si
from collections import Counter as C
from operator import itemgetter as ig
from functools import reduce 
from sys import maxsize as m

class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        i,j=0,len(A)-1
        A=A.lower()
        while i<=j:
            while ord(A[i]) not in range(48,58) \
               and ord(A[i]) not in range(97,123):
                i+=1
            while ord(A[j]) not in range(48,58) \
               and ord(A[j]) not in range(97,123):
                j-=1
            if i>len(A)-1 or j<0:   return False
            if A[i]==A[j]:
                i+=1
                j-=1
            else:
                return False
        else:
            return True


        

if __name__ == "__main__":
    for i in range(int(si.readline())):
        A = si.readline().strip()
        S = Solution()
        print (S.isPalindrome(A))


'''
Palindrome String

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example:

"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''
