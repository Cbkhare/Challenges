from math import pi

if __name__=='__main__':
    g = {}                  #Dictionary to store results
    def bazinga(i,C):
        print (i)
        if C=={}:
            return 0
        else:
            k = i
            if k in g:
                return (g[k])
            else:
                p_vols = []               #possible volumes
                for x in range(k+1,len(C)+1):
                    if C[x]>C[k]:
                        p_vols+=[bazinga(x,C)]                  
                if p_vols==[]:
                    g[k]=C[k]
                    return g[k]
                else:
                    g[k]=max(p_vols)
                    return (C[k]+g[k])
                    
       
    #MAIN#          
    cakes = {}
    n = int(input())
    for i in range(1,n+1):
        r,h = map(int,input().split(' '))
        cakes[i]= (pi*pow(r,2)*h)       #dictionary, key holds the positon and values holds the area
    #print (cakes)
    print (bazinga(1,cakes)%pow(10,6))
    

'''

D. Babaei and Birthday Cake
time limit per test
2 seconds
memory limit per test
256 megabytes
input
standard input
output
standard output

As you know, every birthday party has a cake! This time, Babaei is going to prepare the very special birthday party's cake.

Simple cake is a cylinder of some radius and height. The volume of the simple cake is equal to the volume of corresponding cylinder. Babaei has n simple cakes and he is going to make a special cake placing some cylinders on each other.

However, there are some additional culinary restrictions. The cakes are numbered in such a way that the cake number i can be placed only on the table or on some cake number j where j < i. Moreover, in order to impress friends Babaei will put the cake i on top of the cake j only if the volume of the cake i is strictly greater than the volume of the cake j.

Babaei wants to prepare a birthday cake that has a maximum possible total volume. Help him find this value.
Input

The first line of the input contains a single integer n (1 ≤ n ≤ 100 000) — the number of simple cakes Babaei has.

Each of the following n lines contains two integers ri and hi (1 ≤ ri, hi ≤ 10 000), giving the radius and height of the i-th cake.
Output

Print the maximum volume of the cake that Babaei can make. Your answer will be considered correct if its absolute or relative error does not exceed 10 - 6.

Namely: let's assume that your answer is a, and the answer of the jury is b. The checker program will consider your answer correct, if .
Examples
Input

2
100 30
40 10

Output

942477.796077000

Input

4
1 1
9 7
1 4
10 7

Output

3983.539484752

Note

In first sample, the optimal way is to choose the cake number 1.

In second sample, the way to get the maximum volume is to use cakes with indices 1, 2 and 4.
'''
