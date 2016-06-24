from sys import stdin as Si,maxsize as m
from math import floor as F 
from collections import defaultdict as dt
from operator import itemgetter as ig
from math import pi


if __name__== '__main__':
    n,h,k= map(int,Si.readline().split())
    A = list(map(int,Si.readline().split()))
    count,nai,i = 0,A[0],1
    while nai>0:
        if (nai-k)/h>1:
            nai=nai-k
        elif (nai-k)/h==1:
            nai=max(nai-k,0)
            if i<len(A):    nai=A[i]
            i+=1
        else:
            
            while i<len(A) and (nai+A[i])/h<=1:
                nai+=A[i]
                i+=1
            nai=max(nai-k,0)
            if i<len(A) and (nai+A[i])/h<=1:    nai+=A[i];i+=1
        count+=1
            
    print(count)
        
        
'''
B. Vanya and Food Processor
time limit per test
1 second
memory limit per test
256 megabytes
input
standard input
output
standard output

Vanya smashes potato in a vertical food processor. At each moment of time the height of the potato in the processor doesn't exceed h and the processor smashes k centimeters of potato each second. If there are less than k centimeters remaining, than during this second processor smashes all the remaining potato.

Vanya has n pieces of potato, the height of the i-th piece is equal to ai. He puts them in the food processor one by one starting from the piece number 1 and finishing with piece number n. Formally, each second the following happens:

    If there is at least one piece of potato remaining, Vanya puts them in the processor one by one, until there is not enough space for the next piece.
    Processor smashes k centimeters of potato (or just everything that is inside). 

Provided the information about the parameter of the food processor and the size of each potato in a row, compute how long will it take for all the potato to become smashed.
Input

The first line of the input contains integers n, h and k (1 ≤ n ≤ 100 000, 1 ≤ k ≤ h ≤ 109) — the number of pieces of potato, the height of the food processor and the amount of potato being smashed each second, respectively.

The second line contains n integers ai (1 ≤ ai ≤ h) — the heights of the pieces.
Output

Print a single integer — the number of seconds required to smash all the potatoes following the process described in the problem statement.
Examples
Input

5 6 3
5 4 3 2 1

Output

5

Input

5 6 3
5 5 5 5 5

Output

10

Input

5 6 3
1 2 1 1 1

Output

2

Note

Consider the first sample.

    First Vanya puts the piece of potato of height 5 into processor. At the end of the second there is only amount of height 2 remaining inside.
    Now Vanya puts the piece of potato of height 4. At the end of the second there is amount of height 3 remaining.
    Vanya puts the piece of height 3 inside and again there are only 3 centimeters remaining at the end of this second.
    Vanya finally puts the pieces of height 2 and 1 inside. At the end of the second the height of potato in the processor is equal to 3.
    During this second processor finally smashes all the remaining potato and the process finishes. 

In the second sample, Vanya puts the piece of height 5 inside and waits for 2 seconds while it is completely smashed. Then he repeats the same process for 4 other pieces. The total time is equal to 2·5 = 10 seconds.

In the third sample, Vanya simply puts all the potato inside the processor and waits 2 seconds.
'''
