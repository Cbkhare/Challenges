#In case data is passed as a parameter

from sys import argv
#from itertools import permutations 
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n').split(',') for line in fp]

#print (contents)

def word_chain(sh,bo):
    
    for b in bo:
        #print (sh,bo,sh[-1][-1],b[0])
        if sh[-1][-1] == b[0] and sh[-1] != b :
            
            if b not in sh : sh.append(b)
            #print (bo)
            if len(bo) > 1:
                nbo = [l for l in box if l !=b]
                #print(nbo)
                word_chain(sh,nbo)
            else:
                return sh
    return sh
    #pass


for item in contents:

    stack = []
    lenth = 0
    for word in item:
        shut = [word]
        box  = [ltr for ltr in item if ltr!=word]
        s_shut = word_chain(shut,box)
        #print (s_shut)
        #stack.append(s_shut)
        if len(s_shut) > lenth:
            lenth = len(s_shut)  
    #print (stack)
    if lenth == 1:
        print ('NONE')
    else:
        print (lenth)




#to find the word chain uncomment every stack

'''
Word chain

Challenge Description:

In this challenge, we suggest playing "Word chain" - a well-known game in which players come up with words that begin with the letter that the previous word ended with. Your task is to determine the maximum length of a chain that can be created from a list of words.
Input sample:

Your program should accept a path to a filename as its first argument. Each line of the file contains a list of words separated by comma.

For example:

soup,sugar,peas,rice
ljhqi,nrtxgiu,jdtphez,wosqm
cjz,tojiv,sgxf,awonm,fcv


Output sample:

Print out the length of the longest chain or print out "None" if there is no chain.

For example:
4
NONE
2
Constraints:

    The length of a list of words is in a range from 4 to 35.
    A word in a list is represented by a random lowercase ASCII string with the length from 3 to 7 letters.
    The words in a list do not repeat.
'''

        


            
