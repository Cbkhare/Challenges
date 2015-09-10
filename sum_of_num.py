import sys

file_name = sys.argv[1]
fp = open(file_name,'r+')

#to find contents
contents = fp.read().split()

for i in range(len(contents)):
    num =list(map(int,list(contents[i])))
    print (sum(num))

'''
Input sample:

The first argument will be a path to a filename containing positive integers, one per line. E.g.

23
496

Output sample:

Print to stdout, the sum of the numbers that make up the integer, one per line. E.g.

5
19'''
