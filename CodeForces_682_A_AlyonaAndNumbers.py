from sys import stdin as Si,maxsize as m
from math import floor as F 
from collections import defaultdict as dt,Counter as Co
from operator import itemgetter as ig
from math import pi
from itertools import product as P

if __name__== '__main__':
    n,m = map(int,Si.readline().split())
    cn,cm = n//5,m//5     #complete power of 5 
    en,em = n%5,m%5       #extra
    total = cn*cm*5 + cn*em + en*cm   #forming pairs
    for i in range(1,en+1):
        for j in range(1,em+1):
            if (i+j)%5==0:  total+=1
    print(total)
    

'''
A. Alyona and Numbers
time limit per test
1 second
memory limit per test
256 megabytes
input
standard input
output
standard output

After finishing eating her bun, Alyona came up with two integers n and m. She decided to write down two columns of integers — the first column containing integers from 1 to n and the second containing integers from 1 to m. Now the girl wants to count how many pairs of integers she can choose, one from the first column and the other from the second column, such that their sum is divisible by 5.

Formally, Alyona wants to count the number of pairs of integers (x, y) such that 1 ≤ x ≤ n, 1 ≤ y ≤ m and equals 0.

As usual, Alyona has some troubles and asks you to help.
Input

The only line of the input contains two integers n and m (1 ≤ n, m ≤ 1 000 000).
Output

Print the only integer — the number of pairs of integers (x, y) such that 1 ≤ x ≤ n, 1 ≤ y ≤ m and (x + y) is divisible by 5.
Examples
Input

6 12

Output

14

Input

11 14

Output

31

Input

1 5

Output

1

Input

3 8

Output

5

Input

5 7

Output

7

Input

21 21

Output

88

Note

Following pairs are suitable in the first sample case:

    for x = 1 fits y equal to 4 or 9;
    for x = 2 fits y equal to 3 or 8;
    for x = 3 fits y equal to 2, 7 or 12;
    for x = 4 fits y equal to 1, 6 or 11;
    for x = 5 fits y equal to 5 or 10;
    for x = 6 fits y equal to 4 or 9. 

Only the pair (1, 4) is suitable in the third sample case.
'''
            
        
