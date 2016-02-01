
if __name__ == '__main__':
    stack = []
    n = int(input())
    tup = tuple(map(int,input().split(' ')))
    Sum = 0 
    for  i in range(n):
        if tup[i]%2==0:
            Sum+=tup[i]
        else:
            stack.append(tup[i])
    stack.sort()
    if len(stack)%2==0:
        Sum+=sum(stack)
    else:
        Sum+=sum(stack[1:])
    print (Sum)
            
'''

A. Wet Shark and Odd and Even
time limit per test
2 seconds
memory limit per test
256 megabytes
input
standard input
output
standard output

Today, Wet Shark is given n integers. Using any of these integers no more than once, Wet Shark wants to get maximum possible even (divisible by 2) sum. Please, calculate this value for Wet Shark.

Note, that if Wet Shark uses no integers from the n integers, the sum is an even integer 0.
Input

The first line of the input contains one integer, n (1 ≤ n ≤ 100 000). The next line contains n space separated integers given to Wet Shark. Each of these integers is in range from 1 to 109, inclusive.
Output

Print the maximum possible even sum that can be obtained if we use some of the given integers.
Sample test(s)
Input

3
1 2 3

Output

6

Input

5
999999999 999999999 999999999 999999999 999999999

Output

3999999996

Note

In the first sample, we can simply take all three integers for a total sum of 6.

In the second sample Wet Shark should take any four out of five integers 999 999 999.

'''
