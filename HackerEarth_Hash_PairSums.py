from operator import itemgetter as ig
from sys import stdin as Si


    
if __name__=='__main__':

    n,k = map(int,Si.readline().split())
    A = list(map(int,Si.readline().split()))
    h = {} 
    for i in A:
        if i in h:  print('Yes');break
        h[k-i]=h.get(k-i,0)+1
    else:   print('No')
        
        
'''
Pair Sums
Attempted by: 48
/
Accuracy: 66%
/
Tag(s):
Easy
Problem
Editorial
My Submissions
Analytics
Walk in the Park

You have been given an integer array A
and a number K. Now, you need to find out whether any two different elements of the array A sum to the number K

. Two elements are considered to be different if they lie at different positions in the array. If there exists such a pair of numbers, print "YES" (without quotes), else print "NO" without quotes.

Input Format:

The first line consists of two integers N
, denoting the size of array A and K. The next line consists of N space separated integers denoting the elements of the array A

.

Output Format:

Print the required answer on a single line.

Constraints:

1≤N≤106

1≤K≤2∗106

1≤A[i]≤106

SAMPLE INPUT

5 9
1 2 3 4 5

SAMPLE OUTPUT

YES

Explanation

Here, A[4]+A[5]=4+5=9
. So, the answer is YES.
'''
