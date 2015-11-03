class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        A.sort(key = lambda s: len(s))
        tm = ''
        if len(A)==1: return A[0]
        for i in range(len(A[0])):
            for x in range(i,len(A[0])):
                t = A[0][i:x+1]
                stat = 'free'
                for st in A[1:]:
                    if t not in st:
                        stat = 'midbreak'
                        break
                if len(t)> len(tm) and stat == 'free':
                    tm = t
            
        return (tm)

if __name__=='__main__':

    B =Solution()
    print (B.longestCommonPrefix(input().split(' ')))

'''


Write a function to find the longest common prefix string amongst an array of strings.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

As an example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".

Given the array of strings, you need to find the longest S which is the prefix of ALL the strings in the array.

Example:

Given the array as:

[

  "abcdefgh",

  "aefghijk",

  "abcefgh"
]

The answer would be “a”.

poesas tesap mesale
esa

'''
