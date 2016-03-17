if __name__=='__main__':
    n = int(input())
    gx,gy,c= {},{},0
    tup = {}
    for i in range(n):
        x,y= map(int,input().split(' '))
        if x in gx and y not in gy:
            c += gx[x]
            gx[x]+=1
            gy[y]=1
            tup[(x,y)]=1
        elif x not in gx and y in gy:
            c += gy[y]
            gy[y]+=1
            gx[x]=1
            tup[(x,y)]=1
        elif x not in gx and y not in gy:
            gx[x],gy[y],tup[(x,y)]=1,1,1
        elif x in gx and y in gy:
            if (x,y) in tup:
                c+=gx[x]+gy[y]-tup[(x,y)]     #common
                tup[(x,y)]+=1
            else:
                c+=gx[x]+gy[y]
                tup[(x,y)]=1
            gx[x]+=1
            gy[y]+=1
    print(c)
#Hint: such scenario is only possible when x=x1 or y=y1 or x=x1,y=y1
#Use Hash
'''

C. Watchmen
time limit per test
3 seconds
memory limit per test
256 megabytes
input
standard input
output
standard output

Watchmen are in a danger and Doctor Manhattan together with his friend Daniel Dreiberg should warn them as soon as possible. There are n watchmen on a plane, the i-th watchman is located at point (xi, yi).

They need to arrange a plan, but there are some difficulties on their way. As you know, Doctor Manhattan considers the distance between watchmen i and j to be |xi - xj| + |yi - yj|. Daniel, as an ordinary person, calculates the distance using the formula .

The success of the operation relies on the number of pairs (i, j) (1 ≤ i < j ≤ n), such that the distance between watchman i and watchmen j calculated by Doctor Manhattan is equal to the distance between them calculated by Daniel. You were asked to compute the number of such pairs.
Input

The first line of the input contains the single integer n (1 ≤ n ≤ 200 000) — the number of watchmen.

Each of the following n lines contains two integers xi and yi (|xi|, |yi| ≤ 109).

Some positions may coincide.
Output

Print the number of pairs of watchmen such that the distance between them calculated by Doctor Manhattan is equal to the distance calculated by Daniel.
Examples
Input

3
1 1
7 5
1 5

Output

2

Input

6
0 0
0 1
0 2
-1 1
0 1
1 1

Output

11

Note

In the first sample, the distance between watchman 1 and watchman 2 is equal to |1 - 7| + |1 - 5| = 10 for Doctor Manhattan and for Daniel. For pairs (1, 1), (1, 5) and (7, 5), (1, 5) Doctor Manhattan and Daniel will calculate the same distances.
'''

