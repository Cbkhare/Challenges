from sys import argv
#from itertools import permutations
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n').split(';') for line in fp]

for item in contents:

    lst , s = item[0].split(','), int(item[1])
    stack = []
    while len(lst)-int(s) >=0:
        temp = lst[:s]
        temp.reverse()
        stack += temp
        lst = lst[s:]
    stack += lst   
    print (','.join(stack))


'''

Challenge Description:

Given a list of numbers and a positive integer k, reverse the elements of the list, k items at a time. If the number of elements is not a multiple of k, then the remaining items in the end should be left as is.
Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file contains a list of numbers and the number k, separated by a semicolon. The list of numbers are comma delimited. E.g.

1,2,3,4,5;2
1,2,3,4,5;3

Output sample:

Print out the new comma separated list of numbers obtained after reversing. E.g.

2,1,4,3,5
3,2,1,4,5

'''
