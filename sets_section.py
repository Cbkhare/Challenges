from sys import argv
#from itertools import permutations
#from operator import itemgetter
#from re import search


file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n').split(';') for line in fp ]

#print (contents)


for item in contents:
    i = set(list(map(int,item[0].split(','))))
    j = set(list(map(int,item[1].split(','))))
    box = i.intersection(j)
    #print (i,j,box)

    if len(box) != 0:
        box = sorted(box)
        print (str(box).replace('[','').replace(']','').replace(', ',','))
    else:
        print('')


'''

 You are given two sorted list of numbers (ascending order).
 The lists themselves are comma delimited and the two lists
 are semicolon delimited. Print out the intersection of these two sets.
Input sample:

File containing two lists of ascending order sorted integers,
comma delimited, one per line. E.g.

1,2,3,4;4,5,6
20,21,22;45,46,47
7,8,9;8,9,10,11,12

Output sample:

Print out the ascending order sorted intersection of the two lists,
one per line. Print empty new line in case the lists have no intersection.
E.g.

4

8,9
'''
