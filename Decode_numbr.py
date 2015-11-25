#In case data is passed as a parameter

from sys import argv
from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [ line.strip('\n') for line in fp]


#Genrating Alphabet dict but it is of no need since we have to print only num
#of ways not letter
'''
Alpha = list(ascii_uppercase)
Alpha_dict = {}
for i in range(len(Alpha)):
    Alpha_dict[i+1] = Alpha[i]
del Alpha

print (Alpha_dict)
'''

#print (contents)
for item in contents:

    count = 1  #by default there will be atleast one way where each digit 
               #represents a char in Alpha_dict
    
    #Finding more ways
    if len(item)>1:

        run =2
        if len(item)==3: run=1
        while run <= int(len(item)/2) :    #i.e untill it make pairs to end of list
            i = 1
            while i*run <= len(item):
                
                check =  i*run
                j = 0   
                while j+check <= len(item):

                    stack = item[j:j+check]
                    #print (stack)          #to check
                    x = 0
                    status = 0
                    while x+2 <= len(stack):
                        
                        #print (stack[x:x+2],'ok')   #to check
                        if int(stack[x:x+2]) in range(1,27):
                            status += 1
                        #print (status)              #to check
                        if status*2 == len(stack):
                            count +=1
                            #print (count)           #to check
                            #print ('added')         #to check
                        x+=2
                    j+=1
                i+=1
            run +=2
    print (count)

'''
 You are given an encoded message containing only numbers. You are also provided with the following mapping:

A : 1
B : 2
C : 3
...
Z : 26

Given an encoded message, count the number of ways it can be decoded.
Input sample:

Your program should accept as its first argument a path to a filename.
Each line in this file is a test-case and contains an encoded message of
numbers. E.g.

12
123

You may assume that the test cases contain only numbers.
Output sample:

Print out the different number of ways it can be decoded. E.g.
2
3

NOTE: 12 could be decoded as AB(1 2) or L(12). Hence the number of ways to decode 12 is 2.
Submit Solution
'''
        

        
