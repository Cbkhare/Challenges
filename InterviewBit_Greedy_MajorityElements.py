from sys import stdin as Si, maxsize as m
from math import factorial as F,log as lg 
from  collections import Counter as C 
from operator import itemgetter as ig 

        
class Solution:

    def majorityElement(self,A):
        N = C(A)
        return (max(N.items(),key=ig(1))[0])
        

if __name__=='__main__':
    S=Solution()
    for i in range(int(Si.readline())):
        a = list(map(int,Si.readline().split()))
        print (S.majorityElement(a))


'''


Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example :

Input : [2, 1, 2]
Return  : 2 which occurs 2 times which is greater than 3/2. 


'''
