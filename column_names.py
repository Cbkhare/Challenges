#In case data is passed as a parameter

from sys import argv
#from itertools import permutations 
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [int(line.strip('\n')) for line in fp]

#print (contents)

chars = {}
for i in range(97,123):
    chars[i-96] = (chr(i)).upper()
    
for item in contents:
    stack = []
    num =item
    while num != 0.0:
        if num <= 26:
            #print (num)
            stack.append(chars[int(num)])
            num = num - num
        else:
            if num%26 == 0.0:
                stack.append('Z')
                num = (num-26)/26
                #print (num)
            else:
                divisor  = 0
                while (num-divisor)%26 != 0.0:
                    divisor +=1
                num = (num-divisor)/26
                #print (num)
                stack.append(chars[divisor])
    stack.reverse()
    print (''.join(stack))

            

'''
Column Names
Sponsoring Company:

  
Challenge Description:

Microsoft Excel uses a special convention to name its column headers. The first 26 columns use the letters 'A' to 'Z'. Then, Excel names its column headers using two letters, so that the 27th and 28th column are 'AA' and 'AB'. After 'ZZ', Excel uses three letters.

Write a function that takes as input the number of the column, and returns its header. The input will not ask for a column that would be greater than 'ZZZ'.
Input sample:

The first argument is a path to a file. Each line of the input file contains one test case represented by one integer.

52
3702
702

Output sample:

For each test case your program must print one line containing the Excel column heading corresponding to the integer in the input.

AZ
ELJ
ZZ

Constraints:

    The number of test cases is 40.
    The input will not ask for a column that would be greater than 'ZZZ'.

'''
