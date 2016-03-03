if __name__=='__main__':
    n,q = map(int,input().split(' '))
    A = list(map(int,input().split(' ')))
    B = list(map(int,input().split(' ')))
    
    for i in range(1,n,2):
        A[i],B[i]=B[i],A[i]
    A,B=[0]+A,[0]+B
    for i in range(1,n+1):
        A[i]+=A[i-1]
        B[i]+=B[i-1]
    for i in range(q):
        s,l,r = map(int,input().split(' '))
        if s==1:
            if l%2!=0:  print(A[r]-A[l-1])
            else:       print(B[r]-B[l-1])
        else:
            if l%2==0:  print(A[r]-A[l-1])
            else:       print(B[r]-B[l-1])
'''

Xsquare loves to play with arrays a lot. Today, he has two arrays named as A and B. Each array consists of N positive integers.

Xsquare has decided to fulfill following types of queries over his array A and array B.

    1 L R : Print the value of AL + BL+1 + AL+2 + BL+3 + ... upto Rth term.
    2 L R : Print the value of BL + AL+1 + BL+2 + AL+3 + ... upto Rth term.

Input

First line of input contains two space separated integers N and Q denoting the size of arrays ( A , B ) and number of queries respectively. Next N lines of input contains N space separated integers denoting array A. Next line of input contains N space separated integers denoting array B. Next Q lines of input contains Q queries (one per line). Each query has one of the above mentioned types.
Output

Output consists of Q lines, each containing answer to the corresponding query.
Constraints

    1 ≤ N,Q ≤ 105
    1 ≤ Ai,Bi ≤ 109
    1 ≤ L,R ≤ N

SAMPLE INPUT

5 5
1 2 3 4 5
5 4 3 2 1
1 1 5
2 1 5
1 2 4
2 2 4
1 3 5

SAMPLE OUTPUT

15
15
9
9
10

Explanation

Q1 : A[1] + B[2] + A[3] + B[4] + A[5] = 1 + 4 + 3 + 2 + 5 = 15 Q2 : B[1] + A[2] + B[3] + A[4] + B[5] = 5 + 2 + 3 + 4 + 1 = 15 Q3 : A[2] + B[3] + A[4] = 2 + 3 + 4 = 9 Q4 : B[2] + A[3] + B[4] = 4 + 3 + 2 = 9 Q5 : A[3] + B[4] + A[5] = 3 + 2 + 5 = 10
'''
