from sys import argv
#import os,math,ast,itertools

file_name = argv[1]
fp = open(file_name,'r+')

contents = [list(map(int,line.strip('\n').split(',')))  for line in fp]
#print (contents)

if __name__=='__main__':
    for item in contents:
        num,p1,p2=item[0],item[1],item[2]
        print (str((bin(int(num))[-(int(p1))] == bin(int(num))[-(int(p2))])).lower())

'''
 Given a number n and two integers p1,p2 determine if the bits in position p1 and p2 are the same or not. Positions p1 and p2 are 1 based.
Input sample:
86,2,3
125,1,2

The first argument will be a path to a filename containing a comma separated list of 3 integers, one list per line. E.g.
Output sample:
true
false

Print to stdout, 'true'(lowercase) if the bits are the same, else 'false'(lowercase). E.g.
'''
