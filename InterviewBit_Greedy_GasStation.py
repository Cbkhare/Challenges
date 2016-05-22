from sys import stdin as Si, maxsize as m
from math import factorial as F,log as lg 
from  collections import Counter as C 
from operator import itemgetter as ig 

        
class Solution(object):
    
    def canCompleteCircuit(self, G, C):
        
        for i in range(len(G)):
            G[i] = G[i]-C[i]
        #print(G)
        if sum(G)<0:    return -1
        else:
            Sum = G[0]
            Index = 0
            for i in range(1,len(G)):
                if G[i]>0 and Sum<0:
                    Index = i
                if G[i]>Sum and Sum<0:    Sum=G[i]
                else:           Sum+=G[i]
            
        return Index


    
if __name__=='__main__':
    
    for i in range(int(Si.readline())):
        S=Solution()
        gas = list(map(int,Si.readline().split()))
        cost = list(map(int,Si.readline().split()))
        print (S.canCompleteCircuit(gas,cost))

'''

Checks:-
5
1 2 1 4 6 7 7 7 7 7
2 1 3 1 1 8 8 8 8 8
3
1 2
2 1
1
6 7 5 7 9 9
8 2 9 6 3 5
1



Gas Station

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the minimum starting gas station’s index if you can travel around the circuit once, otherwise return -1.

You can only travel in one direction. i to i+1, i+2, ... n-1, 0, 1, 2..
Completing the circuit means starting at i and ending up at i again.

Example :

Input :
      Gas :   [1, 2]
      Cost :  [2, 1]

Output : 1 

If you start from index 0, you can fill in gas[0] = 1 amount of gas. Now your tank has 1 unit of gas. But you need cost[0] = 2 gas to travel to station 1. 
If you start from index 1, you can fill in gas[1] = 2 amount of gas. Now your tank has 2 units of gas. You need cost[1] = 1 gas to get to station 0. So, you travel to station 0 and still have 1 unit of gas left over. You fill in gas[0] = 1 unit of additional gas, making your current gas = 2. It costs you cost[0] = 2 to get to station 1, which you do and complete the circuit. 

'''
