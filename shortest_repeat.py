#In case data is passed as a parameter

from sys import argv
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [ line.strip('\n') for line in fp]

#print (contents)

for item in contents:

    strng = list(item)
    stack = [strng[0]]
    
    for i in range(1,len(strng)):

        stack.append(strng[i])

        #print (stack,strng [i+1:i+len(stack)])

        if stack == strng [i+1:i+len(stack)+1]:
            break       

    repeat = len(stack)
    
    if len(stack) == 2 and stack[0]==stack[1]: repeat =1
    
    print (repeat)


'''

 Write a program to determine the shortest repetition in a string.
A string is said to have period p if it can be formed by concatenating one or more repetitions of another string of length p. For example, the string "xyzxyzxyzxyz" has period 3, since it is formed by 4 repetitions of the string "xyz". It also has periods 6 (two repetitions of "xyzxyz") and 12 (one repetition of "xyzxyzxyzxyz").
Input sample:

Your program should accept as its first argument a path to a filename. Each line will contain a string of up to 80 non-blank characters. E.g.

abcabcabcabc
bcbcbcbcbcbcbcbcbcbcbcbcbcbc
dddddddddddddddddddd
adcdefg

Output sample:

Print out the smallest period of the input string. E.g.

3
2
1
7
'''
