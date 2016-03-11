class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def get(self,a,b,c):
        return max(abs(a-b),abs(b-c),abs(c-a))
    
    def minimize(self, A, B, C):
        i,j,k=0,0,0
        mv = None           #min value 
        while i<len(A) and j<len(B) and k<len(C):
            cmv = self.get(A[i],B[j],C[k])      #current min value 
            if mv == None or cmv < mv:
                mv = cmv
            if min(A[i], B[j], C[k]) == A[i]:
                i += 1
            elif min(A[i], B[j], C[k]) == B[j] :
                j += 1
            else :
                k += 1
        return mv
            

        
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c = list(map(int,input().split(' ')))
        c1 = list(map(int,input().split(' ')))
        c2 = list(map(int,input().split(' ')))
        print (S.minimize(c,c1,c2))
        

'''


You are given 3 arrays A, B and C. All 3 of the arrays are sorted.

Find i, j, k such that :
max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))

**abs(x) is absolute value of x and is implemented in the following manner : **

      if (x < 0) return -x;
      else return x;

Example :

Input : 
        A : [1, 4, 10]
        B : [2, 15, 20]
        C : [10, 12]

Output : 5 
         With 10 from A, 15 from B and 10 from C. 

'''
