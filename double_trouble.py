
#In case data is passed as a parameter

from sys import argv, getsizeof
#from operator import itemgetter
#import re
#import math
#from itertools import permutations
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n')  for line in fp]


for item in contents:
    p1 = list(item)[:int(len(item)/2)]
    p2 = list(item)[int(len(item)/2):]
    status = 'Fine'
    charge = 1
    for i in range(len(p1)):
        if p1[i] == '*' and p2[i] == '*':
            charge *= 2
            continue
        
        if p1[i] != p2[i]:
            
            if (p1[i] != '*' and  p2[i] == '*') or (p1[i] == '*' and  p2[i] != '*'):
                charge *= 1
            else:
                status = 'NotFine'
                break
        if status == 'NotFine':
            break

    if status == 'NotFine':
        print (0)
    else:
        print (charge)

'''
Double trouble

Challenge Description:

Historians have discovered a mysterious lost code that until this day remains undeciphered. Looks like the code dates back to the 5th century AD. Scientists were trying to decipher the code, which could reveal many details about our ancestors’ life, but they failed. Could you help them?
According to the analysis, there can be only 2 letters in the code: A and B. All messages are transmitted in a form of two equal parts (ABAB, AAAA, BABA, and so on).
Some messages are so mutilated that scientists need to know how many correct variants of the messages might exist to decide whether it would make sense to decipher their meaning, and how long it would take. Therefore, you need to calculate the number of possible correct variants for each message.
Input sample:

The first argument is a path to a file. Each line includes a test case containing one message that includes three symbols:
A and B – deciphered code;
* - lost letter;

For example:
ABA*
BAA*
A*A*
A*BA**


Output sample:

Print the number of possible correct variants of each message.

For example:
2
0
1
2
Constraints:


    A message may be from 2 to 70 letters long.
    All messages have an even number of letters.
    Some messages may be incorrect. In such cases, print 0.
    The number of test cases is 40.

'''
