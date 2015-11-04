class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    def strStr(self, haystack, needle):
        if needle == '':
            return -1
        else:
            if needle not in haystack:
                return -1
            else:
                return (haystack.index(needle))
    
        
if __name__ == '__main__':

    B = Solution()
    haystack, needle = input().split(' ')
    print (B.strStr(haystack, needle))


'''
STRSTR
Please Note:

Another question which belongs to the category of questions which are intentionally stated vaguely.
Expectation is that you will ask for correct clarification or you will state your assumptions before you start coding.

Implement strStr().

    strstr - locate a substring ( needle ) in a string ( haystack ). 

Try not to use standard library string functions for this question.

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

    NOTE:

    Good clarification questions:

        What should be the return value if the needle is empty?

        What if both haystack and needle are empty?

    For the purpose of this problem, assume that the return value should be -1 in both cases.
'''
