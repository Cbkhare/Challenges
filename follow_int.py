from sys import argv, getsizeof
from itertools import permutations

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n') for line in fp]


for item in contents:

    ps = list(item)
    ps.sort(reverse=True)
    stat = 'Hold'
    stack = []
    
    if  ''.join(ps) == item:   #Stage at which we need to append 0
        ps.sort()
        for i in range(len(ps)):
            if ps[i]== '0':
                continue
            else:
                stack += ps.pop(i)
                break
        ps.append('0')
        ps.sort()
        stack += ps
        print (''.join(stack))
    else:
        ls = int(''.join(['9']*len(ps)))
        ts = permutations(ps,len(ps))
        #z= [p for p in permutations(x,4) if int(''.join(p)) > 5000 ]
        for t in ts:
            num = int(''.join(t))
            if num > int(item) and num<= ls:
                ls = num
        print (ls)
        

'''
You are writing out a list of numbers.Your list contains all numbers with exactly Di digits in its decimal representation which are equal to i, for each i between 1 and 9, inclusive. You are writing them out in ascending order. For example, you might be writing every number with two '1's and one '5'. Your list would begin 115, 151, 511, 1015, 1051. Given N, the last number you wrote, compute what the next number in the list will be. The number of 1s, 2s, ..., 9s is fixed but the number of 0s is arbitrary.
Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file is one test case. Each test case will contain an integer n < 10^6. E.g.

115
842
8000

Output sample:

For each line of input, generate a line of output which is the next integer in the list. E.g.

151
2048
80000
'''
