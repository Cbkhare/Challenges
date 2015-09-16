#In case data is passed as a parameter

from sys import argv
#import re

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n').split(',') for line in fp]

#print (contents)


for item in contents:
    s = list(item[0])

    pos = 0

    for i in range(len(s)):

        if s[i]==item[1]:
            pos = i
    if pos == 0:
        print ('-1')
    else:
        print (pos)


'''

Challenge Description:

You are given a string 'S' and a character 't'. Print out the position of the rightmost occurrence of 't' (case matters) in 'S' or -1 if there is none. The position to be printed out is zero based.
Input sample:

The first argument will ba a path to a filename, containing a string and a character, comma delimited, one per line. Ignore all empty lines in the input file. E.g.

Hello World,r
Hello CodeEval,E

Output sample:

Print out the zero based position of the character 't' in string 'S', one per line. Do NOT print out empty lines between your output.
E.g.

8
10

'''
