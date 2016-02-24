if __name__=='__main__':
    L,Q = map(int,input().split(' '))
    g= {}
    last = pow(2,L-1)
    g[L]=sum(range(1,last+1))
    nw_lst=tuple([i for i in range(1,last+1)])
    tmp_lst = ()
    while len(nw_lst)>1:
        #print (nw_lst)
        for i in range(0,len(nw_lst),2):
            tmp_lst+=(nw_lst[i]*nw_lst[i+1],)
        g[L-1]=sum(tmp_lst)
        L=L-1
        nw_lst=tmp_lst[:]
        tmp_lst=()

    for i in range(Q):
        x,y = map(int,input().split(' '))
        Sum = 0
        for j in range(x,y+1):
            Sum+=g[j]
        print (Sum%1299709)
        
        
'''

Crazy Tree 2
Max. Marks 100

Abhimanyu makes a complete binary tree of level L, called Crazy Tree. The levels are numbered 1, 2, ..., L from top to bottom. The root of the tree is at level 1. He numbers all the leaf nodes 1, 2, 3, ... from left to right. The value of every parent node is the product of values of its child nodes.

Below are Level 2 (left) and Level 3 (right) Crazy Trees.

Level 2 Crazy Tree Level 3 Crazy Tree

Abhimanyu has a magical function S:

    S(Z): This function gives sum of all the nodes at level Z

For two magical integers X and Y, Abhimanyu wants to find the value of W % M, where:

    W = S(X) + S(X + 1) + ... + S(Y)
    M = 1299709

Input

First line of input contains two space separated integers L and Q, where L is the number of levels in Crazy Tree and Q is number of queries. Each of next Q lines contains two space separated integers X and Y.

Output

Output W % M, for each test case in single line.

Constraints

    1 <= L <= 21
    1 <= Q <= L (L + 1) / 2
    1 <= X <= L
    X <= Y <= L
    M = 1299709

Sample Input
(Plaintext Link)

3 6
1 1
1 2
1 3
2 2
2 3
3 3

Sample Output
(Plaintext Link)

24
38
48
14
24
10

Explanation

The tree is Level 3 tree. So, S(1) = 24 S(2) = 14 S(3) = 10
Time Limit: 1 sec(s) for each input file.
Memory Limit: 256 MB
Source Limit: 100 KB
Marking Scheme: Marks are awarded if any testcase passes.
Allowed languages: C, CPP, CLOJURE, CSHARP, GO, HASKELL, JAVA, JAVASCRIPT, JAVASCRIPT_NODE, LISP, OBJECTIVEC, PASCAL, PERL, PHP, PYTHON, RUBY, R, RUST, SCALA
'''
            
        
