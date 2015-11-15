
#In case data is passed as a parameter

from sys import argv, getsizeof
#from operator import itemgetter
#import re
#import math
from itertools import permutations, product
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n').split(';') for line in fp]


class Solution:
    def spiralOrder(self, A):
        result = []
        d = 0
        #d = 0 (pop elem from first row traversing left to right, and then del the empty list)
        #d = 1 (pop last element of each list from the list)
        #d = 2 (pop elem from last row traversing right to left, and then del the empty list)
        #d = 3 (pop first elem from each list from the list)
        #Note below if condtions can be removed along with reintializing d        
        while len(A) > 0 :
            if d==0: 
                while len(A[0]) > 0:
                    result.append(A[0].pop(0))
                del A[0]
                d=1
            if d ==1:
                for lst in A:
                    if len(lst)==0:
                        del lst
                        continue
                    result.append(lst.pop(len(lst)-1))
                d=2 
            if d ==2:
                if len(A)==0: continue
                while len(A[len(A)-1]) >0:   #i.e the last list of the Array 
                    result.append(A[len(A)-1].pop(len(A[len(A)-1])-1))
                del A[len(A)-1]
                d =3
            if d==3:
                mack = []
                for lst in A:
                    if len(lst)==0:
                        del lst
                        continue
                    mack.append(lst.pop(0))
                mack.reverse()
                result+=mack
                d=0
        return result

if __name__ == '__main__':

    for item in contents:
        back = []
        it = item[2].split(' ')
        for i in range(int(item[0])):
            track = []
            for j in range(int(item[1])):
                track.append(it.pop(0))
            back.append(track)
        #print (back)
        test = Solution()
        re = test.spiralOrder(back)
        #re = list(map(str,test.spiralOrder(back)))
        print (' '.join(re))
        
'''
piral Printing

Challenge Description:

Write a program to print a 2D array (n x m) in spiral order (clockwise)
Input sample:

Your program should accept as its first argument a path to a filename. The input file contains several lines. Each line is one test case. Each line contains three items (semicolon delimited). The first is 'n'(rows), the second is 'm'(columns) and the third is a single space separated list of characters/numbers in row major order. E.g.

3;3;1 2 3 4 5 6 7 8 9
3;3;a b c d e f g h i
3;3;11 12 13 14 15 16 17 18 19

Output sample:

Print out the matrix in clockwise fashion, one per line, space delimited. E.g.

1 2 3 6 9 8 7 4 5
a b c f i h g d e
11 12 13 16 19 18 17 14 15
'''
