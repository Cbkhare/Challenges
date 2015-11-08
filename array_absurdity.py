from sys import argv

file_name = argv[1]
fp = open(file_name, 'r+')

#contents = [line.strip('\n').split(';') for line in fp]

for line in fp:
    if line =='':
        ('\n')
        continue
    n, tup = line.split(';')[0],tuple(map(int,line.strip('\n').split(';')[1].split(',')))
    #print (n,tup)

    for i in range(int(n)):
        if tup.count(i)>1:
            print (i)
            break


'''
Array Absurdity

Challenge Description:

Imagine we have an immutable array of size N which we know to be filled with integers ranging from 0 to N-2, inclusive. Suppose we know that the array contains exactly one duplicated entry and that duplicate appears exactly twice. Find the duplicated entry. (For bonus points, ensure your solution has constant space and time proportional to N)
Input sample:
5;0,1,2,3,0

20;0,1,10,3,2,4,5,7,6,8,11,9,15,12,13,4,16,18,17,14

Your program should accept as its first argument a path to a filename. Each line in this file is one test case. Ignore all empty lines. Each line begins with a positive integer(N) i.e. the size of the array, then a semicolon followed by a comma separated list of positive numbers ranging from 0 to N-2, inclusive. i.e eg.
Output sample:
0
4
Print out the duplicated entry, each one on a new line eg
'''
