gp = {'1':1, '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        #both of the to are positive
        num1,num2 =0,0
        p = len(A)-1
        for i in A:
            num1 += gp[i]*pow(10,p)
            p-=1
        p = len(B)-1
        for j in B:
            num2 += gp[j]*pow(10,p)
            p-=1
        return (num1*num2) 

if __name__=='__main__':

    B =Solution()
    n = int(input())
    for i in range(n):
        a = input()
        b = input()
        print (B.multiply(a,b))

'''      
MULTIPLY

Given two numbers represented as strings, return multiplication of the numbers as a string.

    Note: The numbers can be arbitrarily large and are non-negative.
    Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer. 

For example,
given strings "12", "10", your answer should be “120”.

NOTE : DO NOT USE BIG INTEGER LIBRARIES ( WHICH ARE AVAILABLE IN JAVA / PYTHON ).
We will retroactively disqualify such submissions and the submissions will incur penalties.
'''
