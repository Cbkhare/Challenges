from sys import argv
#import os,math,ast,itertools

file_name = argv[1]
fp = open(file_name,'r+')

#contents = [list(map(int,line.strip('\n').split(',')))  for line in fp]

#print (contents)

def fibo(num):
    a,b,c=0,1,0
    if num == 0: return 0
    elif num == 1: return 1
    else: return (fibo(num-1)+fibo(num-2))

'''    for i in range(0,num-1):   #since we are starting from 0,1,1 i.e 3rd pos
        c = a + b
        a,b=b,c 
    return (c)
        '''
        

if __name__=='__main__':
    for item in [item for item in fp.read().split()]:
        print (fibo(int(item)))

'''
 The Fibonacci series is defined as: F(0) = 0; F(1) = 1; F(n) = F(n–1) + F(n–2) when n>1. Given an integer n≥0, print out the F(n).
Input sample:

The first argument will be a path to a filename containing integer numbers, one per line. E.g.

5
12

Output sample:

Print to stdout, the fibonacci number, F(n). E.g.

5
144'''
