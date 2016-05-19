from sys import stdin as Si, maxsize as m
from math import factorial as F,log as lg 
from  collections import Counter as C 
from operator import itemgetter as ig 

        
class Solution:

    def majorityElement(self,A):
        N = C(A)
        print (max(N.items(),key=ig(1))[0])
        

        
                

if __name__=='__main__':
    S=Solution()
    for i in range(int(Si.readline())):
        a = list(map(int,Si.readline().split()))
        print (S.majorityElement(a))

'''
Majority Element II
Total Accepted: 30106 Total Submissions: 115679 Difficulty: Medium

Given an integer array of size n, find all elements
that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.
'''
