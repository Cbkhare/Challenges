class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        A = A-1
        if A ==0:
            return '1'
        elif A==1:
            return '11'
        elif A==2:
            return '21'
        
        s = '1211'
        for i in range(3,A):
            j = 0
            ns=''
            while j<=len(s)-1:
                c = 1
                x=j
                if x == len(s)-1:
                    ns += '1' + s[x]
                    break
                
                while s[x]==s[x+1]:
                    c+=1
                    x+=1
                    if x >=len(s)-1: break

                
                if c==1:
                    ns += '1'+ s[j]
                    j+=1
                else:
                    ns += str(c)+s[j]
                    j+=c
                print (i,s,ns,j,c)
            s = ns 
        return s
    

if __name__=='__main__':

    B =Solution()
    n = int(input())
    for i in range(n):
        a = int(input())
        print (B.countAndSay(a))
        
'''
COUNT_SAY

The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...

1 is read off as one 1 or 11.
11 is read off as two 1s or 21.

21 is read off as one 2, then one 1 or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Example:

if n = 2,
the sequence is 11.
'''        
                



