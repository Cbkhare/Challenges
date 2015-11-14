from sys import argv

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n').split(' ') for line in fp]

for item in contents:
    if '+' in item[1]:
        i = item[1].index('+')
        p1= int(item[0][:i])
        p2= int(item[0][i:])
        print (p1+p2)
    elif '-' in item[1]:
        i = item[1].index('-')
        p1= int(item[0][:i])
        p2= int(item[0][i:])
        print (p1-p2) 
        
    

'''
Challenge Description:

You are given a number N and a pattern. The pattern consists of lowercase latin letters and one operation "+" or "-". The challenge is to split the number and evaluate it according to this pattern e.g.
1232 ab+cd -> a:1, b:2, c:3, d:2 -> 12+32 -> 44
Input sample:

Your program should accept as its first argument a path to a filename. Each line of the file is a test case, containing the number and the pattern separated by a single whitespace. E.g.
3413289830 a-bcdefghij
776 a+bc
12345 a+bcde
1232 ab+cd
90602 a+bcde

Output sample:

For each test case print out the result of pattern evaluation. E.g.
-413289827
83
2346
44
611

Constraints:
N is in range [100, 1000000000]
'''
