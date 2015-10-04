#In case data is passed as a parameter

from sys import argv
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [ line.strip('\n').split(' ') for line in fp]

#print (contents)

for item in contents:

    strng = item
    mack = []
    for i in range(len(strng)):
        stack = []
        stack.append(strng[i])
        back = strng[i:]
        for j in range(1,int(len(back)/2)):
            #print (stack,strng [i+1:i+len(stack)])
            stack.append(back[j])
            if stack == back[j+1:j+len(stack)+1]:
                mack=stack
                break
            #print (stack,back[j+1:j+len(stack)+1])
    
    if len(mack) == 2 and mack[0]==mack[1]: mack.pop(1)
    
    print (' '.join(mack))


'''

Given a sequence, write a program to detect cycles within it.
Input sample:

Your program should accept as its first argument a path to a filename containing a sequence of numbers (space delimited). The file can have multiple such lines. E.g

2 0 6 3 1 6 3 1 6 3 1
3 4 8 0 11 9 7 2 5 6 10 1 49 49 49 49
1 2 3 1 2 3 1 2 3


Output sample:

Print to stdout the first cycle you find in each sequence. Ensure that there are no trailing empty spaces on each line you print. E.g.

6 3 1
49
1 2 3


The cycle detection problem is explained more widely on wiki
Constrains:
The elements of the sequence are integers in range [0, 99]
The length of the sequence is in range [0, 50]


'''
