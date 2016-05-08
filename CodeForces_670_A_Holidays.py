from sys import stdin as Si
from math import floor as F 
from collections import defaultdict as dt
from operator import itemgetter as ig
from math import pi 


if __name__== '__main__':
    N = int(Si.readline())
    M = N%7
    Min,Max=0,0
    ne,xe=0,0
    if M>=5:    ne = M-5
    else:   ne =0
    if M>2: xe=2
    else:   xe=M
    
    print((N//7*2)+ne,' ',(N//7*2)+xe)

'''
A. Holidays
time limit per test
1 second
memory limit per test
256 megabytes
input
standard input
output
standard output

On the planet Mars a year lasts exactly n days (there are no leap years on Mars). But Martians have the same weeks as earthlings — 5 work days and then 2 days off. Your task is to determine the minimum possible and the maximum possible number of days off per year on Mars.
Input

The first line of the input contains a positive integer n (1 ≤ n ≤ 1 000 000) — the number of days in a year on Mars.
Output

Print two integers — the minimum possible and the maximum possible number of days off per year on Mars.
Examples
Input

14

Output

4 4

Input

2

Output

0 2

Note

In the first sample there are 14 days in a year on Mars, and therefore independently of the day a year starts with there will be exactly 4 days off .

In the second sample there are only 2 days in a year on Mars, and they can both be either work days or days off.
'''
