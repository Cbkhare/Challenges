from sys import stdin as Si,maxsize as m
from math import floor as F 
from collections import defaultdict as dt,Counter as Co
from operator import itemgetter as ig
from math import pi

if __name__== '__main__':
    n,p = map(int,Si.readline().split())
    C = tuple(map(int,Si.readline().split()))
    count,trv = 0,[]
    for i in range(n):
        d = abs(p-1-i)      #p-1 bcoz 0 based list
        l,r = p-1-d,p-1+d   #left, right
        #print(l,r,p-1,d,count)
        if l==r:
            if l not in trv and C[l]==1: count+=1;trv.append(l)
        else:
            if l<0 and r<n:
                if r not in trv and C[r]==1:   count+=1;trv.append(r)
            elif l>=0 and r>=n:
                if l not in trv and C[l]==1:   count+=1;trv.append(l)
            elif 0<=l<r<n:
                if l not in trv and r not in trv and C[l]==C[r]==1:
                    count+=2;trv.append(l);trv.append(r)
    print(count)
            
        
'''
B. Bear and Finding Criminals
time limit per test
2 seconds
memory limit per test
256 megabytes
input
standard input
output
standard output

There are n cities in Bearland, numbered 1 through n. Cities are arranged in one long row. The distance between cities i and j is equal to |i - j|.

Limak is a police officer. He lives in a city a. His job is to catch criminals. It's hard because he doesn't know in which cities criminals are. Though, he knows that there is at most one criminal in each city.

Limak is going to use a BCD (Bear Criminal Detector). The BCD will tell Limak how many criminals there are for every distance from a city a. After that, Limak can catch a criminal in each city for which he is sure that there must be a criminal.

You know in which cities criminals are. Count the number of criminals Limak will catch, after he uses the BCD.
Input

The first line of the input contains two integers n and a (1 ≤ a ≤ n ≤ 100) — the number of cities and the index of city where Limak lives.

The second line contains n integers t1, t2, ..., tn (0 ≤ ti ≤ 1). There are ti criminals in the i-th city.
Output

Print the number of criminals Limak will catch.
Examples
Input

6 3
1 1 1 0 1 0

Output

3

Input

5 2
0 0 0 1 0

Output

1

Note

In the first sample, there are six cities and Limak lives in the third one (blue arrow below). Criminals are in cities marked red.

Using the BCD gives Limak the following information:

    There is one criminal at distance 0 from the third city — Limak is sure that this criminal is exactly in the third city.
    There is one criminal at distance 1 from the third city — Limak doesn't know if a criminal is in the second or fourth city.
    There are two criminals at distance 2 from the third city — Limak is sure that there is one criminal in the first city and one in the fifth city.
    There are zero criminals for every greater distance. 

So, Limak will catch criminals in cities 1, 3 and 5, that is 3 criminals in total.

In the second sample (drawing below), the BCD gives Limak the information that there is one criminal at distance 2 from Limak's city. There is only one city at distance 2 so Limak is sure where a criminal is.
'''
