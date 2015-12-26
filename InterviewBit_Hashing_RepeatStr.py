class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        lastRepeating = -1
        longestSubstring = 0
        positions = {}
        for i in range(0, len(A)):
            #print (positions,lastRepeating)
            if A[i] in positions and lastRepeating<positions[A[i]]:
                lastRepeating = positions[A[i]]
            if i-lastRepeating > longestSubstring:
                longestSubstring = i-lastRepeating
            positions [A[i]]=i
        return longestSubstring
            
          
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        #c= list(map(int,input().split(' ')))
        c = input()
        print (S.lengthOfLongestSubstring(c))

      


'''
REPEATSTR

Given a string,
find the length of the longest substring without repeating characters.

Example:

The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

For "bbbbb" the longest substring is "b", with the length of 1.
'''
