from operator import itemgetter as ig
from sys import stdin as Si


    
if __name__=='__main__':

    n = int(Si.readline())
    for i in range(n):
        h = {}
        s = Si.readline().strip()
        for j in range(len(s)):
            h[ord(s[j])] = h.get(ord(s[j]),0)+1
        ans = min([k for k in h  if h[k]==max(h.values())])
        print (chr(ans), h[ans])


'''
Maximum occurrence
Attempted by: 1527
/
Accuracy: 84%
/
Tag(s):
Ad-Hoc, Basic Programming, Easy
Problem
Editorial
My Submissions
Analytics
Zomato Hiring Challenge

You are given a string which comprises of lower case alphabets (a-z), upper case alphabets (A-Z), numbers, (0-9) and special characters like !,-.; etc.

You are supposed to find out which character occurs the maximum number of times and the number of its occurrence, in the given string. If two characters occur equal number of times, you have to output the character with the lower ASCII value.

For example, if your string was: aaaaAAAA, your output would be: A 4, because A has lower ASCII value than a.

Input format:
The input will contain a string.

Output format:
You've to output two things which will be separated by a space:
i) The character which occurs the maximum number of times.
ii) The number of its occurrence.

Constraints:
The maximum length of the string can be 1000.
SAMPLE INPUT

Pulkit is a dog!!!!!!!!!!!!

SAMPLE OUTPUT

! 12


'''
