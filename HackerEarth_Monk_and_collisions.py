from operator import itemgetter as ig 
    
if __name__=='__main__':    
    n = int(input())
    for i in range(n):
        t= int(input())
        lst = tuple(map(int,input().split(' ')))
        h = [0 for i in range(10)]  #list hash
        for l in lst:   h[l%10]+=1
        c = sum([j-1 for j in h if j>1])
        print(c)
        
            
'''

Problem
Editorial
My Submissions

As the Monk is also taking part in the CodeMonk Series, this week he learned about hashing. Now he wants to practice some problems. So he came up with a simple problem. Firstly, he made a hash function F such that:

    F(x) = x % 10

Now using this function he wants to hash N integers and count the number of collisions that will occur while hashing the integers.

Input:
The first line contains an integer T, denoting the number of test cases.
The first line of each test case contains an integer N, denoting the number of integers to hash.
The next line contains N space separated integers, denoting the integer X to hash.

Output:
For each test case, print the number of collisions that will occur while hashing the integers.

Constraints:
1 <= T <= 10
1 <= N <= 100
0 <= X <= 105
Sample Input
(Plaintext Link)

2
3
1 2 3
4
1 1 2 3

Sample Output
(Plaintext Link)

0
1

Explanation

In the first case, there will be no collisions as each integer will be hashed to a different index.
F(1) = 1 % 10 = 1
F(2) = 2 % 10 = 2
F(3) = 3 % 10 = 3

In the second case, there will be 1 collision at index 1 as the first two integers will hash to the same index.

'''
        
        
        
    


        
            
            
