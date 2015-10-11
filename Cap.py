
#In case data is passed as a parameter

from sys import argv
#from itertools import permutations
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n').split(' ') for line in fp]

for item in contents:
    lst = [] 
    for word in item:
        lst.append(word[0].upper()+word[1:])

    print (' '.join(lst))
