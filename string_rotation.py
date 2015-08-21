from sys import argv
#from itertools import permutations
#from operator import itemgetter
#from re import search


file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n').split(',') for line in fp]
#print (contents)



def gen_rotations(tupl,strng):
    j,p,up= 0,[],tupl
    while p != tupl and j<=len(tupl):   #  
        p = []
        for i in range(len(tupl)):
            #print (i,up[i-1])
            p.append(up[i-1])
        #print (p)
        up = p
        j += 1
        if tuple(p) == strng:
            return True

    return False
        
            
for item in contents:
    strng, tup = (),()
    for i in range(len(item[0])):
        tup += (item[0][i],)
        strng +=  (item[1][i],)

    print (gen_rotations (tup,strng))
'''
String Rotation

Challenge Description:

You are given two strings. Determine if the second string is a rotation of the first string.
Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file contains two comma separated strings. E.g.

Hello,lloHe
Basefont,tBasefon

Output sample:

Print out True/False if the second string is a rotation of the first. E.g.

True
True
'''
