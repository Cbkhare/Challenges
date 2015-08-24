import sys
from itertools import chain, combinations

file_name = sys.argv[1]
fp = open(file_name, 'r+')
contents = [line.strip('\n').split(';') for line in fp]

#print (contents)


for item in contents:
     s= int(item[1])
     data = list(map(int,item[0].split(',')))
     tup = list(combinations(data,2))
     stack = []
     for stuf in tup:
          if (sum(stuf)) == s:
               stack.append(str(list(stuf)).replace(', ',','))
     if len(stack)==0:
          print ('NULL')
     else:
          
          print (str(stack).replace('[','').replace(']','').replace(', ',';').replace('\'',''))


'''



You are given a sorted array of positive integers and a number 'X'. Print out all pairs of numbers whose sum is equal to X. Print out only unique pairs and the pairs should be in ascending order
Input sample:

Your program should accept as its first argument a filename. This file will contain a comma separated list of sorted numbers and then the sum 'X', separated by semicolon. Ignore all empty lines. If no pair exists, print the string NULL e.g.

1,2,3,4,6;5
2,4,5,6,9,11,15;20
1,2,3,4;50

Output sample:

Print out the pairs of numbers that equal to the sum X. The pairs should themselves be printed in sorted order i.e the first number of each pair should be in ascending order. E.g.

1,4;2,3
5,15;9,11
NULL
'''
