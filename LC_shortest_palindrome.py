class Solution:
    def shortestPalindrome(self, s: str) -> str:
        l = len(s)
        if l<2:
            return s 
        max_len_of_palindrome = 1
        for i in range(1, len(s)):
            if s[:i+1]==s[:i+1][::-1]:
                max_len_of_palindrome = i + 1
        words = s[::-1][:l-max_len_of_palindrome]
        return words + s
