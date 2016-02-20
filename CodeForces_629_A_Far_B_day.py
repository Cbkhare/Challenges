from math import factorial as f
if __name__=='__main__':
    n= int(input())
    if n==1:
        t = input()
        if t=='C':  print(1)
        else:   print(0)
    else:
        hapi = 0
        ck = []
        for i in range(n):
            t = input()
            c = t.count('C')
            if c > 1:
                hapi +=  int(c*(c-1)/2)
            ck+=[t]
        vapi = 0
        for j in range(n):
            c = 0
            for x in range(n):
                if ck[x][j]=='C':
                    c+=1
            if c>1: vapi += int(c*(c-1)/2)
        print (hapi+vapi)

'''

A. Far Relative’s Birthday Cake
time limit per test
1 second
memory limit per test
256 megabytes
input
standard input
output
standard output

Door's family is going celebrate Famil Doors's birthday party. They love Famil Door so they are planning to make his birthday cake weird!

The cake is a n × n square consisting of equal squares with side length 1. Each square is either empty or consists of a single chocolate. They bought the cake and randomly started to put the chocolates on the cake. The value of Famil Door's happiness will be equal to the number of pairs of cells with chocolates that are in the same row or in the same column of the cake. Famil Doors's family is wondering what is the amount of happiness of Famil going to be?

Please, note that any pair can be counted no more than once, as two different cells can't share both the same row and the same column.
Input

In the first line of the input, you are given a single integer n (1 ≤ n ≤ 100) — the length of the side of the cake.

Then follow n lines, each containing n characters. Empty cells are denoted with '.', while cells that contain chocolates are denoted by 'C'.
Output

Print the value of Famil Door's happiness, i.e. the number of pairs of chocolate pieces that share the same row or the same column.
Examples
Input

3
.CC
C..
C.C

Output

4

Input

4
CC..
C..C
.CC.
.CC.

Output

9

Note

If we number rows from top to bottom and columns from left to right, then, pieces that share the same row in the first sample are:

    (1, 2) and (1, 3)
    (3, 1) and (3, 3) 

Pieces that share the same column are:

    (2, 1) and (3, 1)
    (1, 3) and (3, 3) 

'''
        
        
