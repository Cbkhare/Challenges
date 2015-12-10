class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        a = len(A)
        b = len(B)
        if a>b:
            B = '0'*(a-b)+B
        elif a<b:
            A = '0'*(b-a)+A
        #now a==b
        result = ''
        carry ='0' #carry
        for i in range(len(A)-1,-1,-1):
            if A[i]==B[i]=='0':
                if carry =='0':
                    result+='0'
                else:
                    result+='1'
                    carry ='0'
            elif A[i]==B[i]=='1':
                if carry=='0':
                    result+='0'
                else:
                    result+='1'
                carry ='1'
            elif A[i]!=B[i]:
                if carry=='0':
                    result+='1'
                else:
                    result+='0'
                    carry='1'
        if result.count('0')==len(result):  carry='1'
        result= (result+carry)[::-1]
        result = result[result.index('1'):]
        return result
            

        
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c1 = input()
        c2 = input()
        print (S.addBinary(c1,c2))
        

'''
ADDBINARY

Given two binary strings, return their sum (also a binary string).

Example:

a = "100"

b = "11"

Return a + b = “111”.

'''
