from sys import argv
#import re, math, ast
from operator import itemgetter

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n') for line in fp]
content = [item.split(' ') for item in contents]
#for i in range(0,8):
 #   contents = fp.readline().split()
#print (contents)

def arrange_dict(lst):
    a_dict = {}
    for i in range(1,len(lst)):  #to exclude int at first position
        a_dict[lst[i]]=len(lst[i])
    sorted_list = sorted(a_dict.items(),key=itemgetter(1)) #RESULT WILL BE A LIST
    sorted_list.reverse()  # if itemgetter is not specified dict will sorted 
    #print (a_dict,'\n',sorted_list)        #according to the key
    for i in range(int(lst[0])):
        print (sorted_list[i][0])
arrange_dict(contents)

#TRY TO FINDOUT TO SORT A DICT WITH RESULT AS A DICT
'''
Longest Lines

Challenge Description:

Write a program which reads a file and prints to stdout the specified number of the longest lines that are sorted based on their length in descending order.
Input sample:

Your program should accept a path to a file as its first argument. The file contains multiple lines. The first line indicates the number of lines you should output, the other lines are of different length and are presented randomly. You may assume that the input file is formatted correctly and the number in the first line is a valid positive integer.

For example:

2
Hello World
CodeEval
Quick Fox
A
San Francisco

Output sample:

Print out the longest lines limited by specified number and sorted by their length in descending order.

For example:

San Francisco
Hello World'''
