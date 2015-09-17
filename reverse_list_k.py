import sys
from itertools import chain, combinations

file_name = sys.argv[1]
fp = open(file_name, 'r+')
contents = [line.strip('\n').split(';') for line in fp]

#print (contents)

def reverse(lst,k):
    stack = []
    i = 0.0
    c =float(len(lst)/k)
    while i <= c:
        if k <= len(lst):
            cur_lst = lst[0:k]
            cur_lst.reverse()
            stack = list(chain(stack,cur_lst))
            lst = lst[k:]
        else:
            stack = list(chain(stack,lst))
        i+=1
    return stack
          
for item in contents:
    num_lst = list(map(int,list(item[0].split(','))))
    ans = reverse (num_lst,int(item[1]))
    print (str(ans).replace('[','').replace(']','').replace(', ',','))

'''

 Given a list of numbers and a positive integer k, reverse the elements of the list, k items at a time. If the number of elements is not a multiple of k, then the remaining items in the end should be left as is.
Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file contains a list of numbers and the number k, separated by a semicolon. The list of numbers are comma delimited. E.g.

1,2,3,4,5;2
1,2,3,4,5;3

Output sample:

Print out the new comma separated list of numbers obtained after reversing. E.g.

2,1,4,3,5
3,2,1,4,5

'''



