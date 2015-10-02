from sys import argv
#from itertools import permutations
#from operator import itemgetter
#from re import search


file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n') for line in fp]
#print (contents)


for item in contents:
    print (item.lower())
