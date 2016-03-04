if __name__=='__main__':

    n,m,k = map(int,input().split(' '))
    M = list(list('0' for i in range(m)) for i in range(n))
    tR, tC,C = [0]*n, [0]*m, [0]*(k+1)
    for i in range(1,k+1):
        tQ,pQ,C[i]= map(int,input().split(' '))
        print(tR,tC,C)
        if tQ==1:       tR[pQ-1]=i   
        elif tQ==2:     tC[pQ-1]=i
        print(tR,tC,C)
    for i in range(n):
        finalStr= ''
        for j in range(m):
            finalStr += str(C[max(tR[i],tC[j])])
            finalStr +=' '
        print(finalStr)

'''
Print Check
time limit per test
1 second
memory limit per test
256 megabytes
input
standard input
output
standard output

Kris works in a large company "Blake Technologies". As a best engineer of the company he was assigned a task to develop a printer that will be able to print horizontal and vertical strips. First prototype is already built and Kris wants to tests it. He wants you to implement the program that checks the result of the printing.

Printer works with a rectangular sheet of paper of size n × m. Consider the list as a table consisting of n rows and m columns. Rows are numbered from top to bottom with integers from 1 to n, while columns are numbered from left to right with integers from 1 to m. Initially, all cells are painted in color 0.

Your program has to support two operations:

    Paint all cells in row ri in color ai;
    Paint all cells in column ci in color ai. 

If during some operation i there is a cell that have already been painted, the color of this cell also changes to ai.

Your program has to print the resulting table after k operation.
Input

The first line of the input contains three integers n, m and k (1  ≤  n,  m  ≤ 5000, n·m ≤ 100 000, 1 ≤ k ≤ 100 000) — the dimensions of the sheet and the number of operations, respectively.

Each of the next k lines contains the description of exactly one query:

    1 ri ai (1 ≤ ri ≤ n, 1 ≤ ai ≤ 109), means that row ri is painted in color ai;
    2 ci ai (1 ≤ ci ≤ m, 1 ≤ ai ≤ 109), means that column ci is painted in color ai. 

Output

Print n lines containing m integers each — the resulting table after all operations are applied.
Examples
Input

3 3 3
1 1 3
2 2 1
1 2 2

Output

3 1 3 
2 2 2 
0 1 0 

Input

5 3 5
1 1 1
1 3 1
1 5 1
2 1 1
2 3 1

Output

1 1 1 
1 0 1 
1 1 1 
1 0 1 
1 1 1
'''
    
