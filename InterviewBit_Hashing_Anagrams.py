from sys import stdin as si
from collections import Counter as C
from operator import itemgetter as ig
from functools import reduce 

class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        g= {}
        #logic : sum of ascii values of chars will always be unique 
        for j in range(len(A)):
            key = sum([ ord(i) for i in A[j]])
            g[key]=g.get(key,[])+[j+1]
        ans = sorted([v for k,v in g.items()])
        return ans
                    


if __name__ == "__main__":
    for i in range(int(si.readline())):
        A = si.readline().split()

        S = Solution()
        print (S.anagrams(A))
'''
Anagrams

Given an array of strings, return all groups of strings that are anagrams. Represent a group by a list of integers representing the index in the original list. Look at the sample case for clarification.

    Anagram : a word, phrase, or name formed by rearranging the letters of another, such as 'spar', formed from 'rasp' 

    Note: All inputs will be in lower-case. 

Example :

Input : cat dog god tca
Output : [[1, 4], [2, 3]]

cat and tca are anagrams which correspond to index 1 and 4.
dog and god are another set of anagrams which correspond to index 2 and 3.
The indices are 1 based ( the first element has index 1 instead of index 0).

    Ordering of the result : You should not change the relative ordering of the words / phrases within the group. Within a group containing A[i] and A[j], A[i] comes before A[j] if i < j. 

'''
