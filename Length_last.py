class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        while len(A.split(' ')[-1])==0:
            if A=='': break
            A=A[:-1]
        return len(A.split(' ')[-1])
        '''
        time complexity lost
        #last = A.split(' ')[-1]
        lst = A.split(' ')
        while '' in lst: lst.remove('')
        if len(lst) == 0:
            return 0
        else:
            return len(lst[-1])
        '''
        
        

if __name__=='__main__':

    B =Solution()
    n = int(input())
    for i in range(n):
        print (B.lengthOfLastWord(input()))
        
'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Given s = "Hello World",

return 5 as length("World") = 5.

Please make sure you try to solve this problem without using library functions. Make sure you only traverse the string once.
'''
