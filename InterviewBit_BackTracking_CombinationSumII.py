from sys import stdin as Si, maxsize as m
from math import factorial as F,log as lg 
from  collections import Counter as C 
from operator import itemgetter as ig 

        
class Solution:

    def __init__(self):
        self.torture =[] 

    def bazinga(self,C,T,i,CC):
        for j in range(i,len(C)):
            if C[j]==T:
                Ans = sorted(CC+[C[j]])
                if Ans not in self.torture: self.torture.append(Ans)
            if C[j]>T:
                continue
            else:
                self.bazinga(C,T-C[j],j+1,CC+[C[j]])

                
                
    def combinationSum2(self, C, T):
        CC=[]
        self.bazinga(C,T,0,CC)
        return self.torture

        
if __name__=='__main__':
    
    for i in range(int(Si.readline())):
        S=Solution()
        candidate = list(map(int,Si.readline().split()))
        target = int(Si.readline())
        print (S.combinationSum2(candidate,target))

'''
Combination Sum II

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

    Note:

        All numbers (including target) will be positive integers.
        Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
        The solution set must not contain duplicate combinations.

Example :

Given candidate set 10,1,2,7,6,1,5 and target 8,

A solution set is:

[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]


'''
