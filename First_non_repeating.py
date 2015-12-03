'''Write a program which finds the first non-repeated character in a string.
Input sample:

The first argument is a path to a file. The file contains strings.

For example:
yellow
tooth

Output sample:

Print to stdout the first non-repeated character, one per line.

For example:
y
h
'''

import sys

file_name = sys.argv[1]
fp = open(file_name,'r+')

#TO FIND THE CONTENTS
contents = fp.read().split()
#print (contents)  #To print elements inside the contents in a form of list

for i in range(len(contents)):
    bry = list(contents[i])
    for j in range(len(bry)):
        if bry.count(bry[j]) == 1:
            print (bry[j])  #print (bry[j],bry.count(bry[j]))
            break
    


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
