class Solution:
    def powerLink(self,l,r,k):
        Min = int(l/k)
        Max = int(r/k)
        stack = []
        #print (Min,Max)
        for i in range(0,Max+1):
            x = pow(k,i)
            if x>r:    break
            if l<=x<=r: stack.append(x)
        return stack 
        
            

if __name__ == '__main__':
    l,r,k = list(map(int,input().split(' ')))
    
    S = Solution()
    result =  (S.powerLink(l,r,k))
    if result ==[]:
        print (-1)
    else:
        print (' '.join(list(map(str,result))))
    
'''

A. Link/Cut Tree
time limit per test
2 seconds
memory limit per test
256 megabytes
input
standard input
output
standard output

Programmer Rostislav got seriously interested in the Link/Cut Tree data structure, which is based on Splay trees. Specifically, he is now studying the expose procedure.

Unfortunately, Rostislav is unable to understand the definition of this procedure, so he decided to ask programmer Serezha to help him. Serezha agreed to help if Rostislav solves a simple task (and if he doesn't, then why would he need Splay trees anyway?)

Given integers l, r and k, you need to print all powers of number k within range from l to r inclusive. However, Rostislav doesn't want to spent time doing this, as he got interested in playing a network game called Agar with Gleb. Help him!
Input

The first line of the input contains three space-separated integers l, r and k (1 ≤ l ≤ r ≤ 1018, 2 ≤ k ≤ 109).
Output

Print all powers of number k, that lie within range from l to r in the increasing order. If there are no such numbers, print "-1" (without the quotes).
Sample test(s)
Input

1 10 2

Output

1 2 4 8 

Input

2 4 5

Output

-1

Note

Note to the first sample: numbers 20 = 1, 21 = 2, 22 = 4, 23 = 8 lie within the specified range. The number 24 = 16 is greater then 10, thus it shouldn't be printed.
'''
