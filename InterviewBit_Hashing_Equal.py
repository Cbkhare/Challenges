from collections import defaultdict as dt 
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        d = dt(list)
        l = len(A)
        sol= []
        ans = []
        for i in range(l):
            for j in range(i+1,l):
                Sum = A[i]+A[j]
                if Sum in d and Sum not in sol:    sol+=[Sum,]
                d[Sum] += [(i,j),]
                if Sum in sol:
                    for s in d[Sum]:
                        if s==(i,j):    continue
                        else:   
                            x,y=s[0],s[1]
                            if x==i or y==j or x==j or y==i:    continue
                            if ans ==[]:    ans=[x,y,i,j]
                            else:   ans = min([x,y,i,j],ans)
                    
        #print(sol,'\n',d,ans)
        if sol==[]:  return sol
        else:
            return ans
                
if __name__=="__main__":
    n = int(stdin.readline())
    for i in range(n):
        lst = tuple(map(int,stdin.readline().split()))
        S = Solution()
        print(S.equal(lst))
    
'''


Given an array A of integers, find the index of values that satisfy A + B = C + D, where A,B,C & D are integers values in the array

Note:

1) Return the indices `A1 B1 C1 D1`, so that 
  A[A1] + A[B1] = A[C1] + A[D1]
  A1 < B1, C1 < D1
  A1 < C1, B1 != D1, B1 != C1 

2) If there are more than one solutions, 
   then return the tuple of values which are lexicographical smallest. 

Assume we have two solutions
S1 : A1 B1 C1 D1 ( these are values of indices int the array )  
S2 : A2 B2 C2 D2

S1 is lexicographically smaller than S2 iff
  A1 < A2 OR
  A1 = A2 AND B1 < B2 OR
  A1 = A2 AND B1 = B2 AND C1 < C2 OR 
  A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2

Example:

Input: [3, 4, 7, 1, 2, 9, 8]
Output: [0, 2, 3, 5] (O index)

If no solution is possible, return an empty list.

'''
