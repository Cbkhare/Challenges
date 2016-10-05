from sys import stdin as si
from math import sqrt; from itertools import count, islice
from sys import maxsize as m

class Solution(object):
    
    def isPower(self, A):
        if A==1:    return True
        for i in range(2,100000):
            j=i
            while j<m/i:
                j*=i
                if j==A:    return True
        return False
    
        
if __name__=="__main__":
    n = int(si.readline())
    for i in range(n):
        S = Solution()
        a = int(si.readline())
        print (S.isPower(a))
        
    
    
        
'''


Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.

Example

Input : 4
Output : True  
as 2^2 = 4. 

'''
