
from sys import argv
#from itertools import permutations
#from operator import itemgetter
#from re import search


file_name = argv[1]
fp = open(file_name,'r+')

contents = []

for line in fp:
    contents.append(int(line.strip('\n')))
print (sum(contents))
