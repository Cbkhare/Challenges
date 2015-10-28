
#In case data is passed as a parameter

from sys import argv, getsizeof
#from operator import itemgetter
#import re
#import math
from itertools import permutations, product
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n') for line in fp]

t_dict = {
'0':'0',
'1':'1',
'2':'abc',
'3':'def',
'4':'ghi',
'5':'jkl',
'6':'mno',
'7':'pqrs',
'8':'tuv',
'9':'wxyz'
    }

for item in contents:
    item = [t_dict[it] for it in list(item)]
    #print (''.join(list(product(*item))))
    words= product(*item)
    stack = []
    for word in words:
        stack.append(''.join(word))
    print (','.join(stack))
    
