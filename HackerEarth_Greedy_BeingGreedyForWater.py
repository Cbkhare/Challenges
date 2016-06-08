from operator import itemgetter as ig
from sys import stdin as Si,maxsize as Ms
from itertools import chain
    
if __name__=='__main__':

    n = int(Si.readline())
    for i in range(n):
        N,X = map(int,Si.readline().split())
        B = sorted(map(int,Si.readline().split()))
        count,t = 0,0
        for x in B:
            t+=x
            if t>X:    break
            else: count+=1
        print(count)
 

'''

Being greedy for Water

You are given container full of water. Container can have limited amount of water. You also have N

bottles to fill. You need to find the maximum numbers of bottles you can fill.

Input:
First line contains one integer, T
, number of test cases.
First line of each test case contains two integer, N and X, number of bottles and capacity of the container.
Second line of each test case contains N

space separated integers, capacities of bottles.

Output:
For each test case print the maximum number of bottles you can fill.

Constraints:
1≤T≤100

1≤N≤104
1≤X≤109
1≤capacitiesofbottles≤106

SAMPLE INPUT

1
5 10
8 5 4 3 2

SAMPLE OUTPUT

3


'''
