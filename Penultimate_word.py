''' Write a program which finds the next-to-last word in a string.
Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

some line with text
another line

Each line has more than one word.
Output sample:

Print the next-to-last word in the following way.

with
another
'''

import sys

file_name = sys.argv[1]
#Dual opening statement of a file to avoid moving of counter
fp = open(file_name,'r+')
fr = open(file_name,'r+')

#To read individiual lines as a list 
#l1 = fp.readline().split()
#l2 = fp.readline().split()

count = 0
for j in range(0,len(fp.readlines())):
    count +=1
    
print (count)
for i in range(0,count):
    sen = fr.readline().split()
    word = sen[len(sen)-2]
    print (word)


'''
#TO FIND THE CONTENTS INDIVIDUALLY
contents = fp.read().split()
#print (contents)  #To print elements inside the contents in a form of list
'''
'''
# To getnumber of lines
buf = mmap(fp.fileno(), 0)
num_lines = 0
readline = buf.readline
while readline():
    num_lines += 1
#print (num_lines)
'''


'''
for i in range(len(contents)):
    bry = list(contents[i])
    for j in range(len(bry)):
        if bry.count(bry[j]) == 1:
            print (bry[j])  #print (bry[j],bry.count(bry[j]))
            break
    

'''
#To read no. of lines in the filevia Buf mmap"
'''
buf = mmap.mmap(fp.fileno(), 0)
num_lines = 0
readline = buf.readline
while readline():
    num_lines += 1
#print (num_lines)

'''
    
'''

#To Get No. Of line
num_lines = int(sum(1 for line in contents))
print (num_lines)


data = []
for line in contents:
    print (line)
    int_num = line.strip().split()
    intg = [int(x) for x in int_num]
    data.append(intg)
print (data[0])

buf = mmap.mmap(fp.fileno(), 0)
lines = 0
readline = buf.readline
while readline():
    lines += 1
print (lines)


++++++++++++++++++++++++++
num_lines = sum(1 for line in fp)
print (num_lines)'''
