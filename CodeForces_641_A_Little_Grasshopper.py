from sys import stdin as Si
from math import floor as F 
from collections import defaultdict as dt
from operator import itemgetter as ig

if __name__== '__main__':

    n = int(Si.readline())
    d = Si.readline().strip('\n')
    c = tuple(map(int,Si.readline().split()))
    tub,i,Exit = set([0]),0,False
    while not Exit:
        if d[i]=='>':   i=i+c[i]
        else:   i=i-c[i]
        if  i<0 or i>=n:   print('FINITE');break
        elif i in tub:    print('INFINITE');break
        else: tub.add(i)
        
        
    
    
'''
A. Little Artem and Grasshopper
time limit per test
2 seconds
memory limit per test
256 megabytes
input
standard input
output
standard output

Little Artem found a grasshopper. He brought it to his house and constructed a jumping area for him.

The area looks like a strip of cells 1 × n. Each cell contains the direction for the next jump and the length of that jump. Grasshopper starts in the first cell and follows the instructions written on the cells. Grasshopper stops immediately if it jumps out of the strip. Now Artem wants to find out if this will ever happen.
Input

The first line of the input contains a single integer n (1 ≤ n ≤ 100 000) — length of the strip.

Next line contains a string of length n which consists of characters "<" and ">" only, that provide the direction of the jump from the corresponding cell. Next line contains n integers di (1 ≤ di ≤ 109) — the length of the jump from the i-th cell.
Output

Print "INFINITE" (without quotes) if grasshopper will continue his jumps forever. Otherwise print "FINITE" (without quotes).
Examples
Input

2
><
1 2

Output

FINITE

Input

3
>><
2 1 1

Output

INFINITE

Note

In the first sample grasshopper starts from the first cell and jumps to the right on the next cell. When he is in the second cell he needs to jump two cells left so he will jump out of the strip.

Second sample grasshopper path is 1 - 3 - 2 - 3 - 2 - 3 and so on. The path is infinite.
'''
