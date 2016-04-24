from sys import stdin as Si 

class Solution(object):   
            
    def grayCode(self,n):
        if n==0:    return [0]
        elif n==1:  return [0,1]
        else:
            return self.grayCode(n-1)+[(2**(n-1)+x) for x in self.grayCode(n-1)[::-1]]       



if __name__=='__main__':

    n = int(Si.readline())
    S = Solution()
    print (S.grayCode(n))
    
'''


The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2

There might be multiple gray code sequences possible for a given n.
Return any such sequence.

'''
