from sys import argv
#import re, math, ast, operator import itemgetter
import itertools

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n') for line in fp]
content = [item.split(',') for item in contents]

#print (content)

for item in content:
    #print (item[1],item[0])
    comb = sorted(set(itertools.product(item[1],repeat=int(item[0]))))
    #comb = sorted(comb)   #result of itertools will be tuples
    #comb.sort()          
    #print (len(comb),comb,type(comb))
    stack = []
    for value in comb:
        stack.append(''.join(value))
    print (','.join(stack))
        
            
'''
String List

Challenge Description:

Credits: Challenge contributed by Max Demian.

You are given a number N and a string S. Print all of the possible ways to write a string of length N from the characters in string S, comma delimited in alphabetical order.
Input sample:

The first argument will be the path to the input filename containing the test data. Each line in this file is a separate test case. Each line is in the format: N,S i.e. a positive integer, followed by a string (comma separated). E.g.

1,aa
2,ab
3,pop

Output sample:

Print all of the possible ways to write a string of length N from the characters in string S comma delimited in alphabetical order, with no duplicates. E.g.

a
aa,ab,ba,bb
ooo,oop,opo,opp,poo,pop,ppo,ppp
'''
