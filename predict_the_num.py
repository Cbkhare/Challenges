#In case data is passed as a parameter

from sys import argv
#from itertools import permutations 
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [int(line.strip('\n')) for line in fp]

#print (contents)

for num in contents:
    n = num #since it is a zero based list
    if n==0:
        print (0)
        continue
    flip = 0
    while n >=0:
        i = 0
        while pow(2,i)<=n:
            i+=1
        p =i-1
        n = n - pow(2,p)
        flip +=1       
        if n <=0 : break
    #print (flip)
    while flip >0:
        if n==0:
            n=1
        elif n==1:
            n=2
        elif n==2:
            n=0
        flip -=1

        
    print (n)

#LOGIC
#break the sequence in power of 2^p, find the flips till 2^0 and you reach the 0th elem
#from 0th elem i.e make flips untill flip count is zero

'''

Predict the Number

Challenge Description:

The sequence "011212201220200112 ..." is constructed as follows:
first goes 0, and then the following action is repeated: existing part is added to the right, but 0 is replaced with 1, 1 with 2, and 2 with 0.

0 -> 01 -> 0112 -> 01121220 -> ...

Write an algorithm that determines what number is on the N-th position in the sequence.
Input sample:

Your program should accept a path to a filename as its first argument. Each line in the file contains a number N.

For example:
0
5
101
25684


Output sample:

Print out a number that is on the N-th position in the sequence.
0
2
1
0
Constraints:

    0 <= N <= 3000000000.
'''
    
