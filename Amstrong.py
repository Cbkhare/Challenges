
#In case data is passed as a parameter

from sys import argv
#from itertools import permutations
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n') for line in fp]


for item in contents:
    nth = len(item)
    summ = 0

    for i in range(len(item)):

        summ += pow(int(item[i]),nth)
    
    if summ == int(item):
        print (True)
    else:
        print (False)
     

'''
 An Armstrong number is an n-digit number that is equal to the sum of the n'th powers of its digits. Determine if the input numbers are Armstrong numbers.
Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file has a positive integer. E.g.
6
351
153


Output sample:

Print out True/False if the number is an Armstrong number or not. E.g.
True
False
True
'''
