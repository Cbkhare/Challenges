from math import factorial as F 
if __name__=='__main__':
    n = int(input())
    ans = 1
    for i in range(3,6,2):
        t = n+i-1
        b = n-1
        ans *= int(F(t)/(F(t-b)*F(b)))
    print (ans)


'''

G. Challenge Pennants
time limit per test
0.5 seconds
memory limit per test
64 megabytes
input
standard input
output
standard output

Because of budget cuts one IT company established new non-financial reward system instead of bonuses.

Two kinds of actions are rewarded: fixing critical bugs and suggesting new interesting features. A man who fixed a critical bug gets "I fixed a critical bug" pennant on his table. A man who suggested a new interesting feature gets "I suggested a new feature" pennant on his table.

Because of the limited budget of the new reward system only 5 "I fixed a critical bug" pennants and 3 "I suggested a new feature" pennants were bought.

In order to use these pennants for a long time they were made challenge ones. When a man fixes a new critical bug one of the earlier awarded "I fixed a critical bug" pennants is passed on to his table. When a man suggests a new interesting feature one of the earlier awarded "I suggested a new feature" pennants is passed on to his table.

One man can have several pennants of one type and of course he can have pennants of both types on his table. There are n tables in the IT company. Find the number of ways to place the pennants on these tables given that each pennant is situated on one of the tables and each table is big enough to contain any number of pennants.
Input

The only line of the input contains one integer n (1 ≤ n ≤ 500) — the number of tables in the IT company.
Output

Output one integer — the amount of ways to place the pennants on n tables.
Examples
Input

2

Output

24

'''
