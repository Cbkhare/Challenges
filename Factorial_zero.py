class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        c2,c5,i2,i5=A,A,0,0
        
        while c2/2>1:
            c2 = int(c2/2)
            i2+=c2
        
        while c5/5>1:
            c5 = int(c5/5)
            i5+=c5

        if i2>=i5:
            return i5+1
        else:
            return i2+1
            
            
        '''
        z = str(factorial(A))
        c= 0
        while z[::-1][c]=='0':
            c+=1
        yield c
        '''
if __name__=='__main__':

    B =Solution()
    print (B.trailingZeroes(int(input())))
        
'''


Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Example :

n = 5
n! = 120 
Number of trailing zeros = 1
So, return 1


'''
