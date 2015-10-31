class Solution:
    # @param A : integer
    # @return a list of integers
    def isPalindrome(self, A):
        A= list(str(A))
        A2 = A
        A2.sort(reverse=True)
        if A==A2:
            return True
        else:
            return False
        '''
        for i in xrange(0,int(len(A)/2)+1):
            if A[i]==A[len(A)-1-i]:
                continue
            else:
                return False
        return True
        '''
        

B = Solution()
print B.isPalindrome(int(raw_input()))

'''


Determine whether an integer is a palindrome. Do this without extra space.

A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
Negative numbers are not palindromic.

Example :

Input : 12121
Output : True

Input : 123
Output : False

'''
