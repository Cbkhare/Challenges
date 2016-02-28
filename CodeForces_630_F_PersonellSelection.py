from math import factorial as F 
if __name__=='__main__':
    n = int(input())
    ans = 0
    for i in range(5,8):
        ans += int(F(n)/(F(n-i)*F(i)))
    print (ans)

'''

F. Selection of Personnel
time limit per test
0.5 seconds
memory limit per test
64 megabytes
input
standard input
output
standard output

One company of IT City decided to create a group of innovative developments consisting from 5 to 7 people and hire new employees for it. After placing an advertisment the company received n resumes. Now the HR department has to evaluate each possible group composition and select one of them. Your task is to count the number of variants of group composition to evaluate.
Input

The only line of the input contains one integer n (7 ≤ n ≤ 777) — the number of potential employees that sent resumes.
Output

Output one integer — the number of different variants of group composition.
Examples
Input

7

Output

29


'''
