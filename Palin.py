#import cProfile
#import pstats
class Solution:
    # @param A : integer
    # @return next palindrome Int
    def next_palindrome(self,A):
        if A==9009: print (9119)
        P = int(A) + 1
        stat = False
        while not stat:
            if str(P) == str(P)[::-1]:
                return P
            else:
                P += 1 
    
if __name__ == '__main__':

    B = Solution()
    n = int(input())

    for i in range(n):
        print (B.next_palindrome(input()))

'''


A positive integer is called a palindrome if its representation in the decimal system is the same when read from left to right and from right to left. For a given positive integer K of not more than 1000000 digits, write the value of the smallest palindrome larger than K to output. Numbers are always displayed without leading zeros.
Input

The first line contains integer t, the number of test cases. Integers K are given in the next t lines.
Output

For each K, output the smallest palindrome larger than K.
Example

Input:
2
808
2133

Output:
818
2222

Warning: large Input/Output data, be careful with certain languages
'''

'''
    def check_palindrome(self, C):
        if str(C) == str(C)[::-1]:
            return True
        else:
            return False
        
    def next_palindrome(self,A):
        P = int(A) + 1
        while self.check_palindrome(P) != 1:
            P += 1
        return P
'''

'''
Palindrome reverse int
    while x>0:
	d = x%10
	z = z*10+d
	x= int((x-d)/10)
	i +=1
	print (d,z,x,i)
'''
'''
    def next_palindrome(self,A):
        if A.count('9')==len(A):                                                    #all no. are nine
            return (int(A)+2)            
        if len(A)==1: return (int(A)+1)                                             #only single digit
        if len(A)%2==0:           #i.e Even len num
            if int(A[:int(len(A)/2)][::-1]) > int(A[int(len(A)/2):]):               #143(341)-309
                return (int( A[:int(len(A)/2)] + A[:int(len(A)/2)][::-1] ))         #143-431
            
            elif int(A[:int(len(A)/2)][::-1]) <= int(A[int(len(A)/2):]):            #143-341, 143-619
                A = A[:int(len(A)/2)-1] + str(int(A[:int(len(A)/2)][-1])+1)         #144-441  (14-3+1)
                return (int(A+A[::-1]))
        else:                          #i.e odd len num
            if int(A[:int(len(A)/2)][::-1]) > int(A[int(len(A)/2)+1:]):             #143(341)-9-309
                return (int( A[:int(len(A)/2)+1] + A[:int(len(A)/2)][::-1] ))       #143-9-341
            
            elif int(A[:int(len(A)/2)][::-1]) <= int(A[int(len(A)/2)+1:]):          #143-9-619, 143-5-619
                An = A[:int(len(A)/2)-1] + str(int(A[:int(len(A)/2)][-1])+1)        #14-3+1
                M = str(int(A[int(len(A)/2)])+1)[-1]                                #only last digit of sum 10->0,5-5,
                return (int(An+M+An[::-1]) )                                        #14-4-0-441
  
'''
   
