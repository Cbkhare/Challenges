
#In case data is passed as a parameter

from sys import argv, getsizeof
#from operator import itemgetter
#import re
#import math
#from itertools import permutations
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n').split(', ')  for line in fp]


for item in contents:
    p1 = list(item[0])
    p2 = list(item[1])
    
    for w in p2:
        if w in p1:
            while w in p1:
                p1.remove(w)
        else:
            continue
    print (''.join(p1))

'''

 Write a program which removes specific characters from a string.
Input sample:

The first argument is a path to a file. The file contains the source strings and the characters that need to be scrubbed. Each source string and characters you need to scrub are delimited by comma.

For example:

how are you, abc
hello world, def
malbororo roro, or

Output sample:

Print to stdout the scrubbed strings, one per line. Ensure that there are no trailing empty spaces on each line you print.

For example:

how re you
hllo worl
malb
'''
