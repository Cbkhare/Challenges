class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        stack = []
        word_stack = []
        if ' ' not in A: return A
        for letrs in list(A):
            if letrs==' ':
                stack.append(''.join(word_stack))
                word_stack = []
                continue
            word_stack.append(letrs)
        stack.append(''.join(word_stack))
        while '' in stack:
            stack.remove('')
        stack.reverse()
        return (stack)



        
if __name__=='__main__':

    B =Solution()
    print (B.reverseWords(input()))
        
'''


Given an input string, reverse the string word by word.

Example:

Given s = "the sky is blue",

return "blue is sky the".

        A sequence of non-space characters constitutes a word.
        Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
        If there are multiple spaces between words, reduce them to a single space in the reversed string.

'''
