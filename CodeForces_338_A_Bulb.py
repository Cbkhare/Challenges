class Solution:
    def checkPosible(self,n,S):
        Set = []
        for i in range(n):
            Set += list(map(int,input().split(' ')))[1:]
            
        if sum(set(Set))==Sm:
            return 'YES'
        else:
            return 'NO'
            

if __name__ == '__main__':
    n,m = list(map(int,input().split(' ')))
    Sm = sum([i for i in range(1,m+1)])
    S = Solution()
    print (S.checkPosible(n,Sm))
    
'''

A. Bulbs
time limit per test
1 second
memory limit per test
256 megabytes
input
standard input
output
standard output

Vasya wants to turn on Christmas lights consisting of m bulbs. Initially, all bulbs are turned off. There are n buttons, each of them is connected to some set of bulbs. Vasya can press any of these buttons. When the button is pressed, it turns on all the bulbs it's connected to. Can Vasya light up all the bulbs?

If Vasya presses the button such that some bulbs connected to it are already turned on, they do not change their state, i.e. remain turned on.
Input

The first line of the input contains integers n and m (1 ≤ n, m ≤ 100) — the number of buttons and the number of bulbs respectively.

Each of the next n lines contains xi (0 ≤ xi ≤ m) — the number of bulbs that are turned on by the i-th button, and then xi numbers yij (1 ≤ yij ≤ m) — the numbers of these bulbs.
Output

If it's possible to turn on all m bulbs print "YES", otherwise print "NO".
Sample test(s)
Input

3 4
2 1 4
3 1 3 1
1 2

Output

YES

Input

3 3
1 1
1 2
1 1

Output

NO

Note

In the first sample you can press each button once and turn on all the bulbs. In the 2 sample it is impossible to turn on the 3-rd lamp.
'''
