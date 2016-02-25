if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,m= map(int,input().split(' '))
        ml, fm = (),()
        sus = False
        for i in range(m):
            x,y = map(int,input().split(' '))
            if x not in fm and y not in ml:
                ml+=(x,)
                fm+=(y,)
            else:
                sus= True
        if sus: print ('Suspicious lizards found!')
        else:   print ('No suspicious lizards found!')
'''

Professor Hatim's Experiment (Mandatory)
Max. Marks 200

Professor Hatim is researching the sexual behavior of a rare species of lizard. He assumes that they feature two different genders and that they only interact with lizard of the opposite gender. Each lizard has a integer printed on their back.

Given the details of lizard interactions, decide whether the experiment supports his assumption of two genders with no homosexual bugs, or if it contains some bug interactions that falsify it. Or simply, you have to print "Suspicious lizard found!" (without quotes), if an interaction of two lizards of same gender is found in the list of interactions, otherwise print "No suspicious lizard found!" (without quotes).

Input format:
The first line contains an integer T, denoting the number of test cases.
The first line of each test case contains two integers N and M, where N denotes the number of lizards and M denotes the number of interactions.
Next M lines of each test case contains, two space separated integers, say x and y , denoting the interaction between lizard no. x and lizard no. y.

Note: Integers on the back of lizards are numbered from 1 to N.

Output format:
For each test case ,print a line, saying either “No suspicious lizard found!” if the experiment is consistent with his assumption about the lizard sexual behavior, or “Suspicious lizard found!” if Professor Hatims’s assumption is definitely wrong.

Constraints:
1 ≤ T ≤ 5
2 ≤ N ≤ 2000
1 ≤ M ≤ 105
Sample Input
(Plaintext Link)

2
3 3
1 2
2 3
1 3
4 2
1 2
3 4

Sample Output
(Plaintext Link)

Suspicious lizards found!
No suspicious lizards found!

'''
            
        
