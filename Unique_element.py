from sys import argv
#from itertools import permutations
#from operator import itemgetter
#from re import search


file_name = argv[1]
fp = open(file_name,'r+')

contents = [ line.strip('\n').split(',') for line in fp]

#print (contents)


for item in contents:
    box = list(map(int,set(item)))
    box.sort()
    print (str(box).replace('[','').replace(']','').replace(', ',','))

'''

 You are given a sorted list of numbers with duplicates. Print out the sorted list with duplicates removed.
Input sample:

1,1,1,1,1,2,3,3,4,5,5

File containing a list of sorted integers, comma delimited, one per line. E.g.
Output sample:
1,2,3,4,5
Print out the sorted list with duplicates removed, one per line.
'''
