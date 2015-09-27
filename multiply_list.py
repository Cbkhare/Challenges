#In case data is passed as a parameter

from sys import argv
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [ line.strip('\n').split('|') for line in fp]

#print (contents)

for item in contents:

    part1 = list(item[0].split(' '))
    part1.remove('')
    part2 = list(item[1].split(' '))
    part2.remove('')

    stack = []

    for i in range(len(part1)):  #assumed length of both list are equal

        stack.append(int(part1[i])*int(part2[i]))
        
    print (str(stack).replace('[','').replace(']','').replace(', ',' '))

'''
Multiply Lists

Challenge Description:

You have 2 lists of positive integers. Write a program which multiplies corresponding elements in these lists.
Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

9 0 6 | 15 14 9
5 | 8
13 4 15 1 15 5 | 1 4 15 14 8 2

The lists are separated with a pipe char, numbers are separated with a space char.
The number of elements in lists are in range [1, 10].
The number of elements is the same in both lists.
Each element is a number in range [0, 99].
Output sample:

Print the result in the following way.

135 0 54
40
13 16 225 14 120 10
'''
