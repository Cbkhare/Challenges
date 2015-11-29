
#In case data is passed as a parameter
'''
from sys import argv, getsizeof
#from operator import itemgetter
#import re
#import math
from itertools import permutations, product
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n').split(';') for line in fp]
'''
from sys import argv, getsizeof as g
from itertools import permutations
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = tuple(map(str,A))
        y = sorted(A,reverse=True)
        if y.count('0')==len(y):
            return '0'
        num = ''
        i = 2
        while len(y)>0:
            #print (i,y[0],y[1])
            i+=3
            #print (y)
            if len(y)==1:
                num +=y.pop(0)
                continue
            if int(y[0]+y[1]) > int(y[1]+y[0]):    #XY>YX
                num+=y.pop(0)
                continue
            else:
                num+= (y.pop(1))
                #num+= (y.pop(1)+y.pop(0))
                continue
        return num
        
            

if __name__ == '__main__':

    B = Solution()

    n = int(input())
    for j in range(n):
        print (B.largestNumber(tuple(input().split(', '))))
    '''
    #For Large Input
    file_name = argv[1]
    fp = open(file_name,'r+')
    con = fp.readline().split(',') #for line in fp]) 
    print (B.largestNumber(tuple(map(int,con))))
    '''


'''


Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
'''
