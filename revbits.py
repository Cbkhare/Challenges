class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        A = bin(A)[2:]
        I = list('0'*(32-len(A))+A)
        I.reverse()
        I = ''.join(I)
        return (int(I,2))
        #if done via shifting bit
        '''
        def reverse(self, A):
        i = 31
        ret = 0
        while i >= 0:
            temp = ((A & 1<<i) >> i)&1
            ret = ret | temp << (31-i)
            i -= 1
        return ret'''

      
    
if __name__=='__main__':
    B = Solution()
    n = int(input())
    #c  = tuple(map(int,input().split(' ')))
    for i in range(n):
        #c1  = tuple(map(int,input().split(' ')))
        m = int(input())
        print (B.reverse(m))
    

'''
REVBITS

Reverse bits of an 32 bit unsigned integer

Example 1:

x = 0,

          00000000000000000000000000000000  
=>        00000000000000000000000000000000

return 0

Example 2:

x = 3,

          00000000000000000000000000000011 
=>        11000000000000000000000000000000

return 3221225472

Since java does not have unsigned int, use long
'''
