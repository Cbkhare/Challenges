from sys import argv
from itertools import cycle, chain
#import os,math,ast,itertools

file_name = argv[1]
fp = open(file_name,'r+')

contents = [list(map(int,line.strip('\n').split(' '))) for line in fp]
#track    = [list(map(int,item.split(' '))) for line in contents for item in line]

#print (contents)# '\n', track)


def magic(num):
     lst = [item for item in num]
     c_lst,ct=lst,0
     pop_lst = []
     for i in range(len(lst)):
          val = c_lst[ct]
          while 4*val >= len(c_lst) or ct >= len(c_lst) :
               c_lst= list(chain(c_lst,c_lst))
          if c_lst[val+ct] !=0 and c_lst[val+ct] != val:
               if c_lst[val+ct] not in pop_lst:     #if item is already not refrenced 
                    pop_lst.append(c_lst[val+ct])
                    ct+=val
               else:
                    break
          else:
               break
     if len(pop_lst)== len(num):
          return True
     else:
          return False
     
if __name__ == '__main__':
     for item in contents:
          stack = []
          for num in range(item[0],item[1]+1):
               c_num = list(map(int,list(str(num))))
               #print (c_num,num)
               check = magic(c_num)
               if check:
                    stack.append(num)
          if len(stack)>0:
               print (str(stack).replace('[','').replace(']','').replace(',',' '))
          else:
               print ('-1')
               
'''
Magic Numbers
Sponsoring Company:

  
Challenge Description:

There are two wizards, one good and one evil. The evil wizard has captured the princess. The only way to defeat the evil wizard is to recite a set of magic numbers. The good wizard has given you two numbers, A and B. Find every magic number between A and B, inclusive.

A magic number is a number that has two characteristics:

    No digits repeat.
    Beginning with the leftmost digit, take the value of the digit and move that number of digits to the right. Repeat the process again using the value of the current digit to move right again. Wrap back to the leftmost digit as necessary. A magic number will visit every digit exactly once and end at the leftmost digit.

For example, consider the magic number 6231.

    Start with 6. Advance 6 steps to 3, wrapping around once (6→2→3→1→6→2→3).
    From 3, advance to 2.
    From 2, advance to 1.
    From 1, advance to 6.

Input sample:

The input is a file with each line representing a test case. Each test case consists of two integers A and B on a line, separated by spaces. For all test cases 1 <= A <= B <= 10000.

10 100
8382 8841

Output sample:

For each test case print all magic numbers between A and B, inclusive, on one line, separated by spaces. If there is no magic number between A and B, print -1.

13 15 17 19 31 35 37 39 51 53 57 59 71 73 75 79 91 93 95 97
-1

Constraints:

    The number of test cases is 20.
'''
