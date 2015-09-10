from sys import argv
#from re import search


file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n').split(',') for line in fp ]
#print (contents)

stack = []
for item in contents:
    if item[0]=='':
        continue
    elif len(item)==1:
        m_stack = list(map(int,item))
    else:
        lst = [int(i) for i in item]
        sum_stack = []
        n = len(lst)
        for i in range(n,0,-1):      #from last int in the list to first element
            for j in range(0,i):   #include single element of lists
                sum_stack.append(sum(lst[j:i]))
        m_stack= [int(i) for i in sum_stack]
        #print (m_stack)
    stack.append(max(m_stack))

for data in stack:
    print (data)


'''
 Write a program to determine the largest sum of contiguous integers in a list.
Input sample:

The first argument is a path to a filename containing a comma-separated list of integers, one per line.

For example:

-10,2,3,-2,0,5,-15
2,3,-2,-1,10


Output sample:

Print to stdout the largest sum. In other words, of all the possible contiguous subarrays for a given array, find the one with the largest sum, and print that sum.

For example:
8
12
'''
