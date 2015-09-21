#In case data is passed as a parameter

from sys import argv
import re

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n') for line in fp]

#print (contents)

for item in contents:

    junk = list(item)

    i =2
    j =0

    stack = []
    s = 0 
    while (i-j)*2 <= len(item) and j < len(item):

        stat = i        
        #print (junk[j:i],j,i)
        stat_j = j
        while (stat+stat-stat_j) <= len(item):
            
            #print (junk[j:i],junk[stat:stat+stat-stat_j])
            
            if junk[j:i] == junk[stat:stat+stat-stat_j] and \
               len(junk[j:i])*[' '] != junk[j:i] :

                if len(junk[j:i]) > s: 
                    stack= junk[j:i] 
                    s = len(junk[j:i])
            stat +=1
            stat_j +=1 
            
        if (i-j)*2 >= len(item)-1:
            #print (j,i)
            j +=1
            i = j+2
            continue
        i += 1
        
    if stack != []:
        #print (stack)
        print (str(stack).replace(', ','').replace('[','').replace(']','').replace('\'','').replace(' ',''))
    else:
        print ('NONE')

    '''

View All Challenges
Repeated Substring

Challenge Description:

You are to find the longest repeated substring in a given text. Repeated substrings may not overlap. If more than one substring is repeated with the same length, print the first one you find.(starting from the beginning of the text).
NOTE: The substrings can't be all spaces.
Input sample:

Your program should accept as its first argument a path to a filename. The input file contains several lines. Each line is one test case. Each line contains a test string. E.g.

banana
am so uniqe

Output sample:

For each set of input produce a single line of output which is the longest repeated substring. If there is none, print out the string NONE. E.g.

an
NONE
'''
