
#In case data is passed as a parameter

from sys import argv, getsizeof
#from operator import itemgetter
#import re
#import math
#from itertools import permutations
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n').split(';') for line in fp]

number= {
    'zero'   :0,
    'one'    :1,
    'two'    :2,
    'three'  :3,
    'four'   :4,
    'five'   :5,
    'six'    :6,
    'seven'  :7,
    'eight'  :8,
    'nine'   :9,
}


for item in contents:

    stack = []

    for words in item:

        if words.lower() in number:
            stack.append(str(number[words.lower()]))
    print (''.join(stack))
            
    


