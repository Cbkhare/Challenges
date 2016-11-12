from sys import stdin as si
from collections import Counter as C
from operator import itemgetter as ig
from functools import reduce 
from sys import maxsize as m

class Solution:
    # @param n : integer
    # @param k : integer
    # @return a list of list of integers

    def __init__(self):
        self.A = []
        
    def combine(self, n, k):
        if n==k:
            self.A.append([i for i in range(1,n+1)])
            return self.A 
        else:
            self.combine(n-1,k)
            temp = [] 
            for l in self.A:
                for x in range(len(l)):
                    #replacing every index with [n]
                    t = sorted(l[:x]+[n]+l[x+1:])
                    if t in temp: continue 
                    temp.append(t)
            self.A.extend(temp)
        return sorted(self.A)
        
        
        

if __name__ == "__main__":
    for i in range(int(si.readline())):
        #x,y = map(int,si.readline().split())
        #A = list(map(int,si.readline().split(' ')))
        n,k = map(int,si.readline().split())
        #A = [ i for i in range(100)]
        #A = si.readline().split()
        #A = si.readline().strip()
        #A = si.readline()
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
        print (S.combine(n,k))

'''
Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.

Make sure the combinations are sorted.

To elaborate,
1. Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
2. Entries should be sorted within themselves.

Example :
If n = 4 and k = 2, a solution is:

[
  [1,2],
  [1,3],
  [1,4],
  [2,3],
  [2,4],
  [3,4],
]

    Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
    Example : itertools.combinations in python.
    If you do, we will disqualify your submission retroactively and give you penalty points. 


'''
