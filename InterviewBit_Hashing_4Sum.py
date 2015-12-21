from itertools import combinations as C
class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def hash4sum(self,A,B):
        gp= {}
        A.sort()
        stack = []
        i,l= 0,len(A)-1
        sup = []
        while l-i>=3:
            j,k=i+1,l-1
            prev_Sum = 0
            while j<k:
                #print (A[i],A[j],A[k],A[l])
                Sum = A[i]+A[j]+A[k]+A[l]
                if Sum<B:
                    j+=1
                elif Sum>B:
                    k-=1
                elif Sum==B:
                    if [A[i],A[j],A[k],A[l]] not in sup:    sup.append([A[i],A[j],A[k],A[l]])
                    j+=1
                    k-=1
                if j<k: prev_Sum = Sum
            #print (Sum,prev_Sum,i,j,k,l)
            if prev_Sum>=B:  #prev_Sum>B:   l-=1        #last sum
                l-=1
            elif prev_Sum<B:    # prev_Sum<B: i+=1
                i+=1
                l = len(A)-1
        return sorted(sup)
            
          
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c= list(map(int,input().split(' ')))
        c1 = int(input())
        print (S.hash4sum(c,c1))

'''
4SUM

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

    Note:

        Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
        The solution set must not contain duplicate quadruplets.

Example :
Given array S = {1 0 -1 0 -2 2}, and target = 0
A solution set is:

    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
    (-1,  0, 0, 1)

Also make sure that the solution set is lexicographically sorted.
Solution[i] < Solution[j] iff Solution[i][0] < Solution[j][0] OR (Solution[i][0] == Solution[j][0] AND ... Solution[i][k] < Solution[j][k])
'''
