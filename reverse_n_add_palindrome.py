import sys
#from itertools import chain, combinations

file_name = sys.argv[1]
fp = open(file_name, 'r+')
contents = [line.strip('\n') for line in fp]

#print (contents)

def check_palindrome(num):
    num = str(num)
    lenth = len(num)
    count = 0               #current location of the string
    while count <= lenth/2:
        if num[count] != num[lenth-1-count]:  #checking mirror opp number
            return False
        count +=1
    return True

def reverse(n):
    num = list(map(int,(str(n).split(','))))
    s_num = str(num)
    r= list(s_num[1:len(s_num)-1])
    r.reverse()
    r = int(''.join(r))
    return r
    

for item in contents:
    p_num = int(item)
    counter = 0
    while check_palindrome(p_num) != True:
        num   = p_num
        r_num = reverse(num) 
        p_num = num+r_num
        counter +=1
    print (counter,p_num)

'''
 The problem is as follows: choose a number, reverse its digits and add it to the original. If the sum is not a palindrome (which means, it is not the same number from left to right and right to left), repeat this procedure.

For example:

195 (initial number) + 591 (reverse of initial number) = 786

786 + 687 = 1473

1473 + 3741 = 5214

5214 + 4125 = 9339 (palindrome)

In this particular case the palindrome 9339 appeared after the 4th addition. This method leads to palindromes in a few step for almost all of the integers. But there are interesting exceptions. 196 is the first number for which no palindrome has been found. It is not proven though, that there is no such a palindrome.
Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file is one test case. Each test case will contain an integer n < 10,000. Assume each test case will always have an answer and that it is computable with less than 100 iterations (additions).
Output sample:

For each line of input, generate a line of output which is the number of iterations (additions) to compute the palindrome and the resulting palindrome. (they should be on one line and separated by a single space character).

For example:

4 9339
'''
