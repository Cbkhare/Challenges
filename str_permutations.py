#In case data is passed as a parameter

from sys import argv
from itertools import permutations 
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n') for line in fp]

#print (contents)

for item in contents:
    #print (item)

    p_tups= sorted(permutations(item,len(item)))
    stack = []
    for tups in p_tups:
        stack.append(''.join(tups))

    print (','.join(stack))
        
              
'''

String Permutations
Sponsoring Company:

  
Challenge Description:

Write a program which prints all the permutations of a string in alphabetical order. We consider that digits < upper case letters < lower case letters. The sorting should be performed in ascending order.
Input sample:

Your program should accept a file as its first argument. The file contains input strings, one per line.

For example:

hat
abc
Zu6


Output sample:

Print to stdout the permutations of the string separated by comma, in alphabetical order.

For example:
aht,ath,hat,hta,tah,tha
abc,acb,bac,bca,cab,cba
6Zu,6uZ,Z6u,Zu6,u6Z,uZ6


'''
