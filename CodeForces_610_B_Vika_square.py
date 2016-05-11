from sys import stdin as Si

if __name__== '__main__':

    n = int(Si.readline())
    p = list(map(int,Si.readline().split(' ')))
    m= min(p)
    atleast,first,between,s  = m*n, p.index(m),0,0
    for i in p:
        if i==m:    between = max(between,s);s=0
        else:       s+=1
    print(atleast+max(s+first,between))
    
    
    
            
            

    
'''
Vika and Squares
time limit per test
2 seconds
memory limit per test
256 megabytes
input
standard input
output
standard output

Vika has n jars with paints of distinct colors. All the jars are numbered from 1 to n and the i-th jar contains ai liters of paint of color i.

Vika also has an infinitely long rectangular piece of paper of width 1, consisting of squares of size 1 × 1. Squares are numbered 1, 2, 3 and so on. Vika decided that she will start painting squares one by one from left to right, starting from the square number 1 and some arbitrary color. If the square was painted in color x, then the next square will be painted in color x + 1. In case of x = n, next square is painted in color 1. If there is no more paint of the color Vika wants to use now, then she stops.

Square is always painted in only one color, and it takes exactly 1 liter of paint. Your task is to calculate the maximum number of squares that might be painted, if Vika chooses right color to paint the first square.
Input

The first line of the input contains a single integer n (1 ≤ n ≤ 200 000) — the number of jars with colors Vika has.

The second line of the input contains a sequence of integers a1, a2, ..., an (1 ≤ ai ≤ 109), where ai is equal to the number of liters of paint in the i-th jar, i.e. the number of liters of color i that Vika has.
Output

The only line of the output should contain a single integer — the maximum number of squares that Vika can paint if she follows the rules described above.
Examples
Input

5
2 4 2 3 3

Output

12

Input

3
5 5 5

Output

15

Input

6
10 10 10 1 10 10

Output

11

Note

In the first sample the best strategy is to start painting using color 4. Then the squares will be painted in the following colors (from left to right): 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5.

In the second sample Vika can start to paint using any color.

In the third sample Vika should start painting using color number 5.
'''
