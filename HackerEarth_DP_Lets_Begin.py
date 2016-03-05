from sys import maxsize as m
if __name__=='__main__':
    n = int(input())
    g = {1:0,2:1,3:1,4:2,5:1,6:2,7:1}
    def bazinga(N):
        #print(N,g)
        if N in g:  return g[N]
        elif N<=1:   return 0
        else:
            x= [2,3,5,7]
            Min = m
            for i in range(3,-1,-1):
                if N-x[i]<=1:   break
                Min = min(Min,bazinga(N-x[i])+1)
            g[N]=Min
            return Min 
                
        
    for i in range(n):
        num = int(input())
        s = max(g.keys())
        for i in range(s,num+1):
            bazinga(i)
        if (g[num])==0: print(-1)
        else:   print(g[num])
            
            
'''
Let's Begin!
Attempted by: 776
/
Accuracy: 62%
/
Tag(s):
Easy, Math
Problem
Editorial
My Submissions
Analytics
February Easy Challeng...

February Easy Challenge 2015 is underway. Hackerearth welcomes you all and hope that all you awesome coders have a great time. So without wasting much of the time let's begin the contest.

Prime Numbers have always been one of the favourite topics for problem setters. For more information on them you can use see this link http://en.wikipedia.org/wiki/Prime_number .

Aishwarya is a mathematics student at the Department of Mathematics and Computing, California. Her teacher recently gave her an intriguing assignment with only a single question. The question was to find out the minimum number of single digit prime numbers which when summed equals a given number X.

Input:
The first line contains T denoting the number of test cases. Each of the next T lines contains a single integer X.

Output:
Print the minimum number required. If it is not possible to obtain X using single digit prime numbers, output -1.

Constraints:
1<=T<=100
1<=X<=10^6
SAMPLE INPUT

4
7
10
14
11

SAMPLE OUTPUT

1
2
2
3

Explanation

10 can be represented as 7 + 3.

14 can be represented as 7+7

11 can be represented as 5+3+3.
'''
