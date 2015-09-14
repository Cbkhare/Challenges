from sys import argv
import re

file_name = argv[1]
fp = open(file_name,'r+')

contents = [int(line.strip('\n')) for line in fp]

#print (contents)

box = [1,3,5]

for item in contents:
    summ = item        
    coins  = 0
    boom = [i for i in box]

    while summ>0:
        
        m = max(boom)

        while summ >= m:
            summ -= m
            coins +=1
        #print (m)
        boom.remove(m)
    print (coins)

'''

 You are given 3 coins of value 1, 3 and 5. You are also given a total which you have to arrive at. Find the minimum number of coins to arrive at it.
Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file contains a positive integer number which represents the total you have to arrive at. E.g.

11
20

Output sample:

Print out the minimum number of coins required to arrive at the total. E.g.

3
4
'''
