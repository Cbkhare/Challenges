from sys import maxint
class Solution:
    # @param A : integer
    # @return an integer
    
    def reverse(self, A):
        x=0
        #if A.bit_length() >32: return 0
        if A >= 0:
            A=list(str(A))
            A.reverse()
            x= int(''.join(A))
        else:
            A=list(str(A))
            A.pop(0)
            A.reverse()
            A=['-'] + A
            x= int(''.join(A))
        #if  -2147483647> x or x> 2147483647:    #Max & Min range of 32 bit signed int
        if x.bit_length() >32:
            return 0
        else:
            return x
B = Solution()
print B.reverse(int(raw_input()))



'''


Reverse digits of an integer.

Example1:

x = 123,

return 321
Example2:

x = -123,

return -321

Return 0 if the result overflows and does not fit in a 32 bit signed integer

'''
