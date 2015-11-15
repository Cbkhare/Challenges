from sys import argv
#from itertools import combinations
#from operator import itemgetter
#from re import search


file_name = argv[1]
fp = open(file_name,'r+')

contents = [list(map(int,line.strip('\n').split(' '))) for line in fp]
#print (contents)


for item in contents:
    stack = []
    count = 0
    for i in range(1,len(item)-1):        #to exlcude the 1st elem which has
        diff = abs(item[i]-item[i+1])     #the len of the list only 
        #print (diff)        
        if diff in range(1,item[0]):   # 1 to n-1
            if diff not in stack:
                stack.append(diff)
    #print (stack)
    if len(stack) == item[0]-1:    #excluding 1st and then diff of remaning item
        print ('Jolly')
    else:
        print ('Not jolly')
        
'''
Jolly Jumpers

Challenge Description:

Credits: Programming Challenges by Steven S. Skiena and Miguel A. Revilla

A sequence of n > 0 integers is called a jolly jumper if the absolute values of the differences between successive elements take on all possible values 1 through n - 1. eg.

1 4 2 3 

is a jolly jumper, because the absolute differences are 3, 2, and 1, respectively. The definition implies that any sequence of a single integer is a jolly jumper. Write a program to determine whether each of a number of sequences is a jolly jumper.
Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file is one test case. Each test case will contain an integer n < 3000 followed by n integers representing the sequence. The integers are space delimited.

For example:
4 1 4 2 3
3 7 7 8
9 8 9 7 10 6 12 17 24 38
6 41 42 44 47 51 56
3 1 2 4

Output sample:

For each line of input generate a line of output saying 'Jolly' or 'Not jolly'.

For example:

Jolly
Not jolly
Not jolly
Jolly
'''
