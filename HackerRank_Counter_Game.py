from sys import stdin as Si, maxsize as m
from math import log 
#import numpy as np


def winner(N):
        L,R = 'Louise','Richard'
        count = 1
        _n=N
        '''
        while (_n > 1):
            if bin(_n).count('1') == 1:
                _n = int(bin(_n).replace('10', '1', 1), 2)
            else:
                _n = int(bin(_n).replace('1', '', 1), 2)
            print(_n)
        '''
        while N>1:
            if (N & N-1)==0 and N!=0:   N=int(N/2)  #if N is power of 2 
            else:
                N-= 1<<(N.bit_length() - 1)
            count+=1
        
        if count%2==0:  return L
        else: return R
        

if __name__=='__main__':
    n = int(Si.readline())
    for i in range(n):
        print(winner(int(Si.readline())))
    

'''

Counter game
by dheeraj

    Problem
    Submissions
    Leaderboard
    Discussions
    Editorial

Louise and Richard play a game. They have a counter set to N. Louise gets the first turn and the turns alternate thereafter. In the game, they perform the following operations.

    If N is not a power of 2, reduce the counter by the largest power of 2 less than N.
    If N is a power of 2, reduce the counter by half of N.
    The resultant value is the new N which is again used for subsequent operations.

The game ends when the counter reduces to 1, i.e., N == 1, and the last person to make a valid move wins.

Given N, your task is to find the winner of the game.

Update If they set counter to 1, Richard wins, because its Louise' turn and she cannot make a move.

Input Format
The first line contains an integer T, the number of testcases.
T lines follow. Each line contains N, the initial number set in the counter.

Constraints

1 ≤ T ≤ 10
1 ≤ N ≤ 264 - 1

Note: Range of N is larger than long long int, consider using unsigned long long int.

Output Format

For each test case, print the winner's name in a new line. So if Louise wins the game, print "Louise". Otherwise, print "Richard". (Quotes are for clarity)

Sample Input

1
6

Sample Output

Richard

Explanation

    As 6 is not a power of 2, Louise reduces the largest power of 2 less than 6 i.e., 4, and hence the counter reduces to 2.
    As 2 is a power of 2, Richard reduces the counter by half of 2 i.e., 1. Hence the counter reduces to 1.

As we reach the terminating condition with N == 1, Richard wins the game.

'''
