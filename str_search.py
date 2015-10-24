
#In case data is passed as a parameter

from sys import argv, getsizeof
#from operator import itemgetter
import re
#import math
#from itertools import permutations
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n').split(',') for line in fp]

for item in contents:
    #print (item) 
    str1,str2 = item

    if '*' not in str2 and  '\\*' not in str2:
        if str2 in str1:
            print ('true')
            continue
        else:
            print('false')
            continue
            
    if '*' in str2 and  '\\*' not in str2:
        stack = []
        if len(str2) ==1:
            print ('true')
            continue
        while '*' in str2:
            stack.append(str2[:str2.index('*')])
            str2 = str2[str2.index('*')+1:]
            if '*' not in str2: stack.append(str2)

        stat = 1
        for stuff in stack:
            #print (stuff)
            if stuff=='':
                continue
            
            if stuff in str1:
                str1 = str1[str1.index(stuff[-1])+1:]
            else:
                stat = 0
                break
        if stat == 1:
            print ('true')
            continue
        else:
            print ('false')
            continue

    if '\\*' in str2:
        str2 = list(str2)
        while '\\' in str2:
            str2.remove('\\')
        str2 = ''.join(str2)
        if str2 in str1:
            print ('true')
            continue
        else:
            print ('false')
            continue

    

'''
String Searching

Challenge Description:

You are given two strings. Determine if the second string is a substring of the first (Do NOT use any substr type library function). The second string may contain an asterisk(*) which should be treated as a regular expression i.e. matches zero or more characters. The asterisk can be escaped by a \ char in which case it should be interpreted as a regular '*' character. To summarize: the strings can contain alphabets, numbers, * and \ characters.
Input sample:

Your program should accept as its first argument a path to a filename. The input file contains two comma delimited strings per line. E.g.

Hello,ell
This is good, is
CodeEval,C*Eval
Old,Young

Output sample:

If the second string is indeed a substring of the first, print out a 'true'(lowercase), else print out a 'false'(lowercase), one per line. E.g.

true
true
true
false

'''
