import sys
from itertools import chain

file_name = sys.argv[1]
fp = open(file_name, 'r+')
contents = [line.strip('\n') for line in fp]

#print (contents)

def triangle(d):
     if d == 1: return [1]
     elif d==2: return [1,1,1]
     else:
          stack = [1,1,1]
          old_stack=[1,1]       #used to generate next stack
          for i in range(2,d):  #0,1 already icluded in stack
               cur_stack= []
               for j in range(len(old_stack)+1):
                    if j==0 or j==len(old_stack):    #for first and last value
                         cur_stack.append(1)
                    else:
                         cur_stack.append(old_stack[j]+old_stack[j-1])
               stack = list(chain(stack,cur_stack)) #joining new stack
               old_stack = cur_stack                #updating old_stack for new stack
               #print (old_stack)
          return stack
               
               
               

     
for depth in contents:
     print (str(triangle(int(depth))).replace('[','').replace(']','').replace(',',''))

'''
 A Pascals triangle row is constructed by looking at the previous row and adding the numbers to its left and right to arrive at the new value. If either the number to its left/right is not present, substitute a zero in it's place. More details can be found here: Pascal's triangle. E.g. a Pascal's triangle upto a depth of 6 can be shown as:

            1
          1   1
        1   2   1
       1  3   3   1
     1  4   6   4   1
    1  5  10  10  5   1

Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file contains a positive integer which indicates the depth of the triangle (1 based). E.g.

6

Output sample:

Print out the resulting pascal triangle upto the requested depth in row major form. E.g.

1 1 1 1 2 1 1 3 3 1 1 4 6 4 1 1 5 10 10 5 1
'''
