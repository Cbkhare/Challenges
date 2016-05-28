from sys import stdin as Si, maxsize as m
from math import factorial as F,log as lg 
from  collections import Counter as C 
from operator import itemgetter as ig 

        
class Solution:

    def __init__(self):
        self.torture =[] 

    def bazinga(self,C,T,CC):
        for c in C:
            if c==T:
                Ans = sorted(CC+[c])
                if Ans not in self.torture: self.torture.append(Ans)
            if c>T:
                continue
            else:
                self.bazinga(C,T-c,CC+[c])

                
    def combinationSum(self, C, T):
        CC=[]
        self.bazinga(C,T,CC)
        return sorted(self.torture)

        
if __name__=='__main__':
    
    for i in range(int(Si.readline())):
        S=Solution()
        candidate = list(map(int,Si.readline().split()))
        target = int(Si.readline())
        print (S.combinationSum(candidate,target))

'''
 Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:

[
  [7],
  [2, 2, 3]
]

'''
