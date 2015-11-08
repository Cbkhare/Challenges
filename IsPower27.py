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

class Solution:
    # @param A : integer
    # @return a boolean
    def isPower(self, A):
        if A==1: return 1
        for i in xrange(2,100):   #power
            for j in xrange(1,int(A/2)+1): #base
                if pow(j,i)==A:
                    return True
                elif pow(j,i)>A:
                    break
        return False

B = Solution()
print B.isPower(int(raw_input()))
