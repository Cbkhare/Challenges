from sys import argv
#import re, math, ast, operator import itemgetter
import itertools

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n').split(' | ') for line in fp]
track = [' '.join(item) for item in contents]
content = [list(map(int,item.split(' '))) for item in track]


#NOTE:-above 3  lines can also be written as
#contents=[list(map(int,(' '.join(line.strip('\n').split(' | '))).split(' '))) for line in fp]

#print (content)#s,'\n',content)
#print (contents,content)


def check_palindrome(num):
    num = str(num)
    lenth = len(num)
    count = 0               #current location of the string
    while count <= lenth/2:
        if num[count] != num[lenth-1-count]:  #checking mirror opp number
            return False
        count +=1
    return True

        

def check_intresting_ranges(p_lst):
    count_i = 0                  #counts no. of Intresting ranges
    for i in range(1,len(p_lst)+1):
        for j in range(len(p_lst)):
            if i+j > len(p_lst):
                break
            p_count = 0
            for x in range(j,i+j):
                if p_lst[x]:
                    p_count +=1
                #print (i,j,x,p_lst[x],p_count)
            if p_count%2 == 0:
                count_i +=1
            #print(count_i)
    return count_i
            

if __name__=='__main__':
    for item in content:
        p_lst = []     #palindrome list
        for i in range(item[0],item[1]+1):
             p_lst.append(check_palindrome(i))
        #print (p_lst, len(p_lst))
        print (check_intresting_ranges(p_lst))
    
'''
Palindromic Ranges

Challenge Description:

A positive integer is a palindrome if its decimal representation (without leading zeros) is a palindromic string (a string that reads the same forwards and backwards). For example, the numbers 5, 77, 363, 4884, 11111, 12121 and 349943 are palindromes.

A range of integers is interesting if it contains an even number of palindromes. The range [L, R], with L <= R, is defined as the sequence of integers from L to R (inclusive): (L, L+1, L+2, ..., R-1, R). L and R are the range's first and last numbers.

The range [L1,R1] is a subrange of [L,R] if L <= L1 <= R1 <= R. Your job is to determine how many interesting subranges of [L,R] there are.
Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file is one test case. Each test case will contain two positive integers, L and R (in that order), separated by a space. eg.

1 2
1 7
87 88

Output sample:

For each line of input, print out the number of interesting subranges of [L,R] eg.

1
12
1

For the curious: In the third example, the subranges are: [87](0 palindromes), [87,88](1 palindrome),[88](1 palindrome). Hence the number of interesting palindromic ranges is 1 '''
