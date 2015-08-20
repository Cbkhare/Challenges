import sys
#from itertools import chain, combinations

file_name = sys.argv[1]
fp = open(file_name, 'r+')
contents = [line.strip('\n').split(',') for line in fp]

print (contents)
