from sys import stdin as si
from collections import Counter as C
from operator import itemgetter as ig
from functools import reduce 
from sys import maxsize as m

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
     
    def sub(self, A):
        if A==[]:
            return []
        elif len(A)==1:
            return [A]
        else:
            f = A[0]
            stack = [[f]]
            r = self.sub(A[1:])
            for l in r:
                t = sorted(l+[f])
                stack.append(t)
                stack.append(l)
            return sorted(stack)

    def subsets(self,A):   #only to addd []
        ans = [[]]
        ans += [i for i in self.sub(sorted(A))]
        return ans 
        
    def offical_subsets(self, s): #official solutions
        s.sort()
        r = [[]]
        for e in s:
            r += [x+[e] for x in r]
        return sorted(r)
        

if __name__ == "__main__":
    for i in range(int(si.readline())):
        #x,y = map(int,si.readline().split())
        A = list(map(int,si.readline().split(' ')))
        #n = int(input())
        #A = [ i for i in range(100)]
        #A = si.readline().split()
        #A = si.readline().strip()
        '''
        A = [A[j] for j in range(0,len(A),y)
        B = []
        for j in range(x):
            t= []
            for k in range(y):
                t.append(A.pop(0))
            B.append(t)
        '''
        S = Solution()
        print (S.subsets(A))


'''

Subset 

Given a set of distinct integers, S, return all possible subsets.

    Note:

        Elements in a subset must be in non-descending order.
        The solution set must not contain duplicate subsets.
        Also, the subsets should be sorted in ascending ( lexicographic ) order.
        The list is not necessarily sorted.

Example :

If S = [1,2,3], a solution is:

[
  [],
  [1],
  [1, 2],
  [1, 2, 3],
  [1, 3],
  [2],
  [2, 3],
  [3],
]

'''
