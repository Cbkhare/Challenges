from sys import stdin as Si,maxsize as m
from math import floor as F 
from collections import defaultdict as dt,Counter as Co
from operator import itemgetter as ig
from math import pi
from itertools import product as P

if __name__== '__main__':
    n = int(Si.readline())
    A = list(map(int,Si.readline().split()))

    for i in range(n):
        Aa = sorted((A[x],x) for x in range(n))
        print(A,Aa,i)
        t,j = Aa[i]
        if j>i:
            for x in range(j,i,-1):
                print(x,x+1)
                A[x],A[x-1]=A[x-1],A[x]
        
'''
B. Little Robber Girl's Zoo
time limit per test
2 seconds
memory limit per test
256 megabytes
input
standard input
output
standard output

Little Robber Girl likes to scare animals in her zoo for fun. She decided to arrange the animals in a row in the order of non-decreasing height. However, the animals were so scared that they couldn't stay in the right places.

The robber girl was angry at first, but then she decided to arrange the animals herself. She repeatedly names numbers l and r such that r - l + 1 is even. After that animals that occupy positions between l and r inclusively are rearranged as follows: the animal at position l swaps places with the animal at position l + 1, the animal l + 2 swaps with the animal l + 3, ..., finally, the animal at position r - 1 swaps with the animal r.

Help the robber girl to arrange the animals in the order of non-decreasing height. You should name at most 20 000 segments, since otherwise the robber girl will become bored and will start scaring the animals again.
Input

The first line contains a single integer n (1 ≤ n ≤ 100) — number of animals in the robber girl's zoo.

The second line contains n space-separated integers a1, a2, ..., an (1 ≤ ai ≤ 109), where ai is the height of the animal occupying the i-th place.
Output

Print the sequence of operations that will rearrange the animals by non-decreasing height.

The output should contain several lines, i-th of the lines should contain two space-separated integers li and ri (1 ≤ li < ri ≤ n) — descriptions of segments the robber girl should name. The segments should be described in the order the operations are performed.

The number of operations should not exceed 20 000.

If the animals are arranged correctly from the start, you are allowed to output nothing.
Examples
Input

4
2 1 4 3

Output

1 4

Input

7
36 28 57 39 66 69 68

Output

1 4
6 7

Input

5
1 2 1 2 1

Output

2 5
3 4
1 4
1 4

Note

Note that you don't have to minimize the number of operations. Any solution that performs at most 20 000 operations is allowed.
'''
        
