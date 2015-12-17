from functools import reduce 
class Solution:
    # @param A : integer
    # @return an integer
            
    def colorful(self, A):
        gp_prod = {}
        A = str(A)
        for s in A:
            if int(s) not in gp_prod.values():
                gp_prod[s]=int(s)
            else:
                return 0
        for j in range(0,len(A)+1):
            for i in range(j+1,len(A)+1):
                #print (A[j:i])
                mul = reduce(lambda x,y:int(x)*int(y),A[j:i])
                if mul not in gp_prod.values():
                    gp_prod[A[j:i]]=mul
                else:
                    return 0
        return 1
        

        
            
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c = int(input())
        print (S.colorful(c))

'''      


For Given Number N find if its COLORFUL number or not

Return 0/1

COLORFUL number:

A number can be broken into different sub-sequence parts. 
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
And this number is a COLORFUL number, since product of every digit of a sub-sequence are different

Example:

N = 23
2 3 23
2 -> 2
3 -> 3
23 -> 6
this number is a COLORFUL number since product of every digit of a sub-sequence are different. 

Output : 1

'''
