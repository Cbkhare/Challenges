#In case data is passed as a parameter

from sys import argv
#from string import ascii_uppercase
import re
file_name = argv[1]
fp = open(file_name,'r+')

contents = [ line.strip('\n').split(':') for line in fp]

#print (contents)

for item in contents:

    part1 = list(item[0].split(' '))
    part1.remove('')

    part2 = list(item[1].split(','))
    #print (part1,part2)

    for parts in part2:

        p = list(map(int,list(parts.split('-'))))   #try using regex
        #print (p)
        var = part1[p[0]]
        part1[p[0]] = part1[p[1]]
        part1[p[1]] = var
        
    print (' '.join(part1))


'''
 You are given a list of numbers which is supplemented with positions that have to be swapped.
Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

1 2 3 4 5 6 7 8 9 : 0-8
1 2 3 4 5 6 7 8 9 10 : 0-1, 1-3

As you can see a colon separates numbers with positions.
Positions start with 0.
You have to process positions left to right. In the example above (2nd line) first you process 0-1, then 1-3.
Output sample:

Print the lists in the following way.

9 2 3 4 5 6 7 8 1
2 4 3 1 5 6 7 8 9 10
'''
