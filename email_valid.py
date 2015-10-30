
#In case data is passed as a parameter

from sys import argv
import re
import math
#from itertools import permutations
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [lin.strip('\n')  for lin in fp]

#print (contents)
for line in contents:
    if line == '' :
        continue 
    test = re.match(r'^"[a-z|A-Z|0-9|_|-|+|.|@]+"|[a-z|A-Z|0-9|_|-|+|.?]*@{1}[a-z|0-9]+\.{1}[a-z|0-9|-]+\.?[a-z|0-9|-]{2,}', line.lower())

    if test :
        print ('true')
    else:
        print('false')   

'''

 You are given several strings that may/may not be valid emails. You should write a regular expression that determines if the email id is a valid email id or not. You may assume all characters are from the english language.
Input sample:

Your program should accept as its first argument a filename. This file will contain several text strings, one per line. Ignore all empty lines. E.g.

foo@bar.com
this is not an email id
admin#codeeval.com
good123@bad.com


Output sample:

Print out 'true' (all lowercase) if the string is a valid email. Else print out 'false' (all lowercase). E.g.

true
false
false
true

'''
