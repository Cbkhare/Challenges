
#In case data is passed as a parameter

from sys import argv, getsizeof
#from operator import itemgetter
#import re
#import math
#from itertools import permutations
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [list(map(int,line.strip('\n').split(' '))) for line in fp]

for item in contents:
    
    F = item[0]
    B = item[1]
    stack = []
    for i in range(1,item[2]+1):

        if (i%F == 0 and i%B != 0):
            stack.append('F')
        elif (i%B == 0 and  i%F != 0):
           stack.append('B')
        elif (i%F ==0 and i%B == 0):
            stack.append('FB')
        else:
            stack.append(str(i))
    print (' '.join(stack))
            
    


