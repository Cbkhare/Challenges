import sys
from itertools import chain, combinations

file_name = sys.argv[1]
fp = open(file_name, 'r+')
contents = [list(map(int,line.strip('\n').split(','))) for line in fp]

#print (contents)

for item in contents:
    tups = list(combinations(item,4))
    counter = 0
    for ups in tups:
        if sum(ups)==0:
            counter +=1
    print (counter)
    
    
'''
ou are given an array of integers. Count the numbers of ways in which the sum of 4 elements in this array results in zero.
Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file consist of comma separated positive and negative integers. E.g.

2,3,1,0,-4,-1
0,-1,3,-2

Output sample:

Print out the count of the different number of ways that 4 elements sum to zero. E.g.

2
1'''
