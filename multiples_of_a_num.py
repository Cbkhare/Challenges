from sys import argv
#import os,math,ast,itertools

file_name = argv[1]
fp = open(file_name,'r+')

contents = [list(map(int,line.strip('\n').split(',')))  for line in fp]

#print (contents)

def nearest_pow_of_2(lst):
    i,multi = 1,lst[1]
    while lst[0] > multi:
        num = lst[1]
        i +=1
        multi = num*i
    return multi
        
        

if __name__=='__main__':
    for item in contents:
        num = nearest_pow_of_2(item)
        print (num)
'''
 Given numbers x and n, where n is a power of 2, print out the smallest multiple of n which is greater than or equal to x. Do not use division or modulo operator.
Input sample:

The first argument will be a path to a filename containing a comma separated list of two integers, one list per line. E.g.

13,8
17,16

Output sample:

Print to stdout, the smallest multiple of n which is greater than or equal to x, one per line. E.g.

16
32'''
