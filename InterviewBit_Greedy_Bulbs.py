from sys import stdin as Si, maxsize as m
from math import factorial as F
import collections 

class Solution:
    def bulbs(self,A):
        T = 0
        change = False
        for i in range(len(A)):
            if change:
                A[i] = 1-A[i]
            if A[i]==0:
                A[i]==1
                change=not(change)   #applying negtion
                T+=1
        return T 
                



if __name__=='__main__':
    S=Solution()
    for i in range(int(Si.readline())):
        a = list(map(int,Si.readline().split()))
        print (S.bulbs(a))

'''
Bulbs

N light bulbs are connected by a wire. Each bulb has a switch associated with it, however due to faulty wiring, a switch also changes the state of all the bulbs to the right of current bulb. Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs. You can press the same switch multiple times.

Note : 0 represents the bulb is off and 1 represents the bulb is on.

Example:

Input : [0 1 0 1]
Return : 4

Explanation :
	press switch 0 : [1 0 1 0]
	press switch 1 : [1 1 0 1]
	press switch 2 : [1 1 1 0]
	press switch 3 : [1 1 1 1]


'''
