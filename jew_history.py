from sys import argv
#import os,math,ast,itertools

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n').split(',') for line in fp]
#track    = [list(map(int,item.split(' '))) for line in contents for item in line]

#print (contents)# '\n', track)

def poper(junk):
     np, ne,new_lst,pos = [i for i in range(junk[0])],junk[1]-1,[],0    #list no. of people, execution step
     for i in range(0,len(np)):
          cur_lst = np
          pos += ne 
          if pos >= len(cur_lst):
               while pos >= len(cur_lst):
                    pos = pos-len(cur_lst)
               #print (pos,i,'e',cur_lst,new_lst)
               new_lst.append(cur_lst.pop(pos))
          else:
               #print (pos,i,'d',cur_lst,new_lst)
               new_lst.append(cur_lst.pop(pos))
     print (' '.join(list(map(str,new_lst))))
               
     
if __name__ == '__main__':
     for item in contents:
          poper(list(map(int,item)))
          #print (list(map(int,item)))
        

'''
 Flavius Josephus was a famous Jewish historian of the first century, at the time of the destruction of the Second Temple. According to legend, during the Jewish-Roman war he was trapped in a cave with a group of soldiers surrounded by Romans. Preferring death to capture, the Jews decided to form a circle and, proceeding around it, to kill every j'th person remaining until no one was left. Josephus found the safe spot in the circle and thus stayed alive.
Write a program that returns a list of n people, numbered from 0 to n-1, in the order in which they are executed.
Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file contains two comma separated positive integers n and m, where n is the number of people and every m'th person will be executed. E.g.

10,3
5,2

Output sample:

Print out the list of n people (space delimited) in the order in which they will be executed. E.g.

2 5 8 1 6 0 7 4 9 3
1 3 0 4 2
'''
