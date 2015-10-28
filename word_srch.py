#In case data is passed as a parameter
from sys import argv, getsizeof
#from operator import itemgetter
#import re
#import math
#from itertools import permutations, product
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n') for line in fp]

strng = 'ABCESFCSADEE'

for item in contents:
    lst = list(item)
    ts = list(strng)
    found = True
    for l in lst:

        if l in ts:
            i = ts.index(l)
            ts = ts[i+1:]
        else:
            found = False
            break
    if found:
        print (True)
    else:
        print (False)
