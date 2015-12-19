chr_dict = {}
for i in range(1,27):
    chr_dict[chr(64+i)]=i

class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        i = len(A)-1
        c = 0
        for j in range(len(A)):
            c += pow(26,i)*chr_dict[A[j]]
            i-=1
        return c

if __name__=='__main__':
    B = Solution()
    n = int(input())
    #c  = tuple(map(int,input().split(' ')))
    for i in range(n):
        #c  = tuple(map(int,input().split(' ')))
        #m = int(input())
        c = input()
        print (B.titleToNumber(c))
    

'''


Given a column title as appears in an Excel sheet, return its corresponding column number.

Example:

    A -> 1
    
    B -> 2
    
    C -> 3
    
    ...
    
    Z -> 26
    
    AA -> 27
    
    AB -> 28 

'''
