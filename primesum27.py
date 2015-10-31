'''from sys import argv
import re, math, ast

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n') for line in fp]
content = [item.split(' ') for item in contents]
#for i in range(0,8):
 #   contents = fp.readline().split()
print (contents)
'''

from itertools import permutations
class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        np = [] 
        p = []
        #l = int(A**0.5)
        for i in xrange(2,A):
            if i not in np:
                p.append(i)
                #np += list(xrange(i,li,i))
                li = int(A/i)
                for po in xrange(1,li+1):
                    if i*po <=A:
                        np.append(i*po)
                    else:
                        break
        if len(p)==1: p=p*2
        stack = []
        for n in p:
            if n*2 ==A:
                stack.append([n]*2)
        s = permutations(p,2)
        for t in s:
            t = list(t)
            if sum(t)==A:
                t.sort()
                stack.append(t)
        stack.sort()
        if stack !=[]:
            return stack[0]
        else:
            return []

B = Solution()
print B.primesum(int(raw_input()))


'''


Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

NOTE A solution will always exist. read Goldbach’s conjecture

Example:


Input : 4
Output: 2 + 2 = 4

If there are more than one solutions possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b,
and [c,d] is another solution with c <= d, then

[a, b] < [c, d] 

If a < c OR a==c AND b < d. 

'''
