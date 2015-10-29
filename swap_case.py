
#In case data is passed as a parameter

from sys import argv, getsizeof
#from operator import itemgetter
#import re
#import math
#from itertools import permutations
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n') for line in fp]

for item in contents:
    stack = []

    for it in item:
        if it.lower()==it:
            stack.append(it.upper())
        else:
            stack.append(it.lower())
    print (''.join(stack))


'''
 Write a program which swaps letters' case in a sentence. All non-letter characters should remain the same.
Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

Hello world!
JavaScript language 1.8
A letter

Output sample:

Print results in the following way.

hELLO WORLD!
jAVAsCRIPT LANGUAGE 1.8
a LETTER
'''
