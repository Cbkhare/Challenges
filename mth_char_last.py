import sys

file_name = sys.argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n') for line in fp]
content = [item.split(' ') for item in contents]


for item in content:
        int_g = int(item[len(item)-1])  #get the Int
        if int_g >= len(item):
            continue
        else:
            item.reverse()   #to ge the char in reverse order 
            print(item[int_g])

'''
 Write a program which determines the Mth to the last element in a list.
 
Input sample:
a b c d 4
e f g h 2
d 4

The first argument is a path to a file. The file contains the series of space delimited characters followed by an integer. The integer represents an index in the list (1-based), one per line.

For example:

Output sample:

Print to stdout the Mth element from the end of the list, one per line. If the index is larger than the number of elements in the list, ignore that input.

For example:
a
g
'''
