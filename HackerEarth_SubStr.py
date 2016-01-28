t = int(input())
g = {}
for i in range(1,t+1):
    g [i]=input()
n = int(input())
for i in range(n):
    c = 0
    l,r,sub= input().split(' ')
    for x in range(int(l),int(r)+1):
        if sub in g[x]:
            c+=1
    print (c)

'''
Jack is the most intelligent student in the class.To boost his intelligence,his class teacher gave him a problem named "Substring Count".

Problem :
His Class teacher gave him n strings numbered from 1 to n which consists of only lowercase letters (each having length not more than 10) and then ask Q questions related to the given strings.

Each question is described by the 2 integers L,R and a string str,Now his teacher wants to know how many strings numbered from L to R contains str as a substrings.

As expected, Jack solved this problem with in a minute but he failed to solve it efficiently.Now ,its your turn to teach him.How to do it efficiently?? and save him from punishment.

INPUT
First line of input contains a single integer n denoting the number of strings given by class teacher to jack.Next n lines of input contains n strings (one per line).Next line fo input contains a single integer Q denoting the number of questions asked by his teacher.next Q lines of input contains Q question (one per line) as explained above.

OUTPUT
print the correct answer for each of the question asked by his teacher.

CONSTRAINTS
1<=n<=10000
1<=strlen(str)<=10
1<=Q<=5*10^5
1<=L,R<=n

NOTE: strings consist of only lower case characters
Sample Input
(Plaintext Link)

3
code
coder
coding
2
1 3 code
1 3 co

Sample Output
(Plaintext Link)

2 
3

Explanation

Q1:: code coder coding only two out of 3 strings contain cod as substring Q2:: code coder coding all the 3 strings contain co as substring

'''
