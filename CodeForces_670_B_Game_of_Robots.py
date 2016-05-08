from sys import stdin as Si
from math import floor as F 
from collections import defaultdict as dt
from operator import itemgetter as ig
from math import pi 


if __name__== '__main__':
    N,k = map(int,Si.readline().split())
    Id  = list(map(int,Si.readline().split()))
    p = 0
    if k==1:        print(Id[0])
    elif 1<k<=3:    print(Id[:2][k%2])
    elif 3<k<=6:    print(Id[:3][k%3-1])
    else:
        n,p,lp=4,6,4
        while p<k:
            lp=p
            p = int(n*(n+1)/2)
            n+=1
        print(Id[:n][k-lp-1])

'''
B. Game of Robots
time limit per test
1 second
memory limit per test
256 megabytes
input
standard input
output
standard output

In late autumn evening n robots gathered in the cheerful company of friends. Each robot has a unique identifier — an integer from 1 to 109.

At some moment, robots decided to play the game "Snowball". Below there are the rules of this game. First, all robots stand in a row. Then the first robot says his identifier. After that the second robot says the identifier of the first robot and then says his own identifier. Then the third robot says the identifier of the first robot, then says the identifier of the second robot and after that says his own. This process continues from left to right until the n-th robot says his identifier.

Your task is to determine the k-th identifier to be pronounced.
Input

The first line contains two positive integers n and k (1 ≤ n ≤ 100 000, 1 ≤ k ≤ min(2·109, n·(n + 1) / 2).

The second line contains the sequence id1, id2, ..., idn (1 ≤ idi ≤ 109) — identifiers of roborts. It is guaranteed that all identifiers are different.
Output

Print the k-th pronounced identifier (assume that the numeration starts from 1).
Examples
Input

2 2
1 2

Output

1

Input

4 5
10 4 18 3

Output

4

Note

In the first sample identifiers of robots will be pronounced in the following order: 1, 1, 2. As k = 2, the answer equals to 1.

In the second test case identifiers of robots will be pronounced in the following order: 10, 10, 4, 10, 4, 18, 10, 4, 18, 3. As k = 5, the answer equals to 4.
'''
